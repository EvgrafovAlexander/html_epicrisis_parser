import codecs
import logging
import os
import re
from bs4 import BeautifulSoup
from datetime import datetime

from scripts.constants import PATH_ANON_LOAD, PATH_ANON_SAVE, F_DATES
from scripts.date_finder import get_date_between_few_sections
from scripts.segment_finder import get_sex


def main():
    start_date = datetime.today()

    if not os.path.isdir('Anon_data'):
        os.mkdir('Anon_data')
    logging.basicConfig(filename='logs_anon.log', level=logging.INFO)
    logging.info('Анонимизация эпикризов. Начало обработки')

    file_names = os.listdir(path=PATH_ANON_LOAD)
    for name in file_names:
        logging.info('Документ %s в обработке:', name)
        with codecs.open(PATH_ANON_LOAD + name, "r", "utf-8") as html:
            init_text = BeautifulSoup(html, features="html.parser").get_text().encode('utf-8').decode()

            proc_text = init_text
            data, proc_text = get_sex(proc_text)
            proc_text = proc_text.lower()
            data['dob'] = get_date_between_few_sections(F_DATES['dob'], proc_text)

            anon_text = anonymize(init_text, data)

            with open(PATH_ANON_SAVE + name + ".txt", "w", encoding='utf-8') as file:
                file.write(anon_text)
        logging.info('Документ %s обработан\n', name)

    work_interval = (datetime.today() - start_date).microseconds
    logging.info('Завершение обработки')
    logging.info('Продолжительность обработки: %.2f с.', float(work_interval / 10**6))


def anonymize(text: str, data: dict) -> str:
    data_for_anon = {'Мужской': {'имя': 'Иван', 'фамилия': 'Иванов', 'отчество': 'Иванович'},
                     'Женский': {'имя': 'Мария', 'фамилия': 'Петрова', 'отчество': 'Ивановна'}}
    if data['пол'] is not None:
        data_for_anon = data_for_anon[data['пол']]
        for word in data_for_anon:
            if data[word] is not None:
                text = re.sub(data[word], data_for_anon[word], text)
                text = re.sub(data[word].upper(), data_for_anon[word], text)
    if data['dob'] is not None:
        dob = data['dob']
        anon_dob = dob.replace(month=1, day=1)
        dob_str = dob.strftime('%d.%m.%Y')
        anon_dob_str = anon_dob.strftime('%d.%m.%Y')
        text = re.sub(dob_str, anon_dob_str, text)
    return text


if __name__ == "__main__":
    main()
