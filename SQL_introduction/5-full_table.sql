-- script that updates the score of Bob to 10 in the table second
UPDATE second SET score = 10 WHERE name = 'Bob';

-- Get the table structure without using DESCRIBE or EXPLAIN
SELECT TABLE_NAME, CREATE_TABLE 
FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
