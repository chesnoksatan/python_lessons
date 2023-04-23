# Функция десериализует объект из файла типа pickle
# file - файл для десериализации к примеру "data.pkl"
def from_pickle(file):
    import pickle
    with open(file, "rb") as f:
        return pickle.load(f)

# Функция десериализует объект из файла типа json
# from_json - функция сереализует объект в json
# Параметры
# file - файл для десериализации к примеру "data.json"
def from_json(file):
    import json
    with open(file, "rt") as f:
        return json.load(f)


# Функция десериализует объект из файла типа yaml
# Параметры
# file - файл для десериализации к примеру "data.yml"
def from_yaml(file):
    import yaml
    with open(file, "wt") as f: 
        return yaml.load(f)