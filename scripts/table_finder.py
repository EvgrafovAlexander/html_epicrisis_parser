import re, logging
from typing import List
from .table_constants import TABLE_FINDER_DICT


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
    print(sep)
    print()
    print()
    return {}

