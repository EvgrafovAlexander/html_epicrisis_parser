import re, logging

from .classifier import classify_by_dict
from .constants import DIAG_DICT, F_BASE_DIAG, F_COMP_DIAG, F_CONC_DIAG, END_DIAG, F_COMPLAINTS, COMPLAINTS_DICT, \
    F_TEXT, END_COMP, F_ANAMNESIS, END_ANAM
from .number_finder import get_nums_from_text
from .text_finder import get_end_point, get_end_few_point, \
    get_text_between_few_sections, is_words_in_text
from .table_finder import create_table_info, table_handler, prepare_data


# ---------- ФИО и пол ----------
def get_sex(text: str) -> tuple:
    name_dict = {'имя': None,
                 'фамилия': None,
                 'отчество': None,
                 'пол': None}
    found = find_names(text)
    if len(found) > 0:
        full_name = found[0].title().split()
        second_name, first_name, middle_name = full_name

        if middle_name[-3:] == 'вна':
            sex = 'Женский'
        elif middle_name[-3:] == 'вич':
            sex = 'Мужской'
        else:
            sex = None

        name_dict['имя'] = first_name
        name_dict['фамилия'] = second_name
        name_dict['отчество'] = middle_name
        name_dict['пол'] = sex

        return (name_dict, text[get_end_point(text, middle_name):])
    else:
        logging.info('Не найден фрагмент: ФИО и пол')
        return (name_dict, text)


def find_names(text: str) -> str or None:
    reg_list = [r"[А-Яа-я]+\s[А-Яа-я]+\s[А-Яа-я]+вич",
                r"[А-Яа-я]+\s[А-Яа-я]+\s[А-Яа-я]+вна",
                r"[А-Яа-я]+\s[А-Яа-я]+\s[А-Яа-я]+ВИЧ",
                r"[А-Яа-я]+\s[А-Яа-я]+\s[А-Яа-я]+ВНА"]
    name_text = text[:700]
    for reg_exp in reg_list:
        found = re.findall(reg_exp, name_text)
        if found:
            return found
    return None


# ---------- Диагноз ----------
def get_diagnosis(text: str) -> tuple:
    diag_dict = {'base': None,
                 'identified': None,
                 'form': None,
                 'complication': None,
                 'respiratory_distress': None,
                 'is_concomitant_disease': '-',
                 'conc_dieases_text': None}
    diag_text = get_text_between_few_sections(F_TEXT['diagnosis'], text)
    if diag_text:
        diag_dict = find_diagnosis(diag_text, diag_dict, 'base')
        diag_dict = find_diagnosis(diag_text, diag_dict, 'comp')
        diag_dict = find_diagnosis(diag_text, diag_dict, 'conc')
    else:
        logging.info('Не найден фрагмент: Диагноз')
    text = text[get_end_few_point(text, END_DIAG):]
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
            diag_dict['respiratory_distress'] = find_resp_distress(comp_diag_text)
    if type == 'conc' and text is not None:
        conc_diag_text = get_text_between_few_sections(F_CONC_DIAG, text)
        if conc_diag_text:
            diag_dict['is_concomitant_disease'] = '+'
            # TODO - Добавить классификатор сопутствующих заболеваний
            diag_dict['conc_dieases_text'] = conc_diag_text
        else:
            diag_dict['conc_dieases_text'] = 'Отсутствуют'
    return diag_dict


def find_resp_distress(text: str) -> int or None:
    # TODO - Добавить определение римских чисел
    nums = get_nums_from_text(text)
    if nums is not None:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[-1]
    return None


# ---------- Жалобы ----------
def get_complaints(text: str) -> tuple:
    compl_dict = {'is_weakness': None,
                  'is_aches': None,
                  'is_dyspnea_at_rest': None,
                  'is_dyspnea_at_stress': None}
    compl_text = get_text_between_few_sections(F_COMPLAINTS, text)
    if compl_text is not None:
        compl_dict['is_weakness'] = is_words_in_text(COMPLAINTS_DICT['is_weakness'], compl_text)
        compl_dict['is_aches'] = is_words_in_text(COMPLAINTS_DICT['is_aches'], compl_text)
        compl_dict['is_dyspnea_at_rest'] = is_words_in_text(COMPLAINTS_DICT['is_dyspnea_at_rest'], compl_text)
        compl_dict['is_dyspnea_at_stress'] = is_words_in_text(COMPLAINTS_DICT['is_dyspnea_at_stress'], compl_text)
    else:
        logging.info('Не найден фрагмент: Жалобы')
    text = text[get_end_few_point(text, END_COMP):]
    return (compl_dict, text)


# ---------- Анамнез ----------
def get_anamnesis(text: str) -> tuple:
    anamn_dict = {}
    anamn_text = get_text_between_few_sections(F_ANAMNESIS, text)
    if anamn_text:
        # TODO: Выполнить парсинг анамнеза
        pass
    else:
        logging.info('Не найден фрагмент: Анамнез')
    text = text[get_end_few_point(text, END_ANAM):]
    return anamn_dict, text


# ---------- Результаты исследований ----------
def get_test_results(text: str, patient_id: int) -> tuple:
    tables_data = {}
    table_info = create_table_info(text)
    for table in table_info:
        table_data = table_handler(text, table)
        table_data = prepare_data(table_data, patient_id)
        tables_data[table['name']] = table_data
    if len(table_info):
        start = table_info[-1]['start']
        text = text[start:]
    return tables_data, text
