#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

import random


if __name__ == "__main__":
    N = 0

    while N <= 0:
        N = int(input("Введите размер массива "))

    array = list(map(lambda _: random.randint(0, 1000), range(N)))
    print(array)

    new_array = list(map(lambda x: x + 1, array))
    print(new_array)