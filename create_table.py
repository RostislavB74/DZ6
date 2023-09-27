from psycopg2 import Error

from db_connection import connection

create_table_group = """
CREATE TABLE IF NOT EXISTS groupstud (
  id SERIAL PRIMARY KEY,
  name VARCHAR(8)
);

"""
create_table_facultet = """
CREATE TABLE IF NOT EXISTS facultet (
  id SERIAL PRIMARY KEY,
  facultet VARCHAR(50)
);

"""
create_table_course = """
CREATE TABLE IF NOT EXISTS course (
  id SERIAL PRIMARY KEY,
  coursename VARCHAR(20)
);

"""
if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(create_table_group)
        # c.execute(create_table_facultet)
        #c.execute(create_table_course)
        c.close()
