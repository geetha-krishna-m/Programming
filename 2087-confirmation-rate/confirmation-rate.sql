SELECT s.user_id,ROUND(count(CASE WHEN c.action = 'confirmed' THEN 1 ELSE NULL END)/count(*),2) as 'confirmation_rate'
FROM signups s
left JOIN confirmations c ON s.user_id = c.user_id   
GROUP BY s.user_id;
