from psycopg2 import connect, Error
from contextlib import contextmanager


@contextmanager
def connection():
    conn = None
    try:
        conn = connect(host='cornelius.db.elephantsql.com', user='yrtbwazh', database='yrtbwazh',
                       password='YvvKxWT438Cag4cgCUehaptsaTjMnuOW')
        yield conn
        conn.commit()
    except Error as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
# docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
