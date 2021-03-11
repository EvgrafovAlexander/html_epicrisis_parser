import pandas as pd


def create_df_dict(table_dict: dict) -> dict:
    """Создать словарь из пустых df
       на основе таблицы TABLE_DICT"""
    df_dict = {}
    for name in table_dict:
        df = pd.DataFrame({col: [] for col in table_dict[name]})
        df_dict[name] = df
    return df_dict


def add_patient(data_dfs: dict, patient_data: dict) -> dict:
    """Добавить информацию о текущем пациенте
       в общий словарь df пациентов"""
    for table_name in patient_data:
        if table_name in data_dfs:
            empty_row = {col: None for col in data_dfs[table_name].columns}
            if len(patient_data[table_name]):
                for insert_row in patient_data[table_name]:
                    row = empty_row.copy()
                    row.update(insert_row)
                    row = {key: [row[key]] for key in row}
                    df_row = pd.DataFrame(row)
                    data_dfs[table_name] = pd.concat([data_dfs[table_name], df_row])
    return data_dfs


def save_dfs(data_dfs: dict):
    """Сохранить словарь df на отдельные
       листы Excel-таблиц"""
    with pd.ExcelWriter('output.xlsx') as writer:
        for df_name in data_dfs:
            df = data_dfs[df_name]
            df = presave_prepare(df)
            df.to_excel(writer, sheet_name=df_name, startrow=0, startcol=0, index=False)


def presave_prepare(df: pd.DataFrame) -> pd.DataFrame:
    df.replace({True: '+', False: '-'}, inplace=True)
    return df
