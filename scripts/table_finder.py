import re, logging
from datetime import datetime
from typing import List
from .table_constants import TABLE_FINDER_DICT, TABLE_DICT
from .date_finder import get_date_between_sections


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


def table_handler(text: str, table_info: dict) -> dict:
    name = table_info['name']
    table_text = text[table_info['start']:table_info['stop']]
    sep = table_text.split('\n')
    if name == 'Коагулограмма':
        #print(sep)
        information_extractor(table_text, TABLE_DICT['Коагулограмма'])
        #print()
        #print()
    return {}


def information_extractor(text: str, table_dict: dict):
    data_list = []
    data_dict = {key: None for key in table_dict.keys()}

    fragments = text.split('\n')
    columns = []
    col_mode, fill_mode = True, False
    cur_ind, max_ind, data_dict_cur = 0, 0, {}
    add_allowed = True
    for fragment in fragments:
        if col_mode:
            if fragment in table_dict:
                if add_allowed:
                    columns.append(fragment)
                else:
                    columns = []
                    add_allowed = True
                    columns.append(fragment)

            date = re.search(r'\d\d.\d\d.\d\d\d\d', fragment)
            if date:
                date = datetime.strptime(date.string, '%d.%m.%Y')
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
                data_dict_cur[columns[cur_ind]] = fragment
                cur_ind += 1
            else:
                data_list.append(data_dict_cur)
                fill_mode = False
                col_mode = True
    return data_list


