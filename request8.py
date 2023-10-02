import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('hw6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT t.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN teachers t ON t.id = g.grade 
GROUP  BY t.fullname ;

"""

print(execute_query(sql))
