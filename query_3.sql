SELECT i.name, gr.name, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN items i ON i.id = g.items_id
JOIN [groups] gr ON gr.id =s.group_id 
WHERE i.id = 5
GROUP  BY gr.name, i.name
ORDER BY average_grade DESC 
