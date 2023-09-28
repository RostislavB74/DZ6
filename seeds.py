from datetime import datetime, date, timedelta
from faker import Faker
from random import randint, choice
import sqlite3
from pprint import pprint
from tqdm import tqdm

items = [
    "Вища математика",
    "Фізичне виховання та самовдосконалення",
    "Фізика",
    "Комп'ютерні технології та програмування",
    "Ділова українська мова",
    "Фахова іноземна мова",
    "Вступ до спеціальності",
    "Екологія",
    "Електротехніка та авіоніка",
    "Теорія механізмів та машин",
    "Інженерна та комп'ютерна графіка",
    "Робочі тіла рідинно-газових систем ЛА",
    "Аналітичні та варіаційні методи",
    "Філософія",
    "Аерогідродинаміка та динаміка польоту",
    "Механіка матеріалів та конструкцій",
    "Гідравлічна і пневматична автоматика",
    "Історія України",
    "Теорія ймовірності"
]

groups = ["АКФ 101", "АКФ 201", "АКФ 301", "АКФ 401", "АКФ 501",
          "АКФ 102", "АКФ 202", "АКФ 302", "АКФ 402", "АКФ 502",
          "АКФ 103", "АКФ 203", "АКФ 303", "АКФ 403", "АКФ 503"
          ]
# teachers = ["Тарасенко Т.В.", "Богдан С.Ю.", "Агеєв С.Є.", "Орденов С.С."]
NUMBER_TEACHERS = 15
NUMBER_STUDENTS = 300
fake = Faker()
connect = sqlite3.connect("hw6.db")
cur = connect.cursor()


def seed_teachers():
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers (fullname) VALUES(?);"
    cur.executemany(sql, zip(teachers,))


def seed_items():
    sql = "INSERT INTO items(name, teachers_id) VALUES(?, ?);"
    cur.executemany(sql, zip(items, iter(randint(1, NUMBER_TEACHERS)
                    for _ in range(len(items)))))


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students (fullname, group_id) VALUES(?, ?);"
    cur.executemany(sql, zip(students, iter(randint(1, len(groups))
                    for _ in range(len(students)))))


def seed_groups():
    sql = "INSERT INTO groups (name) VALUES(?);"
    cur.executemany(sql, zip(groups,))


def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2022-12-25", "%Y-%m-%d")
    sql = "INSERT INTO grades (items_id, students_id, grade, date_of) VALUES(?, ?, ?, ?);"

    def get_list_date(start: date, end: date):
        result = []
        current_date = start
        while current_date < end:
            if current_date.isoweekday() < 6:
                result.append(current_date)
                current_date += timedelta(1)
        return result

    list_dates = get_list_date(start_date, end_date)
    grades = []
    for day in tqdm(list_dates):
        random_items = randint(1, len(items))
        random_student = [randint(1, len(NUMBER_STUDENTS)) for _ in range(5)]
        for student in tqdm(random_student):
            grades.append((random_items, student, randint(1, 12), day.date()))
    cur.executemany(sql, grades)


if __name__ == '__main__':
    try:
        seed_teachers()
        seed_items()
        seed_groups()
        seed_grades()
        seed_students()
        connect.commit()
    except sqlite3.Error as error:
        pprint(error)
    finally:
        connect.close()
