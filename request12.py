import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('hw6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
--Оцінки студентів у певній групі з певного предмета на останньому занятті.
SELECT gr.name AS 'Група', s.fullname AS 'Студент',  i.name as 'Предмет', g.grade AS 'Оцінка', g.date_of AS 'Дата'
FROM grades g
JOIN students s ON s.id=g.student_id
JOIN groups gr ON gr.id =s.group_id
--JOIN students s ON s.id=g.student_id
JOIN items i ON i.id = g.items_id 
WHERE g.date_of = '2023-06-15'
GROUP BY gr.name  
ORDER BY g.date_of  ; 

"""

print(execute_query(sql))
