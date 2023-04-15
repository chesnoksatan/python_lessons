def solve(a: float, b: float) -> float:
    return -b / a


if __name__ == "__main__":
    a = 0

    while a == 0:
        a = float(input("Введите коэффициент А "))
    
    b = int(input("Введите коэффициент точки В "))

    print(solve(a, b))