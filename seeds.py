from datetime import datetime
from faker import Faker
from random import randint, choice
import sqlite3
from pprint import pprint

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
#teachers = ["Тарасенко Т.В.", "Богдан С.Ю.", "Агеєв С.Є.", "Орденов С.С."]
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


# def seed_students():
#     teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
#     sql = "INSERT INTO students(fullname) VALUES(?);"
#     cur.executemany(sql, zip(teachers,))


if __name__ == '__main__':
    try:
        seed_teachers()
        seed_items()
    except sqlite3.Error as error:
        pprint(error)