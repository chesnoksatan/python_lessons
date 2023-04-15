# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

def get_century(year: int) -> int:
    return int(year / 100) + 1


if __name__ == "__main__":
    year = 0

    while year <= 0:
        year = int(input("Введите год "))

    print(get_century(year))