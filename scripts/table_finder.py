import re, logging
from datetime import datetime
from typing import List
from .table_constants import TABLE_FINDER_DICT, TABLE_DICT


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
    for name in table_names:
        found = re.search(name, text)
        if found:
            return found.start()
    return None


def order_table_info(text: str, seg_tables: list) -> List[dict]:
    segmented_table_info = []
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
        table_text = text[table_info['start']:table_info['stop']]
        table_data = information_extractor(table_text, TABLE_DICT[name])
    else:
        logging.info('Таблица "%s" не найдена в словаре.', name)
    return table_data


def information_extractor(text: str, table_dict: dict) -> List[dict]:
    data_list = []
    data_dict = {key: None for key in table_dict.keys()}

    fragments = text.split('\n')
    columns = []
    col_mode, fill_mode = True, False
    cur_ind, max_ind, data_dict_cur = 0, 0, {}
    add_allowed = True
    for fragment in fragments:
        if col_mode:
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
                date = datetime.strptime(fragment[date.start():date.end()], '%d.%m.%Y')
                data_dict_cur = data_dict.copy()
                data_dict_cur['дата'] = date
                cur_ind = 0
                max_ind = len(columns)
                col_mode = False
                fill_mode = True
                add_allowed = False
                continue
        if fill_mode:
            if cur_ind < max_ind:
                data_dict_cur[columns[cur_ind]] = value_handler(fragment,
                                                                columns[cur_ind],
                                                                table_dict[columns[cur_ind]])
                cur_ind += 1
            else:
                data_list.append(data_dict_cur)
                fill_mode = False
                col_mode = True
    if len(data_list):
        data_list = delete_empty_rec(data_list)
    return data_list


def find_column(fragment: str, table_dict: dict) -> str or None:
    columns = [k for k in table_dict.keys()]
    if fragment != '':
        for column in columns:
            if fragment in column:
                return column
    return None


def value_handler(value: str, column: str, table_dict: dict):
    value_type = table_dict['type']
    value_unit = table_dict['unit']
    value = value_parser(value, value_type, value_unit)
    return value


def value_parser(value: str, value_type: str, value_unit: List[str]):
    re_dict = {'float': r'^\d+(?:[\.,]\d+)?',
               'int': r'^\d+(?:[\.,]\d+)?'}
    parsed_value = None
    value = prepare_value(value)
    if is_unit_matched(value, value_unit):
        matches = re.findall(re_dict[value_type], value)
        if len(matches):
            parsed_value = float(matches[0])
    elif value != '':
        logging.info('Недостоверное значение: %s', value_unit)
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
    for row in data:
        row['id'] = patient_id
    return data
