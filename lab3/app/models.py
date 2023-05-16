from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped

Base = declarative_base()

'''
    Схема БД расположена здесь: https://editor.ponyorm.com/user/chesnoksatan/lms/designer
'''

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    tasks = relationship('Task', backref="category")

    def __repr__(self) -> str:
        return f'<Category "{self.name}">'
    
class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    complexity = Column(Integer, default=1)     # Сложность задания
    name = Column(String(255), nullable=False)  # Название задания
    description = Column(String(255))           # Описание задачи

    category_id = Column(Integer, ForeignKey("category.id")) # Идентификатор категории, к которой относится задание
    student_tasks = relationship('StudentTask', backref="task")
    class_tasks = relationship('ClassTask', backref="task")

class ClassTask(Base):
    __tablename__ = "class_task"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    task_id = Column(Integer, ForeignKey("task.id"))
    class_id = Column(Integer, ForeignKey("class.id"))

class StudentTask(Base):
    __tablename__ = "student_task"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    status = Column(Boolean)
    code = Column(String())

    task_id = Column(Integer, ForeignKey("task.id"))
    student_id = Column(Integer, ForeignKey("student.id"))

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    student_tasks = relationship('StudentTask', backref="student")
    student_groups = relationship('StudentGroup', backref="student")

class StudentGroup(Base):
    __tablename__ = "student_group"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    student_id = Column(Integer, ForeignKey("student.id"))
    group_id = Column(Integer, ForeignKey("group.id"))
    
class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    student_groups = relationship('StudentGroup', backref="group")
    class_groups = relationship('ClassGroup', backref="group")

class ClassGroup(Base):
    __tablename__ = "class_group"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    group_id = Column(Integer, ForeignKey("group.id"))
    class_id = Column(Integer, ForeignKey("class.id"))

class Class(Base):
    __tablename__ = "class"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    class_groups = relationship('ClassGroup', backref="class")
    class_tasks = relationship('ClassTask', backref="class")

    teacher_id = Column(Integer, ForeignKey("teacher.id"))

class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    classes = relationship('Class', backref="teacher")

    def __repr__(self) -> str:
        return f'<Category "{self.name}">'