import re
from scripts.constants import COLUMNS


def get_sex(text: str) -> tuple:
    reg_exp = r"[А-Я][а-я]+\s[А-Я][а-я]+\s[А-Я][а-я]+"
    found = re.findall(reg_exp, text)
    if len(found):
        full_name = found[0].split()
        second_name, first_name, middle_name = full_name
        if middle_name[-3:] == 'вна':
            sex = 'Женский'
        elif middle_name[-3:] == 'вич':
            sex = 'Мужской'
        else:
            sex = 'Неизвестно'
        return (second_name, first_name, middle_name, sex)
    else:
        return ('unknown', 'unknown', 'unknown', 'unknown')


def text_parser(data: str) -> dict:
    patient_data = {col: None for col in COLUMNS}

    second_name, first_name, middle_name, sex = get_sex(data)
    patient_data['second_name'] = second_name
    patient_data['first_name'] = first_name
    patient_data['middle_name'] = middle_name
    patient_data['sex'] = sex

    return patient_data
