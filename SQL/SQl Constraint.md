### Link: [MySQL constraints (zetcode.com)](https://zetcode.com/mysql/constraints/)

In this part of the MySQL tutorial, we will work with constraints.

_Constraints_ are placed on columns or tables. They limit the data that can be inserted into tables.

We have the following constraints:

-   NOT NULL
-   UNIQUE
-   PRIMARY KEY
-   FOREIGN KEY
-   ENUM
-   SET

Other databases also have the CHECK constraint, which places a condition on a valid data. MySQL parses this constraint, but it is not enforced.

### NOT NULL constraint

A column with a `NOT NULL` constraint, cannot have NULL values.

mysql> CREATE TABLE People(Id INTEGER, LastName TEXT NOT NULL,
    ->                     FirstName TEXT NOT NULL, City VARCHAR(55));
Query OK, 0 rows affected (0.07 sec)

We create two columns with `NOT NULL` constraints.

mysql> INSERT INTO People VALUES(1, 'Hanks', 'Robert', 'New York');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO People VALUES(1, NULL, 'Marianne', 'Chicago');
ERROR 1048 (23000): Column 'LastName' cannot be null

The first `SELECT` statement is executed OK, the second one fails. The SQL error says, the `LastName` column may not be null.

### UNIQUE constraint

The `UNIQUE` constraint ensures that all data are unique in a column.

mysql> CREATE TABLE Brands(Id INTEGER, BrandName VARCHAR(30) UNIQUE);
Query OK, 0 rows affected (0.08 sec)

Here we create a table `Brands`. The `BrandName` column is set to be `UNIQUE`. There cannot be two brands with the same name.

mysql> INSERT INTO Brands VALUES(1, 'Coca Cola');
Query OK, 1 row affected (0.03 sec)

mysql> INSERT INTO Brands VALUES(2, 'Pepsi');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO Brands VALUES(3, 'Pepsi');
ERROR 1062 (23000): Duplicate entry 'Pepsi' for key 'BrandName'

We get an SQL error Duplicate entry 'Pepsi' for key 'BrandName'. There can only be one Pepsi brand.

Note that a `PRIMARY KEY` constraint automatically has a `UNIQUE` constraint defined on it.

### Primary key

The `PRIMARY KEY` constraint uniquely identifies each record in a database table. It is a special case of unique keys. Primary keys cannot be `NULL`, unique keys can be. There can be more `UNIQUE` columns, but only one primary key in a table. Primary keys are important when designing the database tables. Primary keys are unique ids. We use them to refer to table rows. Primary keys become foreign keys in other tables, when creating relations among tables.

mysql> DROP TABLE Brands;
mysql> CREATE TABLE Brands(Id INTEGER PRIMARY KEY, BrandName VARCHAR(30) UNIQUE);

The Id column of the `Brands` table becomes a primary key.

mysql> DESCRIBE Brands;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| Id        | int(11)     | NO   | PRI | NULL    |       |
| BrandName | varchar(30) | YES  | UNI | NULL    |       |
+-----------+-------------+------+-----+---------+-------+

The `DESCRIBE` statement shows information about the columns in a table. We can see that the Id column has a `PRIMARY KEY` defined and the `BrandName` has `UNIQUE` constraint set. The primary key is used to uniquely identify the row in a table, when dealing with a specific table. The unique key enforces that all data in a column are not duplicate.

### Foreign key

A `FOREIGN KEY` in one table points to a `PRIMARY KEY` in another table. It is a referential constraint between two tables. The foreign key identifies a column or a set of columns in one (referencing) table that refers to a column or set of columns in another (referenced) table.

We will be demonstrating this constraint on two tables: `Authors` and `Books`.

mysql> CREATE TABLE Authors(AuthorId INTEGER PRIMARY KEY, Name VARCHAR(70))
    -> type=InnoDB;

Here we create the Authors table. In MySQL, the referencing and the referenced tables must be of InnoDB or BDB storage engines. In the MyISAM storage engines the foreign keys are parsed, but they are not enforced.

mysql> CREATE TABLE Books(BookId INTEGER PRIMARY KEY, Title VARCHAR(50),
    -> AuthorId INTEGER, FOREIGN KEY(AuthorId) REFERENCES Authors(AuthorId))
    -> type=InnoDB;

We create the `Books` table. Here we have an `AuthorId` column name, which acts as a foreign key. It references to the primary key of the `Authors` table.

What would foreign key enforcement mean in our example? We could not insert a row into the `Books` table with an `AuthorId`, which is not present in `Authors` book.

### ENUM constraint

An `ENUM` is a string object with a value chosen from a list of permitted values. They are enumerated explicitly in the column specification at table creation time.

mysql> CREATE TABLE Shops(Id INTEGER, Name VARCHAR(55), 
    -> Quality ENUM('High', 'Average', 'Low'));

We have a `Shops` table. The table has an `Id`, `Name`, and `Quality` columns defined. The `Quality` column is an `ENUM`. It permits to have one of three specified values: `High`, `Average`, or `Low`.

mysql> INSERT INTO Shops VALUES(1, 'Boneys', 'High');
mysql> INSERT INTO Shops VALUES(2, 'AC River', 'Average');
mysql> INSERT INTO Shops VALUES(3, 'AT 34', '**');
mysql> SELECT * FROM Shops;
+------+----------+---------+
| Id   | Name     | Quality |
+------+----------+---------+
|    1 | Boneys   | High    |
|    2 | AC River | Average |
|    3 | AT 34    |         |
+------+----------+---------+

In the first two statements, we have inserted two rows. In the third case, the value is not available in the `ENUM`. In this case an empty string is inserted.

### SET constraint

A `SET` can have zero or more values. Each of the values must be chosen from a list of permitted values.

mysql> CREATE TABLE Students(Id INTEGER, Name VARCHAR(55), 
    -> Certificates SET('A1', 'A2', 'B1', 'C1')); 

We have a `Students` table. In this table, we have a Certificates column. Each student can have 0, 1 or more of these certificates. This is different from the `ENUM` constraint, where you can have only one distinct value from the list of permitted values.

mysql> INSERT INTO Students VALUES(1, 'Paul', 'A1,B1');
mysql> INSERT INTO Students VALUES(2, 'Jane', 'A1,B1,A2');
mysql> INSERT INTO Students VALUES(3, 'Mark', 'A1,A2,D1,D2');
mysql> SELECT * FROM Students;
+------+------+--------------+
| Id   | Name | Certificates |
+------+------+--------------+
|    1 | Paul | A1,B1        |
|    2 | Jane | A1,A2,B1     |
|    3 | Mark | A1,A2        |
+------+------+--------------+

Paul has two certificates, Jane has three, Mark has four, but only two of them are recognised, so only the first two were written to the table. The certificates are separated by commas. No spaces are allowed.