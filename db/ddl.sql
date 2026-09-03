-- clause and Object 
-- Clause ->  is part of Sql statement used to Perform some specific Part.
-- Object -> is a database Structure (table, view, index, function, Trigger)
DDL
CREATE  database,table 
Alter 
Drop
Truncate 

CREATE TABLE sample (
    id INT,
    name VARCHAR(50),
    age INT
);

-- ALTER TABLE – Important Operations

-- 1. Add a new column

ALTER TABLE sample
ADD COLUMN email VARCHAR(100);
-- 2. Drop a column
ALTER TABLE sample
DROP COLUMN email;
-- 3. Rename a column
ALTER TABLE sample
RENAME COLUMN name TO student_name;
-- 4. Change column datatype
ALTER TABLE sample
ALTER COLUMN age TYPE VARCHAR(3);


-- 5. Set a default value
ALTER TABLE sample
ALTER COLUMN age SET DEFAULT 18;
-- 6. Remove a default value
ALTER TABLE sample
ALTER COLUMN age DROP DEFAULT;
-- 7. Add a constraint
ALTER TABLE sample
ADD CONSTRAINT students_pk PRIMARY KEY (id);
-- 8. Drop a constraint
ALTER TABLE sample
DROP CONSTRAINT students_pk;
-- 9. Set NOT NULL
ALTER TABLE sample
ALTER COLUMN student_name SET NOT NULL;
-- 10. Remove NOT NULL
ALTER TABLE sample
ALTER COLUMN student_name DROP NOT NULL;
-- 11. Rename a table
ALTER TABLE sample
RENAME TO sample_details;
drop table sample_details



--------------------
Constraint	Simple meaning
PRIMARY KEY -	 unique identification for each row
FOREIGN KEY	-  maintain relationship  between Two tables
NOT NULL -  Value compulsory
UNIQUE	- Duplicate values 
CHECK	- satisfy Condition  
DEFAULT	- default value 
---------------------------




CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    city VARCHAR(50) DEFAULT 'Chennai'
);

---------------------------------
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE students_samp (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
	course_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id),
);




