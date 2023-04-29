# todo:
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.

class Person:
    __age: int
    __name: str

    def __init__(self, age: int, name: str):
        self.__age = age
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age: int):
        raise ValueError(f"Age for {self.__name} can not be changed")