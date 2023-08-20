-- Query Table for Maximum state
-- group by state
-- order by state
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
