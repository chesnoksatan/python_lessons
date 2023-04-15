#todo: Напишите калькулятор (простой). На вход подается строка, например:
# 1 + 2  или  5 – 3  или  3 * 4  или  10 / 2.
# Вывод: сосчитать и напечатать результат операции.
# Гарантируется, что два операнда и операция есть в каждой строчке, и все они разделены пробелами.

def sum(x: int, y: int) -> int:
    return x + y

def dif(x: int, y: int) -> int:
    return x - y

def mul(x: int, y: int) -> int: 
    return x * y

def div(x: int, y: int) -> float:
    return x / y


operations = {
    '+': sum,
    '-': dif,
    '*': mul,
    '/': div
}


if __name__ == "__main__":
    operation = input().split(' ')
    print(operations[operation[1]](int(operation[0]), int(operation[2])))