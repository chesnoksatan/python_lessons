# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.

from calendar import monthrange

# Мб я не понял постановку задачи
def get_dates(year: int, month: int) -> list:
    return [i+1 for i in range(monthrange(year, month)[1])] #[i for i in monthrange(year, month)]


if __name__ == "__main__":
    print(get_dates(2023, 2))