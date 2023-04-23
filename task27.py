#todo:
# Создайте лямбда функцию, которая принимает один параметр – строку.
# Переводит все буквы в нижний регистр и переворачивает их в обратном порядке. Пример входа: ‘ACbdzYx’,
# Вывод: 'xyzdbca'


if __name__ == "__main__":
    transform = lambda string: string.lower()[::-1]
    print(transform('ACbdzYx'))