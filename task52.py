#todo:
#  Разработать систему учета решения задач учениками курса «Разработчик на Питоне».
#
# Проблема.
# Преподаватель каждый урок задает некоторое количество задач в качестве домашнего задания, для упрощения можно считать, что одну.
# Каждый ученик решает каждую задачу. Переводит ее статус в решенную.
# Преподаватель проверяет каждую задачу каждого ученика и либо подтверждает ее статус как решенную или меняет ее статус как не решенную.
# Вопрос. Как спроектировать систему классов на Питоне для решения задачи учета?
# Разработайте систему
# классов (Teacher, Pupil, Lesson, Task. Нужен ли класс Группа?);
# атрибутов для каждого состояния каждого объекта;
# методов для каждого объекта.
# Отчетность? Запросы? Начните с формулировки решаемой задачи – спецификации или технического задания. Затем спроектируйте классы, атрибуты, методы. Протестируйте систему.

import random

class Task:
    name: str
    is_solved: bool = False

    def __init__(self, name: str, is_solved: bool = False) -> None:
        self.name = name

    @classmethod
    def copy(cls, task):
        return Task(task.name, task.is_solved)

    def __str__(self) -> str:
        return f"Task {self.name}, is solved: {self.is_solved}"

class Teacher:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def check(self, task: Task) -> bool:
        task.is_solved = random.choice([True, False])
        return task.is_solved

class Pupil:
    name: str
    tasks: list[Task]

    def __init__(self, name: str) -> None:
        self.name = name

    def solve(self):
        for task in self.tasks:
            task.is_solved = True

    def __str__(self) -> str:
        return self.name + " " + "; ".join([str(task) for task in self.tasks])

class Lesson:
    teacher: Teacher
    students: list[Pupil]

    def __init__(self, teacher: Teacher, students: list[Pupil], tasks: list[Task]) -> None:
        self.teacher = teacher
        self.students = students

        for student in self.students:
            student.tasks = [Task.copy(task) for task in tasks]

    def start_lesson(self):
        print("Начинаем занятие")
        for student in self.students:
            student.solve()

    def end_lesson(self):
        print("Заканчиваем занятие")
        for student in self.students:
            for task in student.tasks:
                self.teacher.check(task)

        print("Результаты занятия:")
        for student in self.students:
            print(student)


if __name__ == "__main__":
    teacher = Teacher("Кандидат питонических наук")
    tasks = [Task("Задание 1"), Task("Задание 2"), Task("Задание 3")]
    students = [Pupil("Удав"), Pupil("Сетчатый питон"), Pupil("Анаконда"), Pupil("Мини-конда")]

    lesson = Lesson(teacher, students, tasks)

    lesson.start_lesson()
    lesson.end_lesson()