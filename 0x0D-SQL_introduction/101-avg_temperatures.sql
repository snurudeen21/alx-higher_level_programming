-- Query to display the average temperature (Fahrenheit) by city ordered by temperature (descending) and average value
SELECT `city`, AVG(`value`) 'avg_temp' FROM temperatures GROUP BY `city` ORDER BY `avg_temp` DESC;
