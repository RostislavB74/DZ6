from psycopg2 import connect, DatabaseError
from contextlib import contextmanager


@contextmanager
def connection():
    conn = None
    try:
        conn = connect(host='localhost', user='postgres', database='postgres',
                       password='mysecretpassword')
        yield conn
        conn.commit()
    except DatabaseError as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
# docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
