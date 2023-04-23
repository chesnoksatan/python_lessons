#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
# >4

#Введите  массу тела
# >1

# Ответ: 1000 кг


if __name__ == "__main__":
    x = 0

    while x <= 0 or x > 5:
        x = int(input("""Введите единицу массы тела
    1 - килограмм
    2 — миллиграмм
    3 — грамм
    4 — тонна
    5 — центнер
"""))

    weight = -1

    while weight < 0:
        weight = float(input("Введите массу тела "))

    match x:
        case 1:
            print(f"{weight} килограмм")
        case 2:
            print(f"{weight * 1e-6} килограмм")
        case 3:
            print(f"{weight * 1e-3} килограмм")
        case 4:
            print(f"{weight * 1e3} килограмм")
        case 5:
            print(f"{weight * 1e2} килограмм")