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
