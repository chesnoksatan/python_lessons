# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.


def sumn(n: int) -> int:
    if n == 0:
        return 0
    
    x = n + sumn(n-1)
    print(x)
    return x


if __name__ == "__main__":
    sumn(10)