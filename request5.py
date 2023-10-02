import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('hw6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT t.fullname  as 'Викладач', i.name as 'Предмет'
FROM items i 
JOIN teachers t ON t.id  = i.teachers_id  
WHERE t.id  = 15
ORDER BY t.fullname;

"""

print(execute_query(sql))
