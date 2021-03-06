import re, logging
from collections import Counter
from datetime import datetime
from typing import List
from .table_constants import TABLE_FINDER_DICT, TABLE_DICT
from .classifier import classify_by_dict


def create_table_info(text: str) -> List[dict]:
    """Сформировать список с информацией о таблицах по правилу:
    Наименование - Индекс начала - Индекс конца таблицы"""
    seg_tables = []
    for table_name in TABLE_FINDER_DICT.keys():
        table_start = get_table_begin(text, TABLE_FINDER_DICT[table_name])
        if table_start is not None:
            info = [table_start, table_name]
            seg_tables.append(info)
    # упорядочить по мере нахождения и дополнить
    # данными об окончании таблиц
    table_info = order_table_info(text, sorted(seg_tables))
    return table_info


def get_table_begin(text: str, table_names: list) -> int or None:
    """Найти индекс начала таблицы по ее наименованию"""
    for name in table_names:
        found = re.search(name, text)
        if found:
            return found.start()
    return None


def order_table_info(text: str, seg_tables: list) -> List[dict]:
    segmented_table_info = []
    if not seg_tables: return segmented_table_info
    for i in range(len(seg_tables) - 1):
        info = {'name': seg_tables[i][1],
                'start': seg_tables[i][0],
                'stop': seg_tables[i+1][0]}
        segmented_table_info.append(info)
    # в данном контексте проводится поиск конца последней таблицы
    last = get_table_begin(text[seg_tables[-1][0]:],
                    ['лечение', 'заключение', 'рекомендации'])
    last = len(text) if last is None else seg_tables[-1][0] + last
    info = {'name': seg_tables[-1][1],
            'start': seg_tables[-1][0],
            'stop': last}
    segmented_table_info.append(info)
    logging.info('Найдено таблиц: %d', len(segmented_table_info))
    return segmented_table_info


def table_handler(text: str, table_info: dict) -> List[dict]:
    table_data = []
    name = table_info['name']
    if name in TABLE_DICT:
        logging.info('\nОбработка таблицы: "%s"', name)
        table_text = text[table_info['start']:table_info['stop']]
        table_data = information_extractor(table_text, TABLE_DICT[name])
    else:
        logging.info('Таблица "%s" не найдена в словаре.', name)
    return table_data


def information_extractor(text: str, table_dict: dict) -> List[dict]:
    """Извлечь информацию из текстового фрагмента.
    Включает 2 режима:
    - col_mode (not fill_mode) - собирает список параметров, исходя
    из перечня возможных параметров конкретной таблицы;
    - fill_mode - заполняет словарь в соответствии с собранным списком"""
    data_list = []
    data_dict = {key: None for key in table_dict.keys()}

    fragments = text.split('\n')
    if len(fragments) <= 1:
        logging.info('Не удалось разделение на фрагменты\n')
    columns = []
    fill_mode = False
    cur_ind, max_ind, data_dict_cur = 0, 0, {}
    add_allowed = True
    for fragment in fragments:
        if not fill_mode:
            column_found = find_column(fragment, table_dict)
            if column_found:
                if add_allowed:
                    columns.append(column_found)
                else:
                    columns = []
                    add_allowed = True
                    columns.append(column_found)

            date = re.search(r'\d\d.\d\d.\d\d\d\d', fragment)
            if date:
                date = fragment[date.start():date.end()].replace('/', '.')
                date = datetime.strptime(date, '%d.%m.%Y')
                data_dict_cur = data_dict.copy()
                data_dict_cur['дата'] = date
                cur_ind = 0
                max_ind = len(columns)
                fill_mode = True
                add_allowed = False
                continue
        else:
            if cur_ind < max_ind:
                data_dict_cur[columns[cur_ind]] = value_handler(fragment,
                                                                columns[cur_ind],
                                                                table_dict[columns[cur_ind]])
                cur_ind += 1
            else:
                data_list.append(data_dict_cur)
                fill_mode = False
    logging.info('Ожидаемые параметры: %s \n', ', '.join(columns))
    if len(data_list):
        data_list = delete_empty_rec(data_list)
    return data_list


def find_column(fragment: str, table_dict: dict) -> str or None:
    """Найти соответствие фрагмента текста
    с наименованием известных столбцов таблицы"""
    columns = [k for k in table_dict.keys()]
    if fragment != '':
        for column in columns:
            if column in fragment:
                return column
    return None


def value_handler(value: str, column: str, table_dict: dict):
    value_type = table_dict['type']
    value_unit = table_dict['unit']
    if value_type in ['float']:
        value = value_parser_float(value, value_type, value_unit, column)
    if value_type in ['class']:
        value = value_parser_mixed(value, value_type, value_unit, column)
    if value_type in ['not']:
        value = value
    return value


def value_parser_float(value: str, value_type: str, value_unit: List[str], column: str):
    parsed_value = None
    re_dict = {'float': r'^\d+(?:[\.,]\d+)?'}
    value = prepare_value(value)
    if is_unit_matched(value, value_unit):
        matches = re.findall(re_dict[value_type], value)
        if len(matches):
            parsed_value = float(matches[0])
    elif value.rstrip() not in ['', '\xa0']:
        logging.info("""Недостоверное значение:
                    Столбец: {} 
                    Значение: {}
                    Ожидаемые единицы измерения: {}""".format(column, value, value_unit))
    return parsed_value


def value_parser_class(value: str, value_type: str, classes: dict):
    parsed_value = classify_by_dict(value, classes)
    return parsed_value


def value_parser_mixed(value: str, value_type: str, classes: dict, column: str):
    value = prepare_value(value)
    matches = re.findall(r'^\d+(?:[\.,]\d+)?', value)
    if len(matches):
        parsed_value = float(matches[0])
    else:
        parsed_value = classify_by_dict(value, classes)
    return parsed_value


def is_unit_matched(value: str, units: List[str]) -> bool:
    """Проверка совпадения единиц измерения
       полученного и ожидаемого значения"""
    for unit in units:
        matches = re.findall(unit, value)
        if len(matches):
            return True
    return False


def delete_empty_rec(data: List[dict]) -> List[dict]:
    """Удалить из результата записи,
    содержащие менее 2 единиц информации"""
    result = []
    for rec in data:
        all_columns_sum = len(rec.keys())
        none_columns_sum = len([val for val in rec.values() if val is None])
        if none_columns_sum < all_columns_sum - 1:
            result.append(rec)
    return result


def prepare_value(value: str) -> str:
    """Подготовить полученное значение
    к обработке парсером"""
    value = value.replace(',', '.').replace('^', 'deg')
    return value


def prepare_data(data: list, patient_id: int):
    """Подготовить список записей перед отправкой
    в основную функцию (уровень List[dict])"""

    # 1. добавить patient_id
    for row in data:
        row['patient_id'] = patient_id

    # 2. объединить данные с одинаковыми датами
    result_data = []
    dates_cnt = Counter([row['дата'] for row in data])
    for date in dates_cnt:
        data_on_date = [row for row in data if row['дата'] == date]
        if dates_cnt[date] == 1:
            result_data.append(data_on_date[0])
        else:
            result_data.append(union_data_by_date(data_on_date))
    return result_data


def union_data_by_date(data: List[dict]) -> dict:
    """Объединить несколько строк одного вида анализа
    с одинаковыми датами в одну строку"""
    result = {col: None for col in data[0].keys()}
    for col in result:
        for row in data:
            if row[col] is not None and result[col] is None:
                result[col] = row[col]
                continue
    return result
