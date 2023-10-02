--Список курсів, які певному студенту читають викладачі
SELECT s.fullname AS 'Студент',  i.name as 'Предмет', t.fullname as 'Викладач'
FROM grades g  
JOIN students s ON s.id=g.student_id
JOIN teachers t ON t.id=g.items_id
JOIN items i ON i.id = g.items_id 
WHERE s.id = 11 --AND i.id =14
--IF WHERE i.id =1
GROUP BY i.id 


ORDER BY s.fullname  ; 
