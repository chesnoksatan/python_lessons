# todo:
#  Создайте класс Triangle с методом, который при создании объекта проверяет три переменный x, y, z на то,
#  что из них можно составить треугольник. Требования: все числа должны быть больше нуля, сумма любых двух должны быть больше третьего.


class Triangle:
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        if x <= 0 or y <= 0 or z <= 0:
            raise Exception("Треугольника с заданными параметрами не существует")
        
        if x + y <= z or y + z <= x or z + x <= y:
            raise Exception("Треугольника с заданными параметрами не существует")
        
        self.x = x
        self.y = y
        self.z = z


if __name__ == "__main__":
    x = int(input("Введите x "))
    y = int(input("Введите y "))
    z = int(input("Введите z "))

    Triangle(x, y, z)