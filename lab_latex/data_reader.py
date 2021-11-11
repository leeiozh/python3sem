import pandas as pd


def read_data(file_name):
    """
    функция читает file_name с данными в некий dataframe
    """
    if file_name[-3:] == "csv":
        return pd.read_csv(file_name)
    if file_name[-4:] == "xlsx":
        return pd.read_excel(file_name)
    if file_name[-4:] == "json":
        return pd.read_json(file_name)


def read_set(file_name):
    """
    функция читает file_name с настройками в словарь
    """
    sets = {}
    with open(file_name, 'r') as file:
        for line in file:
            tmp = line.split(" >>> ")
            if len(tmp) > 1:
                sets.setdefault(tmp[0], tmp[1][:-1])
    return sets
