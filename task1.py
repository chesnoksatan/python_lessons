def sum(x: int, y: int) -> int:
    return x + y

def dif(x: int, y: int) -> int:
    return x - y

def mul(x: int, y: int) -> int: 
    return x * y

def div(x: int, y: int) -> float:
    return x / y

def int_div(x: int, y: int) -> int:
    return x // y

def rem_div(x: int, y: int) -> float:
    return x % y

def pow(x: int, y: int) -> int:
    return x ** y


if __name__ == "__main__":
    x = int(input("Введите первое число "))
    y = int(input("Введите второе число "))

    print(sum(x, y))
    print(dif(x, y))
    print(mul(x, y))
    print(div(x, y))
    print(int_div(x, y))
    print(rem_div(x, y))
    print(pow(x, y))