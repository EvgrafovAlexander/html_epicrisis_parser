import re
from typing import List


def get_end_few_point(text: str, search_list: List[str]) -> int:
    for search in search_list:
        found = get_end_point(text, search)
        if found != 0:
            return found
    return 0


def get_end_point(text: str, search: str) -> int:
    found = re.search(search, text)
    return 0 if not found else found.start()


def get_text_between_sections(beg_sec: str, end_sec: str, text: str) -> str or None:
    # ищем позиции тегов в тексте
    beg_point = re.search(beg_sec, text)
    end_point = re.search(end_sec, text)
    if beg_point is not None and end_point is not None:
        return text[beg_point.start():end_point.end()]
    return None


def get_text_between_few_sections(sections: list, text: str) -> str or None:
    for section in sections:
        found = get_text_between_sections(section[0], section[1], text)
        if found:
            return found
    return None


def is_words_in_text(words: list, text: str):
    for word in words:
        if word in text:
            return True
    return False
