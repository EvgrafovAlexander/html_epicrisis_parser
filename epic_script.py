import codecs, os, logging
from bs4 import BeautifulSoup
from datetime import datetime
from scripts.data_to_df import add_patient, create_df_dict, save_dfs
from scripts.constants import PATH
from scripts.html_parser import text_parser
from scripts.table_constants import TABLE_DICT


def main():
    start_date = datetime.today()
    logging.basicConfig(filename='logs.log', level=logging.INFO)
    logging.info('Начало обработки')

    patient_id = 100001
    file_names = os.listdir(path=PATH)
    data_dfs = create_df_dict(TABLE_DICT)

    for name in file_names:
        logging.info('Документ {} в обработке:'.format(name))
        with codecs.open(PATH + name, "r", "utf-8") as html:
            text = BeautifulSoup(html, features="html.parser").get_text()
            patient_data = text_parser(text, patient_id)
            data_dfs = add_patient(data_dfs, patient_data)
            patient_id += 1
        logging.info('Документ {} обработан\n'.format(name))

    save_dfs(data_dfs)

    work_interval = (datetime.today() - start_date).microseconds
    logging.info('Завершение обработки')
    logging.info('Продолжительность обработки: %.2f с.', float(work_interval / 10**6))


if __name__ == "__main__":
    main()
