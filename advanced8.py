#todo:
# Организовать подключение к DB Postgres на базе паттерна Singleton
# Использовать библиотеку https://www.psycopg.org/psycopg3/docs/basic/index.html
# Пароли спросить у админа.

import psycopg

class DBSingleton(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(DBSingleton, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, name: str, user: str, password: str):
        self.name = name
        self.user = user
        self.password = password

        print(name, user, password)

    def connect(self):
        self.__db_connection = psycopg.connect(f"dbname={self.name} user={self.user} password={self.password}")
        return self.__db_connection

    def close_connection(self):
        if not hasattr(self, '__db_connection'):
            return False
        
        self.__db_connection.close()
        return self.__db_connection.closed

    def __enter__(self):
       self.connect()
       return self

    def __exit__(self, exc_type, exc_value, traceback):
       return self.close_connection()


if __name__ == "__main__":

    # _db = DBSingleton("pythondb", "newuser", "password")
    # print(_db)
    # _db2 = DBSingleton("pythondb", "newuser", "password")
    # print(_db2)

    # _db.connect()
    # _db.close_connection()

    with DBSingleton("pythondb", "newuser", "password") as db:
        pass