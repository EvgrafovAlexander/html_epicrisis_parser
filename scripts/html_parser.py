from scripts.table_constants import TABLE_DICT
from .date_finder import get_date_between_few_sections
from .segment_finder import get_sex, get_diagnosis, get_complaints, get_anamnesis, get_test_results, get_treatment
from .constants import F_DATES


def text_parser(text: str, patient_id: int) -> dict:
    base_patient_data = {col: None for col in TABLE_DICT['Основная информация']}
    base_patient_data['id'] = patient_id
    # break into lines and remove leading and trailing space on each
    #lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    #chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    #text = '\n'.join(chunk for chunk in chunks if chunk)

    name_dict, text = get_sex(text)
    base_patient_data.update(name_dict)

    text = text.lower()

    dob = get_date_between_few_sections(F_DATES['dob'], text)
    base_patient_data['dob'] = dob

    treatment_start = get_date_between_few_sections(F_DATES['treatment_start'], text)
    base_patient_data['treatment_start'] = treatment_start

    treatment_stop = get_date_between_few_sections(F_DATES['treatment_stop'], text)
    base_patient_data['treatment_stop'] = treatment_stop

    diag_dict, text = get_diagnosis(text)
    base_patient_data.update(diag_dict)

    comp_dict, text = get_complaints(text)
    base_patient_data.update(comp_dict)

    anam_dict, drugs_before_dict, text = get_anamnesis(text, base_patient_data['treatment_start'])
    drugs_before_dict['id'] = patient_id
    base_patient_data.update(anam_dict)

    test_dict, text = get_test_results(text, patient_id)

    treat_during_dict, text = get_treatment(text, patient_id)
    treat_during_dict['id'] = patient_id

    # объединяем текстовые и табличные данные
    patient_data = {'Основная информация': [base_patient_data],
                    'Перед госпитализацией': [drugs_before_dict],
                    'Во время госпитализации': [treat_during_dict]}
    patient_data.update(test_dict)

    return patient_data
