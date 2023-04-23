#todo: Реализовать игровую механику морского боя.
# 1. Система в случайном порядке расставляет 10 однопалубных кораблей в игровом поле 10x10
# 2. Между караблями при расстановке должно соблюдаться правило пустых полей.
# 3. Игра заканчивается при 20 промахах.

from argparse import ArgumentParser
from random import randint
import json

# TODO
FIELD_SIZE = 10

game_field = [
    ['_'] * FIELD_SIZE for i in range(FIELD_SIZE)
]

def safe_game(game_field: list, attempts: int) -> None:
    safe = {
        "game_field": game_field,
        "attempts": attempts
    }

    try:
        file_name = input("Введите имя файла сохранения ")
        print(file_name)
        with open(file_name, "w") as file:
            json.dump(safe, file)

        print(f"Текущая игра сохранена в файл {file_name}")
    except Exception:
        print("Не удалось сохранить игру")

def generate(path: str | None) -> tuple:

    if path is None:
        return generate_random(), 0

    try:
        with open(path, "r") as file:
            obj_json = json.load(file)
    except Exception:
        return generate_random(), 0
        
    return obj_json["game_field"], obj_json["attempts"]

def generate_random() -> list:
    new_game_field = game_field[:]

    ships = []

    # Сгенерируем FIELD_SIZE кораблей
    for _ in range(FIELD_SIZE):

        # Пока не подберем подходящую координату необходимо генерировать координаты
        is_correct_place = False
        while not is_correct_place:
            x = randint(0, FIELD_SIZE - 1)
            y = randint(0, FIELD_SIZE - 1)

            # Если не было ни одного корабля то его точно можно расположить
            if len(ships) == 0:
                break

            # Если рандом выдал уже помещенный корабль
            if new_game_field[x][y] == '*':
                continue

            is_correct_place = all(map(lambda e: abs(e[0] - x) > 1 or abs(e[1] - y) > 1, ships))

        new_game_field[x][y] = '*'
        ships.append((x, y))

    return new_game_field

def process_move(field: list, x: int, y: int) -> bool:
    return field[x][y] == '*'

def is_correct_move(x: int, y: int) -> bool:
    return 0 <= x < FIELD_SIZE and 0 <= y < FIELD_SIZE

def print_field(field: list) -> None:
    for x in field:
        print(''.join(x))

version = "0.0.1"
parser = ArgumentParser(prog="battleship")
parser.add_argument("-v", "--version", action="version", version=version)
parser.add_argument("--safe", help="Принимает файл сохранения")




if __name__ == "__main__":
    args = parser.parse_args()
    current_game, attempts = generate(args.safe)

    print_field(current_game)

    defeated_counter = 0

    try:
        while defeated_counter < 10 and attempts < 20:
            x, y = (-1, -1)

            while not is_correct_move(x, y):
                x = int(input("Введите координату по горизонтали "))
                y = int(input("Введите координату по вертикали "))

            print(f"Ваш текущий ход ({x}, {y})")

            if process_move(current_game, x, y):
                current_game[x][y] = 'X'
                defeated_counter += 1
                print("Вы попали")
            else:
                attempts += 1
                print("Вы промахнулись")
            
            print_field(current_game)
    except KeyboardInterrupt:
        print("\nПопытка сохранения игры")
        safe_game(current_game, attempts)
        exit(0)

    if defeated_counter == 10:
        print("Поздравляем")
    else:
        print("Ничего страшного")