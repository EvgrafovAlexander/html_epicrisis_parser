import codecs, os, logging
import pandas as pd
from bs4 import BeautifulSoup
from scripts.constants import COLUMNS, PATH
from scripts.html_parser import text_parser


def add_patient(df_data: dict, patient_data: dict):
    for key in df_data.keys():
        df_data[key].append(patient_data[key])


def main():
    logging.basicConfig(filename='logs.log', level=logging.INFO)
    logging.info('Запуск скрипта')

    id = 1
    data_for_df = {col: [] for col in COLUMNS}
    file_names = os.listdir(path=PATH)
    # TODO - Убрать следующую строку
    #file_names = [file_names[0]]
    for name in file_names:
        with codecs.open(PATH + name, "r", "utf-8") as html:
            text = BeautifulSoup(html, features="html.parser").get_text()
            patient_data = text_parser(text, id)
            add_patient(data_for_df, patient_data)
            id += 1
        logging.info('Документ ' + str(name) + ' обработан')

    df = pd.DataFrame(data=data_for_df)
    df.replace({True: '+', False: '-'}, inplace=True)

    df.to_excel("output.xlsx", index=False)
    logging.info('Конец скрипта')


'''
re.findall(r'\bB\w+', text, flags=re.IGNORECASE)  
r"[А-Я][а-я]+\s[А-Я][а-я]+\s[А-Я][а-я]+"
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    df.to_excel("output.xlsx")
'''



if __name__ == "__main__":
    main()


'''
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
'''
