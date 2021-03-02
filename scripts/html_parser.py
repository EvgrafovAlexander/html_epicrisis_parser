from scripts.constants import COLUMNS
from .date_finder import get_date_between_few_sections
from .segment_finder import get_sex, get_diagnosis, get_complaints, get_anamnesis, get_test_results
from .constants import F_DATES


def text_parser(text: str, patient_id: int) -> dict:
    patient_data = {col: None for col in COLUMNS}
    patient_data['id'] = patient_id
    # break into lines and remove leading and trailing space on each
    #lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    #chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    #text = '\n'.join(chunk for chunk in chunks if chunk)

    name_dict, text = get_sex(text)
    patient_data.update(name_dict)

    text = text.lower()

    dob = get_date_between_few_sections(F_DATES['dob'], text)
    patient_data['dob'] = dob

    treatment_start = get_date_between_few_sections(F_DATES['treatment_start'], text)
    patient_data['treatment_start'] = treatment_start

    treatment_stop = get_date_between_few_sections(F_DATES['treatment_stop'], text)
    patient_data['treatment_stop'] = treatment_stop

    diag_dict, text = get_diagnosis(text)
    patient_data.update(diag_dict)

    comp_dict, text = get_complaints(text)
    patient_data.update(comp_dict)

    anam_dict, text = get_anamnesis(text)
    patient_data.update(anam_dict)

    test_dict, text = get_test_results(text)

    return patient_data
