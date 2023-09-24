from psycopg2 import Error

from db_connection import connection

create_table_group = """
CREATE TABLE IF NOT EXISTS groupname (
  id SERIAL PRIMARY KEY,
  groupname VARCHAR(8)
);

"""

if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(create_table_group)
        c.close()
