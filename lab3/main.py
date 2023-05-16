#todo:

#  Установить FLASK, установить SQLAlchemy
#  Настроить ORM на базу PostgresSQL
#  Для модели  БД "Система проверки задач" создать ORM модель. Сгенерировать ее в БД.
#  Переписать запросы с SQL на ORM


# https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application
# https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
# https://habr.com/ru/companies/yandex/articles/511892/

# Создать интерфейсы ввода GUI согласно бизнес логики.

from app.models import Category, Task, ClassTask, StudentTask, Student, StudentGroup, Group, ClassGroup, Class, Teacher
from app.database import Session

# session = Session()

# categoty = Category(name="Первозданная категория")
# session.add(categoty)
# session.commit()

# class CategoryController:
#     __session = Session()

#     def addCategory(self, lst):
#         self.__session.add_all(lst)
#         self.__session.commit()

# class TeacherController:
#     __session = Session()

#     def addTeacher(self, lst):
#         self.__session.add_all(lst)
#         self.__session.commit()

# if __name__ == "__main__":
#     category_controller = CategoryController()
#     teacher_controller = TeacherController()

#     category_controller.addCategory([Category(name="Первозданная категория"), Category(name="Обычная задача")])
#     teacher_controller.addTeacher([Teacher(name="Иванов Иван Иванович"), Teacher(name="Петров Петр Петрович")])