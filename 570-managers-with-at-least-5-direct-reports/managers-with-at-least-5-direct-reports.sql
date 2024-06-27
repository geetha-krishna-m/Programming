# Write your MySQL query statement below
select e.name
from employee e
where e.id in 
(select a.managerId 
from employee a
group by a.managerId
having count(a.managerId)>=5);