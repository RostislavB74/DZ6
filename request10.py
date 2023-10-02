import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('hw6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
--Список курсів, які певному студенту читає певний викладач.
SELECT s.fullname AS 'Студент',  i.name as 'Предмет', t.fullname as 'Викладач'
FROM grades g  
JOIN students s ON s.id=g.student_id
JOIN teachers t ON t.id=g.items_id
JOIN items i ON i.id = g.items_id 
WHERE s.id = 11 AND i.id =14
--IF WHERE i.id =1
GROUP BY i.id 


ORDER BY s.fullname  ; 

"""

print(execute_query(sql))
