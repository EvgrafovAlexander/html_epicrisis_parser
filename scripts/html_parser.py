from scripts.constants import COLUMNS
from .date_finder import get_date_between_sections
from .text_finder import get_sex, get_diagnosis


def text_parser(text: str) -> dict:
    patient_data = {col: None for col in COLUMNS}

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    name_dict, text = get_sex(text)
    patient_data.update(name_dict)

    text = text.lower()

    dob, text = get_date_between_sections(r'дата рождения:', r'находился', text)
    patient_data['dob'] = dob

    treatment_start, text = get_date_between_sections(r'находился', r'по', text)
    patient_data['treatment_start'] = treatment_start

    treatment_stop, text = get_date_between_sections(r'по', r'адрес', text)
    patient_data['treatment_stop'] = treatment_stop

    diag_dict, text = get_diagnosis(text)
    patient_data.update(diag_dict)

    return patient_data
