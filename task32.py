#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
# Ввод: GGCTAA
# Вывод: CCGATT

dnk_rnk = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "T"
}


def to_rnk(dnk: str) -> str:
    return ''.join(map(lambda x: dnk_rnk[x], dnk))


if __name__ == "__main__":
    print(to_rnk("GGCTAA"))