#todo:
# Создайте функцию-генератор, которая создает последовательность числовых
# палиндромов: 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212 …


def get_palindrom(max: int = 10000000) -> list:
    return [i for i in range(max) if str(i)[::-1] == str(i)]


if __name__ == "__main__":
    print(get_palindrom(213))