-- Query to list all records without a null name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
