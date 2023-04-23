def sum(x: int, y: int) -> int:
    return abs(x - y)


if __name__ == "__main__":
    a = int(input("Введите координату точки А "))
    b = int(input("Введите координату точки В "))
    c = int(input("Введите координату точки С "))

    ab = sum(a, b)
    bc = sum(b, c)
    abc = ab + bc

    print(ab)
    print(bc)
    print(abc)