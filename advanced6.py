# todo: Magic methods.Task
# Description Implement
# class Currency and inherited classes Euro, Dollar, Pound.Course is 1 EUR == 2 USD == 100 GBP
#
# You need to implement the following methods:
# course - classmethod which  returns string in the following pattern:
# {float value} {currency to} for 1 {currency for}
#
#     >>> print(
#         f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
#         f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
#         f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
#     )
#     Euro.course(Pound) == > 100.0  GBP for 1 EUR
#     Dollar.course(Pound) == > 50.0  GBP for 1 USD
#     Pound.course(Euro) == > 0.01  EUR for 1 GBP
#     to_currency - method transforms currency from one currency to another.Method should return instance of
#     a required currency.
#
# >>> e = Euro(100)
# >>> r = Pound(100)
# >>> d = Dollar(200)
#
# >>> print(
#     f"e = {e}\n"
#     f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
#     f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
#     f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
# )
# e = 100 EUR
# e.to_currency(Dollar) = 200.0 USD  # Dollar instance printed
# e.to_currency(Pound) = 10000.0 GBP  # Pound instance printed
# e.to_currency(Euro) = 100.0 EUR  # Euro instance printed
#
# >> > print(
#     f"r = {r}\n"
#     f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
#     f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
#     f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
# )
# r = 100 GBP
# r.to_currency(Dollar) = 2.0 USD  # Dollar instance printed
# r.to_currency(Euro) = 1.0 EUR  # Euro instance printed
# r.to_currency(Pound) = 100.0 GBP  # Pound instance printed
# + - returns an instance of a new value
#
# >>> e = Euro(100)
# >>> r = Pound(100)
# >>> d = Dollar(200)
# >>> print(
#     f"e + r  =>  {e + r}\n"
#     f"r + d  =>  {r + d}\n"
#     f"d + e  =>  {d + e}\n"
# )
# e + r = > 101.0 EUR  # Euro instance printed
# r + d = > 10100.0 GBP  # Pound instance printed
# d + e = > 400.0 USD  # Dollar instance printed
# other comparison methods: > < ==
#
# Please pay attention on examples.Your code should work exactly the same.
#
# Шаблон:
from __future__ import annotations
from typing import Type

class Currency:
    """
    1 EUR = 2 USD = 100 GBP
    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    value: float

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        raise NotImplementedError

    def to_currency(self, other_cls: Type[Currency]):
        raise NotImplementedError


class Euro(Currency):

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        if other_cls is Dollar:
            return "2 USD for 1 EUR"
        elif other_cls is Pound:
            return "100.0 GBP for 1 EUR"
        else:
            raise NotImplementedError
        
    def to_currency(self, other_cls: Type[Currency]):
        if other_cls is Dollar:
            coeff = 2
        elif other_cls is Pound:
            coeff = 100
        elif other_cls is Euro:
            coeff = 1
        else:
            raise NotImplementedError
        
        return other_cls(self.value * coeff)
    
    def __str__(self):
        return f"{self.value} EUR"
    
    def __add__(self, other_currency):
        self.value += other_currency.to_currency(Euro).value
        return self
    
    def __lt__(self, other_currency):
        return self.value < other_currency.to_currency(Euro).value
    
    def __eq__(self, other_currency):
        return self.value == other_currency.to_currency(Euro).value
    
    def __gt__(self, other_currency):
        return self.value > other_currency.to_currency(Euro).value


class Dollar(Currency):

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        if other_cls is Euro:
            return "0.5 EUR for 1 USD"
        elif other_cls is Pound:
            return "50 GBP for 1 USD"
        else:
            raise NotImplementedError
        
    def to_currency(self, other_cls: Type[Currency]):
        if other_cls is Euro:
            coeff = 0.5
        elif other_cls is Pound:
            coeff = 50
        elif other_cls is Dollar:
            coeff = 1
        else:
            raise NotImplementedError
        
        return other_cls(self.value * coeff)
    
    def __str__(self):
        return f"{self.value} USD"
        
    def __add__(self, other_currency):
        self.value += other_currency.to_currency(Dollar).value
        return self
    
    def __lt__(self, other_currency):
        return self.value < other_currency.to_currency(Dollar).value
    
    def __eq__(self, other_currency):
        return self.value == other_currency.to_currency(Dollar).value
    
    def __gt__(self, other_currency):
        return self.value > other_currency.to_currency(Dollar).value


class Pound(Currency):

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        if other_cls is Euro:
            return "0.02 EUR for 1 GBP"
        elif other_cls is Dollar:
            return "0.01 USD for 1 GBP"
        else:
            raise NotImplementedError
        
    def to_currency(self, other_cls: Type[Currency]):
        
        if other_cls is Euro:
            coeff = 0.01
        elif other_cls is Dollar:
            coeff = 0.02
        elif other_cls is Pound:
            coeff = 1
        else:
            raise NotImplementedError
        
        return other_cls(self.value * coeff)
    
    def __str__(self):
        return f"{self.value} GBP"
    
        
    def __add__(self, other_currency):
        self.value += other_currency.to_currency(Pound).value
        return self
    
    def __lt__(self, other_currency):
        return self.value < other_currency.to_currency(Pound).value
    
    def __eq__(self, other_currency):
        return self.value == other_currency.to_currency(Dollar).value
    
    def __gt__(self, other_currency):
        return self.value > other_currency.to_currency(Dollar).value


if __name__ == "__main__":

    print(
        f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
        f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
        f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
    )

    e = Euro(100)
    r = Pound(100)
    d = Dollar(200)

    print(
        f"e = {e}\n"
        f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
        f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
        f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
    )

    print(
        f"r = {r}\n"
        f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
        f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
        f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
    )

    print(
        f"e + r  =>  {e + r}\n"
        f"r + d  =>  {r + d}\n"
        f"d + e  =>  {d + e}\n"
    )