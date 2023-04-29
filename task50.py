#todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.

def str_decorator(func):
    def wrapper(*args):
        func(args)
        return [arg.upper() for arg in args if type(arg) is str]
    
    return wrapper

@str_decorator
def magic_function(*args):
    pass


if __name__ == "__main__":
    print(magic_function("abc", "mvc", "wtf", "nvm", 10, 20))