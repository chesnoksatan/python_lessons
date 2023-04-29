# #todo: Написать авторизацию пользователя в систему.
# При реализации авторизации спроектировать абстрактный класс и реализовать методы в наследуемом классе
# login, check_password, check_login

# При запуске программы пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
#
# При неправильном вводе логина должно генерироваться пользовательское исключение LoginNotFound
# Введеный пароль должен проверятся на длину. Длина должна быть более 8 символов иначе генерируем пользовательское
# исключение LengthError
# При вводе некорректного пароля генерируем соответсвуещее исключение
# При успешном заходе генерируем исключение "Доступ разрешен!"

from abc import ABC, abstractmethod


class LoginNotFound(Exception):
    pass

class LengthError(Exception):
    pass

class IncorrectPassword(Exception):
    pass

class AccessGranted(Exception):
    pass

class IAuthorization(ABC):
    
    @abstractmethod
    def check_login(self, login: str):
        pass

    @abstractmethod
    def check_password(self, password: str):
        pass

    @abstractmethod
    def login(self, login: str, password: str):
        pass

class BasicAuthorization(IAuthorization):
    
    def check_login(self, login: str):
        if login.lower().count("not") != 0:
            raise LoginNotFound("Пользователь не найден")
        
    def check_password(self, password: str):
        if len(password) <= 8:
            raise LengthError("Длина пароля должна быть более 8 символов")
        
        if password.lower().count("not") != 0:
            raise IncorrectPassword("Отказано в доступе. Не верный пароль")
        
    def login(self, login: str, password: str):
        self.check_login(login)
        self.check_password(password)
        raise AccessGranted("Доступ разрешен!")
    

if __name__ == "__main__":
    auth = BasicAuthorization()

    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    auth.login(login, password)