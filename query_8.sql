SELECT t.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN teachers t ON t.id = g.grade 
GROUP  BY t.fullname
--ORDER BY average_grade DESC 
