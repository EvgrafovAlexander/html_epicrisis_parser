import re
from datetime import datetime
from .text_finder import get_end_point


# TODO - несоответствие возвращаемым типам в отдельных случаях
def get_date_between_sections(beg_sec: str, end_sec: str, text: str) -> datetime or None:
    # ищем позиции тегов в тексте
    beg_point = re.search(beg_sec, text)
    end_point = re.search(end_sec, text)
    if beg_point is not None and end_point is not None:
        # 27.12.1985
        matches = re.findall(r'\d\d.\d\d.\d\d\d\d', text[beg_point.end():end_point.start()])
        if matches:
            return (datetime.strptime(matches[0], '%d.%m.%Y').date(),
                    text[get_end_point(text, matches[0]):])
        # 27.12.85
        matches = re.findall(r'\d\d.\d\d.\d\d', text[beg_point.end():end_point.start()])
        if matches:
            day_mon = matches[0][:-2]
            year = matches[0][-2:]
            if int(year) > 35:
                year = '19' + matches[0][-2:]
            else:
                year = '20' + matches[0][-2:]
            return (datetime.strptime(day_mon + year, '%d.%m.%Y').date(),
                    text[get_end_point(text, matches[0]):])
        # 1985
        matches = re.findall(r'\d\d\d\d', text[beg_point.end():end_point.start()])
        if matches:
            return (datetime.strptime('01.01.' + matches[0], '%d.%m.%Y').date(),
                    text[get_end_point(text, matches[0]):])
        # 85
        matches = re.findall(r'\d\d', text[beg_point.end():end_point.start()])
        if matches:
            year = matches[0]
            if int(year) > 35:
                year = '19' + matches[0]
            else:
                year = '20' + matches[0]
            return datetime.strptime('01.01.' + year, '%d.%m.%Y').date()
    return None


def get_date_between_few_sections(sections: list, text: str) -> datetime or None:
    for section in sections:
        found = get_date_between_sections(section[0], section[1], text)
        if found:
            return found[0]
    return None


def get_date_in_fragment(text: str) -> datetime or None:
    # 27.12.1985
    matches = re.findall(r'\d\d.\d\d.\d\d\d\d', text)
    if matches:
        return datetime.strptime(matches[0], '%d.%m.%Y').date()
    # 27.12.85
    matches = re.findall(r'\d\d.\d\d.\d\d', text)
    if matches:
        day_mon = matches[0][:-2]
        year = matches[0][-2:]
        if int(year) > 35:
            year = '19' + matches[0][-2:]
        else:
            year = '20' + matches[0][-2:]
        return datetime.strptime(day_mon + year, '%d.%m.%Y').date()
    # 1985
    matches = re.findall(r'\d\d\d\d', text)
    if matches:
        return datetime.strptime('01.01.' + matches[0], '%d.%m.%Y').date()
    # 85
    matches = re.findall(r'\d\d', text)
    if matches:
        year = matches[0]
        if int(year) > 35:
            year = '19' + matches[0]
        else:
            year = '20' + matches[0]
        return datetime.strptime('01.01.' + year, '%d.%m.%Y').date()
    return None
