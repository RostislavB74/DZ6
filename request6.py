import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('hw6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.fullname  as 'Студент', g.name as 'Група'
FROM [groups] g
JOIN students s ON s.group_id  = g.id  
WHERE g.id  = 3
ORDER BY s.fullname;

"""

print(execute_query(sql))
