#todo: Создать абстрактный класс Transport (транспорт) содержащий:
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.

from abc import ABC, abstractmethod


class Transport(ABC):
    speed: float
    prime_price: float
    price: float

    def __init__(self, speed: float, prime_price: float, price: float) -> None:
        super().__init__()
        self.speed = speed
        self.prime_price = prime_price
        self.price = price

    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def info(self) -> str:
        pass

class Marine(Transport):

    def __init__(self, speed: float, prime_price: float, price: float) -> None:
        super().__init__(speed, prime_price, price)

    def cost(self) -> float:
        return self.price * 1.25
    
    def info(self) -> str:
        return f"Стоимость перевозги груза на морском транспорте: {self.cost}, со скоростью: {self.speed}"
    
class Ground(Transport):

    def __init__(self, speed: float, prime_price: float, price: float) -> None:
        super().__init__(speed, prime_price, price)

    def cost(self) -> float:
        return self.price * 1.5
    
    def info(self) -> str:
        return f"Стоимость перевозги груза на наземном транспорте: {self.cost}, со скоростью: {self.speed}"