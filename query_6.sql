SELECT s.fullname  as 'Студент', g.name as 'Група'
FROM [groups] g
JOIN students s ON s.group_id  = g.id  
WHERE g.id  = 3
ORDER BY s.fullname  
