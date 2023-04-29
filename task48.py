# todo:
#  Создайте класс Shape, объекты которого имеют атрибуты
#  Colour – строка, например, «Красный», «Синий»;
#  Square – площадь объекта.
#  Создайте несколько методов:
#  1) Установить цвет объекта.
#  2) Запросить цвет объекта и напечатать его.
#  3) Задать площадь объекта.
#  4) Запросить площадь  объекта.

class Shape:
    __color: str
    __square: float

    def __init__(self, color: str = "Прозрачный", square: float = 0.0):
        self.__color = color
        self.__square = square

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def square(self):
        return self.__square
    
    @square.setter
    def square(self, square: float):
        self.__square = square