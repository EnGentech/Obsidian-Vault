show databases
```sql 
SHOW DATABASES;
```
create database
```sql
CREATE DATABASE db_name;
```
to list privileges on sql
```sql
show privileges
```
show permitted grants to users
```sql
show grants user_name@localhost --or sql server
```
assigning permission to created user in sql
```sql

```
to create user
```sql
create user user_name
```
to show how many user exists
```sql
select user, host from mysql.user;
```
change active database
```sql
USE db_name;
```
confirm active database
```sql
SELECT DATABASE();
```
delete database
```SQL
DROP DATABASE IF EXISTS db_name;
```
creating table
```sql
CREATE TABLE student(
id INT,
class VARCHAR(50) NOT NULL,
First_Name VARCHAR(50) NOT NULL,
email VARCHAR(30) NULL,
state CHAR(2) NOT NULL DEFAULT 'PA',
zip MEDIUMINT UNSIGNED NOT NULL,
phone VARCHAR(20) NOT NULL,
birth_date DATE NOT NULL,
sex ENUM('M', 'F'),
lunch_cost FLOAT NOT NULL,
date_created TIMESTAMP,
student_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
);
```
print a corresponding data created table
```sql
describe table_name
```
lets add data into the created table
```SQL
INSERT INTO student VALUE(
21011004,
'Lecturer',
'Gentle',
'engen.inyang@gmail.com',
'AK',
520003,
08039678842,
'1992-8-21',
'M',
500,
NOW(),
null
);
```
creating another table
```sql
CREATE TABLE class(
name varchar(30) NOT NULL,
class_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
);
```
Lets add value to the creted table
```SQL
INSERT INTO class VALUES
("Computer Engineering", null),
("Electrical Engineering", null),
("SLT", null),
("Computer Science", null),
("Mechanical Engineering", null);
```
to view table content
```sql
select * from table_name
```
lets create another table with a foreign key
```sql
CREATE TABLE test(
date DATE NOT NULL,
type ENUM('T', 'Q') NOT NULL,
class_id INT UNSIGNED NOT NULL,
test_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY)
);
-- the foreign key (class_id) is used to make reference to other table
-- a foreign key does not have to be unique
```
lets create another table
```sql
CREATE TABLE score(
student_id INT UNSIGNED NOT NULL,
event_id INT UNSIGNED NOT NULL,
score INT NOT NULL,
PRIMARY KEY(event_id, student_id)
);
```
then the last table
```SQL 
CREATE TABLE absence(
student_id INT UNSIGNED NOT NULL,
date DATE NOT NULL, 
PRIMARY KEY(student_id, date)
);
```
Adding row to existing table
```sql
ALTER TABLE table_name
ADD name data_type
-- if you want to specify position, user AFTER followed by the postion of interest
```
e.g
```sql
ALTER TABLE test 
ADD test INT NOT NULL AFTER type;
```
to alter or chage the name of an existing table header
```sql
ALTER TABLE score CHANGE event_id test_id 
INT UNSIGNED NOT NULL;
```

Listing base on need
```sql
SELECT first_name, last_name FROM student;
```
renaming tables
first list all your tables by using
```sql 
SHOW TABLE
```
then rename any of your choice with
```sql
RENAME TABLES
table_old_name to table_new_name,
table_old_name to table_new_name,
-- repeat untill your desire is done and terminate the last
```
we can select desired information base on a criteria, this is where the keyword WHERE comes in e.g, lets list student who was born not less than 1995
```sql
SELECT first_name, email, phone 
FROM students 
WHERE YEAR(birth_date) >= 1995;
```
in this aspect, conditional statement is advantegous. 
we can also search with logical statement e.g
```sql
select first_name, phone 
from students
where month(birth_date) > 1995 or state = "AK";
```
you can use OR, AND or NOT as a condition here which can be replaced with || && or ! respectively

lets add more complication
```sql
select first_name, phone 
from students 
where day(birth_date) > 10 && (state='AK' or state='NG');
```
using null to check validation
```sql
select first_name from students 
where first_name is not null;
```
selection with order
NOTE: DESC meand descenting order and ASC means ascending order
e.g
```sql
select first_name from students where first_name is not null order by first_name desc;
```
using limit limits the number of result obtained 
```sql
select first_name from students where first_name is not null order by first_name desc limit 1;
```
you can skip the first limit and get the next limit
e.g
```sql 
select first_name from students where first_name is not null order by first_name desc limit 1, 1;
-- the above will return the second value in the list rather than the first value
```
the AS and CONCAT keyword
The concat keyword is use to join two fields together and the AS is used to make a header for our print out
e.g
```sql
select concat(first_name, " from ", state) AS 'Name', CONCAT(first_name, " birth ", birth_date) AS "Birth" from students;
```
we can select base on what a field content begins with or end with 
e.g lets say we need students whose name begin with b or a student whose name ends with y
```sql
select first_name from students where first_name like "b%" or first_name like "%y";
```
we can specify the limit of characters needed while using the like, for instance we need a name with 4 characters with the end character as y
```sql
select first_name from students where first_name like '___y';
```
another example
```sql 
select first_name from students where first_name like "___tle"
-- that selects student with letter ending with tle
```
we can print with DISTINCT, this avoids duplication, lets say we need to know how many country representatives are active in our school, hence this should print only one country at a time
```sql
select distinct state from students order by state;
```
the COUNT command, 
this is use to count the number of occurence in our database or table
e.q, if we need to count the number of country associated with our school, the the distinct state will be called as an argument to the count function e.g
```sql
select count(distinct state) from students;
```
we can count the total number of students in our database by 
```sql
select count(*) from students;
```
lets count the number of boys in the class
```sql
select count(*) from students 
where sex='M';
```
lets find out how many boys are there and girls respectively
```sql
select sex, count(*)
from students 
group by sex;
```
another thing 
```sql
select month(brith_date) as "month", count(*) 
from students 
group by month
order by month;
```