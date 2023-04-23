# Написать игру "Поле чудес"

# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
words = ["оператор", "конструкция", "объект"]
desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", 
          "Объект, который может быть представлен в виде множества объектов", 
          "Сущность в цифровом пространстве, обладающая состоянием и поведением, имеющая поля и методы" ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.

# Пример вывода:

# "Это слово обозначает наименьшую автономную часть языка программирования"

# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

# Введите букву: O

# O  ▒  ▒  ▒  ▒  ▒  O  ▒


# Введите букву: Я

# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:

import random


if __name__ == "__main__":
    x = random.randint(0, len(words) - 1)

    current_word = words[x].lower()

    print(desc_[x])

    counter = 10
    isFinished = False

    current_state = list('*' * len(current_word))
    print(''.join(current_state))

    while counter > 0 and not isFinished:
        current_ch = ""

        while len(current_ch) != 1:
            current_ch = str(input("Введите букву: ")).lower()

        if current_state.count(current_state) != 0:
            counter -= 1
            print("Данную букву вы уже отгадали")
            print(f"У вас осталось {counter} попыток!")
            continue


        if current_word.count(current_ch) == 0:
            counter -= 1
            print("Нет такой буквы.")
            print(f"У вас осталось {counter} попыток!")
            continue
        else:
            for i in range(len(current_word)):
                if current_word[i] == current_ch:
                    current_state[i] = current_ch
            
            print(''.join(current_state))

        isFinished = current_state.count('*') == 0

    if isFinished:
        print("Поздравляю, вы выиграли")
    elif counter <= 0:
        print("В следующий раз повезет!")
