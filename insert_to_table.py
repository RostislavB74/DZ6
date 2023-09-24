from random import randint

from psycopg2 import DatabaseError
from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')
insert_group = """
    INSERT INTO groupname(groupname) VALUES(%s);
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        for _ in range(50):
            c.execute(insert_group, (fake.groupname('АКФ-101')))
        c.close()
