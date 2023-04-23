#todo Задача 1. Транспонирование матрицы, transpose(matrix)
# Создайте списковое включение, которое генерирует следующую последовательность: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10

def generate() -> list:
    return [number for number in range(11) for _ in range(number)]


#todo Задача 2. Транспонирование матрицы, transpose(matrix)
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
# Пример:
# >>> transpose([[1, 2, 3], [4, 5, 6]])

# [[1, 4], [2, 5], [3, 6]]


# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


#todo Задача 3. Найти сумму элементов матрицы
# Написать msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.

# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)

def msum(matrix) -> int:
    return sum([sum(lst) for lst in matrix])


if __name__ == "__main__":
    print(generate())
    print(transpose([[1, 2, 3], [4, 5, 6]]))
    print(msum([[1, 2, 3], [4, 5, 6]]))