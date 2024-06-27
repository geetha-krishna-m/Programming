SELECT e1.name
FROM employee e1
LEFT JOIN employee e2 ON e1.id=e2.managerId
GROUP BY e1.id
HAVING COUNT(e1.id) >= 5;