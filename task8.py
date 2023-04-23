# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

def number_is_mirrored(number: int) -> bool:
    number_str = str(number)
    return number_str == number_str[::-1]

def validate(string: str) -> bool:
    return len(string) == 4 and string.isnumeric()


if __name__ == "__main__":

    number = ""
    while not validate(number):
        number = str(input("Введите четырехзначное число "))
        
    print(number_is_mirrored(int(number)))