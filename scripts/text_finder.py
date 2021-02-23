import re


def get_end_point(text: str, search: str):
    found = re.search(search, text)
    return 0 if not found else found.end()


def get_sex(text: str) -> tuple:
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
            sex = 'Неизвестно'
        return (second_name, first_name, middle_name, sex,
                    text[get_end_point(text, middle_name):])
    else:
        return ('unknown', 'unknown', 'unknown', 'unknown', text)


def get_diagnosis(text: str) -> tuple:
    diag_text = get_text_between_sections('с диагнозом', 'жалобы пациента', text)
    base_diag = find_diagnosis(diag_text, 'base')
    return ()


def find_diagnosis(text: str, type: str) -> dict:
    if type == 'base':
        base_diag = get_text_between_sections('основной', 'осложнение', text)
        print(base_diag)


def get_text_between_sections(beg_sec: str, end_sec: str, text: str) -> str:
    # ищем позиции тегов в тексте
    beg_point = re.search(beg_sec, text)
    end_point = re.search(end_sec, text)
    if beg_point is not None and end_point is not None:
        return text[beg_point.end():end_point.start()]
    return ''
