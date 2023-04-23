# todo:
#  Напишите функцию, которая принимает два аргумента, lst - список чисел и x – число.
#  Функция возвращает список, содержащий квадраты чисел из lst, которые больше числа x.
#  Сделайте несколько вариантов решений:
#  1) Просто цикл с условием.
#  2) Воспользуйтесь функцией filter, для чего создайте функцию проверки числа больше x


def list_pow(lst: list, x: int) -> list:
    is_greater = lambda value: value > x

    # return [e**2 for e in lst if e**2 > x]

    return list(filter(is_greater, map(lambda value: value**2, lst)))


if __name__ == "__main__":
    x = int(input("Введите число "))
    lst = map(int, input("Введите список чисел ").split())

    print(list_pow(lst, x))