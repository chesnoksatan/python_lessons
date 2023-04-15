# todo:  Ввести число n. Напечатать треугольник из символов +.
#  Пример для n = 5:
# +
# ++
# +++
# ++++
# +++++


def get_line(count: int) -> str:
    return ''.join(['+' for _ in range(count)])

def get_line_2(count: int) -> str:
    return '+' * count

def get_line_3(count: int) -> str:
    return '+' * count + '\n'


if __name__ == "__main__":
    n = int(input("Введите n "))
    for i in range(1, n+1):
        print(get_line_2(i))

    # print(''.join([get_line_3(i) for i in range(1, n + 1)]))