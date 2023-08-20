-- List all records excluding name filed
-- where name = ""
SELECT score, name FROM second_table
WHERE name <> ""
ORDER BY score DESC
