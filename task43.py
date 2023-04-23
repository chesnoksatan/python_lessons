#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.

import calendar

def get_days(year: int) -> list:
    c = calendar.Calendar(firstweekday=calendar.SATURDAY)
    return [c.monthdatescalendar(year, month)[2][5] for month in range(1,13)]


if __name__ == "__main__":
    print(get_days(2023))

