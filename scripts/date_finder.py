import re
from datetime import datetime
from .text_finder import get_end_point


def get_date_between_sections(beg_sec: str, end_sec: str, text: str) -> tuple:
    # ищем позиции тегов в тексте
    beg_point = re.search(beg_sec, text)
    end_point = re.search(end_sec, text)
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
        return (datetime.strptime('01.01.' + year, '%d.%m.%Y').date(),
                text[get_end_point(text, matches[0]):])

    return (datetime.strptime("01.01.1800", '%d.%m.%Y').date(),
            text[get_end_point(text, matches[0]):])
