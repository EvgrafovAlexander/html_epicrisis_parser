import re
from .constants import DIAG_DICT, F_BASE_DIAG, F_COMP_DIAG


def get_end_point(text: str, search: str) -> int:
    found = re.search(search, text)
    return 0 if not found else found.end()


def get_sex(text: str) -> tuple:
    name_dict = {'first_name': None,
                 'second_name': None,
                 'middle_name': None,
                 'sex': None}
    reg_exp = r"[А-Я][а-я]+\s[А-Я][а-я]+\s[А-Я][а-я]+"

    found = re.findall(reg_exp, text)
    if len(found) > 0:
        full_name = found[0].split()
        second_name, first_name, middle_name = full_name

        if middle_name[-3:] == 'вна':
            sex = 'Женский'
        elif middle_name[-3:] == 'вич':
            sex = 'Мужской'
        else:
            sex = None

        name_dict['first_name'] = first_name
        name_dict['second_name'] = second_name
        name_dict['middle_name'] = middle_name
        name_dict['sex'] = sex

        return (name_dict, text[get_end_point(text, middle_name):])
    else:
        return (name_dict, text)


def get_diagnosis(text: str) -> tuple:
    diag_dict = {'base': None,
                 'identified': None,
                 'form': None,
                 'complication': None,
                 'respiratory_distress': None}
    diag_text = get_text_between_sections('с диагнозом', 'жалобы пациента', text)
    diag_dict = find_diagnosis(diag_text, diag_dict, 'base')
    diag_dict = find_diagnosis(diag_text, diag_dict, 'comp')
    return (diag_dict, text)


def find_diagnosis(text: str, diag_dict: dict, type: str) -> dict:
    if type == 'base' and text is not None:
        base_diag_text = get_text_between_few_sections(F_BASE_DIAG, text)
        if base_diag_text:
            diag_dict['base'] = classify_by_dict(base_diag_text, DIAG_DICT['base'])
            diag_dict['identified'] = classify_by_dict(base_diag_text, DIAG_DICT['identified'])
            diag_dict['form'] = classify_by_dict(base_diag_text, DIAG_DICT['form'])
    if type == 'comp' and text is not None:
        comp_diag_text = get_text_between_few_sections(F_COMP_DIAG, text)
        if comp_diag_text:
            diag_dict['complication'] = classify_by_dict(comp_diag_text, DIAG_DICT['complication'])
    return diag_dict


def classify_by_dict(text: str, classifier: dict):
    for key in classifier.keys():
        for item in classifier[key]:
            if item in text:
                return key
    return None


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
