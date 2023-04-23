#todo:
# Реализовать декоратор который подсчитывает время выполнения функции.

import time


def print_execution_time(func):
    def wrapper(lst: list):
        start_time = time.time()
        ret = func(lst)
        print(f"========= {time.time() - start_time} seconds =========")

        return ret
    
    return wrapper

@print_execution_time
def list_sum(lst: list) -> int:
    return sum(lst)


if __name__ == "__main__":
    print(list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 124, 234, 345, 546, 1, 23, 23, 645]))