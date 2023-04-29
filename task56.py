# todo: Создать абстрактный класс Press (пресса) содержащий:
# Поля: название, цена за единицу.
# В классе должны быть абстрактные методы:
# метод SetPrice (без параметров) – установка цены. #### Я дико извиняюсь, но как можно установить цену не передавая новую цену в параметрах?????
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Magazine - журнал,
# Book- книга.

from abc import ABC, abstractmethod


class Press(ABC):
    name: str
    price: int

    def __init__(self, name: str, price: int) -> None:
        super().__init__()
        self.name = name
        self.price = price

    @abstractmethod
    def set_price(self, price: int) -> int:
        pass

    @abstractmethod
    def info(self) -> str:
        pass

class Magazine(Press):

    def __init__(self, name: str, price: int) -> None:
        super().__init__(name, price)

    def set_price(self, price: int) -> int:
        self.price = price
        return self.price
    
    def info(self) -> str:
        return f"Журнал {self.name} стоит {self.price} за штуку"
    
class Book(Press):

    def __init__(self, name: str, price: int) -> None:
        super().__init__(name, price)

    def set_price(self, price: int) -> int:
        self.price = price
        return self.price
    
    def info(self) -> str:
        return f"Книга {self.name} стоит {self.price} за штуку"