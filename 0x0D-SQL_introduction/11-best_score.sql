-- prints all records of the table second_table of the database in MySQL server.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;