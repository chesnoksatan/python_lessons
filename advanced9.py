#todo: Реализовать класс враппер PgDataBase над библиотекой psycopg3.
# предусмотреть методы
# __connect()
# create_database
# insert(sql, data)
# select(sql)
# delete(sql)
# update(sql, data)
# close_database()

import psycopg

class DBWrapper:
    connection: psycopg.Connection = None
    
    def __init__(self, dbname: str = "pythondb", user: str = "newuser", password: str = "password"):
        self.dbname = dbname
        self.user = user
        self.password = password

    def __connect(self):
        self.connection = psycopg.connect(f"dbname={self.dbname} user={self.user} password={self.password}")
        self.connection.autocommit = True

    def create_database(self, name: str):
        if self.connection is None or self.connection.closed:
            self.__connect()

        with self.connection.cursor() as cursor:
            cursor.execute(f"create database {name};")





    

    def insert(self, sql, data):
        if self.connection is None or self.connection.closed:
            self.__connect()

        
        with self.connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS test (
                    id serial PRIMARY KEY,
                    num integer,
                    data text)
                """)
            
            query = """
                insert into test {0} values {1}
                returning *
            """
            cursor.execute(query.format(sql, data))

    def select(self, sql):
        if self.connection is None or self.connection.closed:
            self.__connect()

    def delete(self, sql):
        if self.connection is None or self.connection.closed:
            self.__connect()

    def update(self, sql, data):
        if self.connection is None or self.connection.closed:
            self.__connect()

    def close_database(self):
        if self.connection is None or self.connection.closed:
            return
        
        self.connection.close()


if __name__ == "__main__":
    db = DBWrapper()

    db.insert(("id", "num", "data"), (1, 10, "string"))
    db.close_database()