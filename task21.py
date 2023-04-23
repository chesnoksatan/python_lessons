#todo:  Напишите программу, которая получает на вход строку, и определяет,
# является ли строка панграммой (т.е. содержатся ли в ней все 33 буквы русского алфавита).
import re

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def is_pangramm(string: str) -> bool:
    return len(set(string.lower())) >= len(alphabet.lower())


if __name__ == "__main__":
    string = input("Введите строку")
    print(is_pangramm(string))