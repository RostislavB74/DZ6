SELECT i.name, s.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN items i ON i.id = g.items_id
WHERE i.id = 15
GROUP  BY s.fullname
ORDER BY average_grade DESC 
LIMIT 1;