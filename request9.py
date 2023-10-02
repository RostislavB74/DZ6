import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('hw6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
--Знайти список курсів, які відвідує студент.
SELECT s.fullname AS 'Студент',  i.name as 'Предмет'
FROM grades g  
JOIN students s ON s.id=g.student_id
JOIN items i ON i.id = g.items_id 
WHERE s.id = 11
--WHERE i.id =1
GROUP BY i.id 


ORDER BY s.fullname ;

"""

print(execute_query(sql))
