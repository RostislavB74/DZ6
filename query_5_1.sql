SELECT t.fullname AS 'Викладач',
       i.name as 'Предмет'
FROM items i
JOIN teachers t ON t.id = i.teachers_id
ORDER BY t.fullname,
         i.name ;