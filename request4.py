import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('hw6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
ORDER BY average_grade;

"""

print(execute_query(sql))
