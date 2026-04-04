-- lists all records of the table second_table
-- don't list rows without a name value
-- score and name, ordered by score (descending)
SELECT score, name FROM second_table 
WHERE name IS NOT NULL AND name <> '' 
ORDER BY score DESC;
