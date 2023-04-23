def is_even(a: int) -> bool:
    return a % 2 == 0


if __name__ == "__main__":
    a = int(input("Введите число А "))

    print(is_even(a))
    print(not is_even(a))