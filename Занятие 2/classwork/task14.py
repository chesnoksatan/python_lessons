#todo: Введите список lst, состоящий из чисел. Найдите и напечатайте наименьшее число из списка lst.
# B Python есть функция min, которая решает эту задачу. Но напишите свою функцию, которая не использует функцию min.
import math

def get_min(array: list[int]) -> int:
    if len(array) == 0: return -math.inf

    min = array[0]
    for x in array:
        min = (x if x < min else min)
    return min
             

if __name__ == "__main__":
    lst = list(map(int, input().split()))

    print(get_min(lst))