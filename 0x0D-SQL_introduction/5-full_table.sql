-- a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server
-- Set the database to hbtn_0c_0
USE hbtn_0c_0;

-- Show the full description of the table first_table
SELECT 
    COLUMN_NAME,
    ORDINAL_POSITION,
    COLUMN_DEFAULT,
    IS_NULLABLE,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH,
    NUMERIC_PRECISION,
    NUMERIC_SCALE,
    COLUMN_TYPE,
    COLUMN_KEY,
    EXTRA
FROM
    information_schema.COLUMNS
WHERE
    TABLE_NAME = 'first_table';
