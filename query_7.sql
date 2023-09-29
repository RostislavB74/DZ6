--Знайти оцінки студентів у окремій групі з певного предмета.
SELECT gr.name as 'Група', s.fullname  as 'Студент', i.name as 'Предмет', g.grade as 'Оцінка', g.date_of 'Дата'
FROM grades g , [groups] gr, items i 
JOIN students s ON s.id  = g.items_id  -- ON i.id = g.items_id
--JOIN students s ON s.id = g.student_id
WHERE gr.id  = 3 AND i.id=1 --AND s.id = 2
ORDER BY s.fullname  
--SELECT i.name, gr.name, ROUND(AVG(g.grade), 2) AS average_grade
--FROM grades g
--JOIN students s ON s.id = g.student_id
--JOIN items i ON i.id = g.items_id
--JOIN [groups] gr ON gr.id =s.group_id 
--WHERE i.id = 5
--GROUP  BY gr.name, i.name
--ORDER BY average_grade DESC 
