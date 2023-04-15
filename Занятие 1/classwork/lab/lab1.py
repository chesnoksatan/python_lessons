# todo: Необходимо реализовать консольную утилиту marge.py которая реализует функцию слияния
# содержимого файлов определенного типа с указанного каталога в один файл json при задании параметров:
# ./ marge.py -v --root_dir=ROOT_FOLDER output.json

# Где:
# output.json Исходный файл
# --root_dir  Директория для обработки

# Структура каталогов выглядит следующим образом:
# ROOT_FOLDER   -->   A  ---  w.txt
#                          -  x.txt
#                     B  ---  z.txt
#                          -  y.txt

# Результат: в файле output.json
# {
#   "VectorTelemetry": {
#     "w": 74.72395045538597,
#     "x": 74.72395045538597,
#     "y": 74.72395045538597,
#     "z": 74.72395045538597
#   }
# }
# Примечание: О запуске и окончании утилиты информировать пользователя через логгер.

# Перед тем как написать утилиту нужно решить локальные подзадачи в папке simple.
# 1. Посмотреть как работает логгер
# 2. Разобраться с передачей аргументов программе через коммандную строку
# 3. Понять как работает обход папок
# Далее соединить полученные знания в утилите merge.py


from argparse import ArgumentParser
import logging
import os

def find_files(catalog: str, filename: str) -> list:
    '''
        Функция ищет все файлы с именем filename во всех подкаталогах каталога catalog
    '''
    find_files = []
    for root, _, files in os.walk(catalog):
        find_files += [os.path.join(root, name) for name in files if name == filename]

    return find_files

version = "0.0.1"
parser = ArgumentParser(prog="merge", description="Выполняет слияние содержимого файлов определенного типа с указанного каталога в один файл json", epilog="Приятного пользования!")
parser.add_argument('output', help="выходной файл")  # positional argument
parser.add_argument("-v", "--version", action="version", version=version)
parser.add_argument("--debug", action="store_true", help="enable debug mode")
parser.add_argument("--root_dir", help="Принимает папку для обработки")

logger = logging.getLogger()
logger.name = "My Merge Application"
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s %(name)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


if __name__ == "__main__":
    args = parser.parse_args()

    output = args.output
    root_dir = args.root_dir
    debug = args.debug

    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)


    logger.info("Начало выполнения скрипта")