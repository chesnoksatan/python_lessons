#todo:
# Определите класс Person. При создании объекта p=Person(‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ

class Person:
    name: str
    surname: str
    middle_name: str

    def __init__(self, surname: str, name: str, middle_name: str) -> None:
        self.surname = surname
        self.name = name
        self.middle_name = middle_name

    def __str__(self) -> str:
        return (self.surname + self.name + self.middle_name)[::-1]
    

if __name__ == "__main__":
    print(Person('Иванов', 'Михаил', 'Федорович'))