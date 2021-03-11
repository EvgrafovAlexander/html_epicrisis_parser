import codecs, os, logging
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from scripts.constants import COLUMNS, PATH
from scripts.html_parser import text_parser


def add_patient(df_data: dict, patient_data: dict):
    for key in df_data.keys():
        df_data[key].append(patient_data[key])


def main():
    start_date = datetime.today()
    logging.basicConfig(filename='logs.log', level=logging.INFO)
    logging.info('Начало обработки')

    id = 1
    data_for_df = {col: [] for col in COLUMNS}
    file_names = os.listdir(path=PATH)
    # TODO - Убрать следующую строку
    #file_names = [file_names[0]]
    for name in file_names:
        logging.info('Документ ' + str(name) + ' в обработке:')
        with codecs.open(PATH + name, "r", "utf-8") as html:
            text = BeautifulSoup(html, features="html.parser").get_text()
            patient_data = text_parser(text, id)
            add_patient(data_for_df, patient_data)
            id += 1
        logging.info('Документ ' + str(name) + ' обработан\n')

    df = pd.DataFrame(data=data_for_df)
    df.replace({True: '+', False: '-'}, inplace=True)

    df.to_excel("output.xlsx", sheet_name='Основная информация', index=False)

    work_interval = (datetime.today() - start_date).microseconds
    logging.info('Завершение обработки')
    logging.info('Продолжительность обработки: %.2f с.', float(work_interval / 10**6))


if __name__ == "__main__":
    main()
