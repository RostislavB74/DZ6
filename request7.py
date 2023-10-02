import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('hw6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
--Знайти оцінки студентів у окремій групі з певного предмета.
SELECT gr.name as 'Група', s.fullname  as 'Студент', i.name as 'Предмет', g.grade as 'Оцінка', g.date_of 'Дата'
FROM grades g , [groups] gr, items i 
JOIN students s ON s.id  = g.items_id  -- ON i.id = g.items_id
WHERE gr.id  = 3 AND i.id=1 --AND s.id = 2
ORDER BY s.fullname ;

"""

print(execute_query(sql))
