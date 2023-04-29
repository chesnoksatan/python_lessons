# todo:
#   Создайте класс Pet с атрибутам имя, вес и уровень сытости.
#   Напишите метод info, который в качестве результата выдает эти атрибуты.
#   Напишите метод hungry, который возвращает уровень сытости и комментирует: если меньше 5, то «голоден», если больше 10, то «сыт».
#   Напишите метод feed, который передает питомцу некоторую еду, которая прибавляется к уровню сытости и вызывает метод info.

class Pet:
    name: str
    weight: int
    fullness: int

    def __init__(self, name: str, weight: int, fullness: int = 0):
        self.name = name
        self.weight = weight
        self.fullness = fullness

    def info(self):
        print(f"{self.name} весит {self.weight} с уровнем сытости {self.fullness}")
        return (self.name, self.weight, self.fullness)

    def hungry(self):
        if self.fullness < 5:
            print("голоден")
        elif self.fullness > 10:
            print("сыт")

        return self.fullness
    
    def feed(self, food: int):
        self.fullness += food
        self.info()

if __name__ == "__main__":
    pet = Pet("Кот", 5, 2)
    pet.info()
    pet.hungry()
    pet.feed(5)