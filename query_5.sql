SELECT t.fullname  as 'Викладач', i.name as 'Предмет'
FROM items i 
JOIN teachers t ON t.id  = i.teachers_id  
WHERE t.id  = 15
ORDER BY t.fullname  
