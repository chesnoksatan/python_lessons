# todo:
#  Функция get_weekday()
#  Реализуйте функцию get_weekday(), которая принимает один аргумент:
#
#  number — целое число (от 1 до 7 включительно)
#  Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:
#
#  если number не является целым числом, функция должна возбуждать исключение:
#  TypeError('Аргумент не является целым числом')
#  если number является целым числом, но не принадлежит отрезку [1;7]
#  функция должна возбуждать исключение:
#  ValueError('Аргумент не принадлежит требуемому диапазону')

#todo:
# Сделайте функцию get_weekday() статической в классе Helper

week = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье",
}

class Helper:

    @staticmethod
    def get_weekday(number: int) -> str:
        if type(number) is not int:
            raise TypeError('Аргумент не является целым числом')
        
        if number < 1 or number > 7:
            raise ValueError('Аргумент не принадлежит требуемому диапазону')
        
        return week[number]
    

if __name__ == "__main__":
    print(Helper.get_weekday(1))
    print(Helper.get_weekday(7))
    # print(Helper.get_weekday(0.0))
        