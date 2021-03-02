import re
from .table_constants import TABLE_FINDER_DICT


def segment_tables(text: str) -> list:
    seg_tables = []
    #print(text)
    for table_name in TABLE_FINDER_DICT.keys():
        table_start = get_table_begin(text, TABLE_FINDER_DICT[table_name])
        if table_start is not None:
            table_info = {table_start: table_name}
            seg_tables.append(table_info)
    print(seg_tables)



def get_table_begin(text: str, table_names: list) -> int or None:
    for name in table_names:
        found = re.search(name, text)
        if found:
            return found.start()
    return None
