# todo: Ввод: 2 слова, разделенных пробелами. Для ввода используем функцию s = input().split()
#  Определить, являются ли эти слова анаграммами (словами с одинаковым набором букв). Если да, то True. Если нет, то False.
#  (Примеры: АКВАРЕЛИСТ-КАВАЛЕРИСТ, АНТИМОНИЯ-АНТИНОМИЯ, АНАКОНДА-КАНОНАДА, ВЕРНОСТЬ-РЕВНОСТЬ, ВЛАДЕНИЕ-ДАВЛЕНИЕ, ЛЕПЕСТОК-ТЕЛЕСКОП)

def is_annagramm(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False
    
    for ch in first:
        if first.count(ch) != second.count(ch):
            return False
        
    return True


if __name__ == "__main__":
    string = input("Введите через пробел 2 слова ").split()
    print(is_annagramm(string[0], string[1]))