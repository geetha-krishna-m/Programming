select e.name
from employee e
join employee b
on e.id = b.managerId
group by b.managerId
having count(*)>=5;