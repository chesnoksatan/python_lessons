
def to_pickle(obj, file):
    '''
    # Функция сериализует объект в байтовый поток pickle
    ## Параметры:
        obj - сериализуемый объект\n
        file - файл для сериализации к примеру "data.pkl" \n
    '''
    import pickle
    with open(file, "wb") as f:
        pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    

def to_json(obj, file):
    '''
    # Функция сериализует объект в json
    ## Параметры:
        obj - сериализуемый объект
        file - файл для сериализации к примеру "data.json"    
    '''
    import json
    with open(file, "wt") as f: 
        json.dump(obj, f, indent=4)


def to_yaml(obj, file):
    '''
    # Функция сериализует объект в yaml
    ## Параметры:
        obj - сериализуемый объект
        file - файл для сериализации к примеру "data.yaml"    
    '''
    import yaml
    with open(file, "wt") as f:
        yaml.dump(obj, f)