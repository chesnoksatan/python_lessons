#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

from datetime import datetime

class FuncInfo:
    name: str
    execution_times: int
    last_execution: datetime

    def __init__(self, name: str, execution_times: int, last_execution: datetime):
        self.name = name
        self.execution_times = execution_times
        self.last_execution = last_execution

    @classmethod
    def from_line(self, line: str):
        lst = line.split(',')

        name = lst[0].strip()
        execution_times = int(lst[1].strip())
        last_execution = datetime.strptime(lst[2].strip(), '%d.%m.%Y %H:%M')

        return self(name, execution_times, last_execution)

    def __str__(self):
        date_time_str = self.last_execution.strftime("%d.%m.%Y %H:%M'")
        return f"{self.name}, {self.execution_times}, {date_time_str}\n"
    
    def __eq__(self, other):
        if not isinstance(other, FuncInfo):
            return False
        
        if self.name != other.name:
            return False
        
        return True
    
    def __hash__(self):
        return self.name


def get_debug_info() -> list[FuncInfo]:
    with open("debug.log", "r") as file:
        return [ FuncInfo.from_line(line) for line in file]
    
def save_debug_info(lst: list[FuncInfo]):
    with open("debug.log", "w") as file:
        for func_info in lst:
            file.write(str(func_info)) # При записи происходит бага, к концу строки добавляется ', это куда он берется?????


def execution_times(func):
    def wrapper(*args, **kwargs):

        debug_info = get_debug_info()
        for func_info in debug_info:
            if func_info.name == func.__name__:
                func_info.last_execution = datetime.now()
                func_info.execution_times += 1
                break
        else:
            debug_info.append(FuncInfo(func.__name__, 1, datetime.now()))

        save_debug_info(debug_info)

        return func(args, kwargs)

    return wrapper


@execution_times
def summ(*args, **kwargs):
    return sum(args[0])


if __name__ == "__main__":
    # debug_info = get_debug_info()
    # for func_info in debug_info:
    #     print(func_info)
        
    print(summ(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))