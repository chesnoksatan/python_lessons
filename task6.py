if __name__ == "__main__":
    a = int(input("Введите А "))
    b = int(input("Введите В "))
    c = int(input("Введите С "))

    a, b, c = c, a, b

    print(a)
    print(b)
    print(c)