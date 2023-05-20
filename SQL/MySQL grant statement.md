## Introduction to the MySQL `GRANT` statement
#### Link to the below text: [How to Use MySQL GRANT Statement To Grant Privileges to a User (mysqltutorial.org)](https://www.mysqltutorial.org/mysql-grant.aspx)

The `[CREATE USER](https://www.mysqltutorial.org/mysql-create-user.aspx)` statement creates one or more user accounts with no privileges. It means that the user accounts can log in to the MySQL Server, but cannot do anything such as [selecting a database](https://www.mysqltutorial.org/mysql-select-database/) and [querying data](https://www.mysqltutorial.org/mysql-select-statement-query-data.aspx) from tables.

To allow user accounts to work with database objects, you need to grant the user accounts privileges. And the `GRANT` statement grants a user account one or more privileges.

The following illustrates the basic syntax of the `GRANT` statement:

`GRANT privilege [,privilege],..  ON privilege_level  TO account_name;`

Code language: SQL (Structured Query Language) (sql)

In this syntax:

First, specify one or more privileges after the `GRANT` keyword. If you grant multiple privileges, you need to separate privileges by commas.

This example grants the `SELECT` privilege on the table `employees`  in the sample database to the user acount `bob@localhost`:

`GRANT SELECT ON employees TO bob@localhost;`

Code language: SQL (Structured Query Language) (sql)

The following example grants `UPDATE`, `DELETE`, and `INSERT` privileges on the table `employees` to `bob@localhost`:

`GRANT INSERT, UPDATE, DELETE ON employees  TO bob@localhost;`Code language: SQL (Structured Query Language) (sql)

Second, specify the `privilege_level` that determines the level to which the privileges apply.

MySQL supports the following main privilege levels:

![MySQL Grant - Privilege Level](https://www.mysqltutorial.org/wp-content/uploads/2019/09/MySQL-Grant-Privilege-Level.png)

**Global privileges** apply to all databases in a MySQL Server. To assign global privileges, you use the `*.*` syntax, for example:

`GRANT SELECT  ON *.*  TO bob@localhost;`
Code language: SQL (Structured Query Language) (sql)

The account user `bob@localhost` can query data from all tables in all database of the current MySQL Server.

**Database privileges** apply to all objects in a database. To assign database-level privileges, you use the ON `database_name.*` syntax, for example:

`GRANT INSERT  ON classicmodels.*  TO bob@localhost;`Code language: SQL (Structured Query Language) (sql)

In this example, `bob@localhost` can insert data into all tables in the `classicmodels` database.

**Table privileges** apply to all columns in a table. To assign table-level privileges, you use the `ON database_name.table_name` syntax, for example:

`GRANT DELETE  ON classicmodels.employees  TO bob@localhsot;`Code language: SQL (Structured Query Language) (sql)

In this example, `bob@localhost` can delete rows from the table `employees` in the database `classicmodels`.

If you skip the database name, MySQL uses the default database or issues an error if there is no default database.

**Column privileges** apply to single columns in a table.  You must specify the column or columns for each privilege, for example:

`GRANT     SELECT (employeeNumner,lastName, firstName,email),     UPDATE(lastName)  ON employees  TO bob@localhost;`
Code language: SQL (Structured Query Language) (sql)

In this example, `bob@localhost` can select data from four columns `employeeNumber`, `lastName`, `firstName`, and `email` and update only the `lastName` column in the `employees` table.

**Stored routine privileges** apply to stored procedures and stored functions, for example:

`GRANT EXECUTE  ON PROCEDURE CheckCredit  TO bob@localhost;`
Code language: SQL (Structured Query Language) (sql)

In this example, `bob@localhost` can execute the stored procedure `CheckCredit` in the current database.

**Proxy user privileges** allow one user to be a proxy for another. The proxy user gets all privileges of the proxied user. For example:

`GRANT PROXY  ON root  TO alice@localhost;`
Code language: SQL (Structured Query Language) (sql)

In this example, `alice@localhost` assumes all privileges of `root`.

Finally, specify the account name of the user that you want to grant privileges after the `TO` keyword.

Notice that in order to use the `GRANT` statement, you must have the `GRANT OPTION` privilege and the privileges that you are granting. If the `[read_only](http://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_read_only)` system variable is enabled, you need to have the [`SUPER`](http://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_super) privilege to execute the `GRANT` statement.

## MySQL `GRANT` statement examples

Typically, you use the `CREATE USER` statement to create a new user account first and then use the `GRANT` statement to grant privileges to the user.

First, create a new user called `super@localhost` by using the following `CREATE USER` statement:

`CREATE USER super@localhost  IDENTIFIED BY 'Secure1Pass!';`Code language: SQL (Structured Query Language) (sql)

Second, show the privileges assigned to `super@localhost user` by using the `SHOW GRANTS` statement.

`SHOW GRANTS FOR super@localhost;`Code language: SQL (Structured Query Language) (sql)

![MySQL Grant - No Privilege](https://www.mysqltutorial.org/wp-content/uploads/2019/09/MySQL-Grant-No-Privilege.png)

The `USAGE` means that the `super@localhost` can log in the database but has no privilege.

Third, grant all privileges in all databases in the current database server to `super@localhost`:

`GRANT ALL  ON classicmodels.*  TO super@localhost;`Code language: SQL (Structured Query Language) (sql)

Fourth, use the `SHOW GRANTS` statement again:

`SHOW GRANTS FOR super@localhost;`Code language: SQL (Structured Query Language) (sql)

![MySQL Grant example](https://www.mysqltutorial.org/wp-content/uploads/2019/09/MySQL-Grant-example.png)

## Permissible privileges for `GRANT` statement

The following table illustrates all permissible privileges that you can use for the `GRANT` and [`REVOKE`](https://www.mysqltutorial.org/mysql-revoke.aspx) statement:

**Privilege**

**Meaning**

**Level**

**Global**

**Database**

**Table**

**Column**

**Stored Routine**

**Proxy**

ALL [PRIVILEGES]

Grant all privileges at specified access level except `GRANT OPTION`

ALTER

Allow user to use of `[ALTER TABLE](https://www.mysqltutorial.org/mysql-alter-table.aspx)`statement

X

X

X

ALTER ROUTINE

Allow user to alter and drop stored procedures or stored functions.

X

X

X

CREATE

Allow user to create databases and tables

X

X

X

CREATE ROUTINE

Allow user to create stored procedures and stored functions

X

X

CREATE TABLESPACE

Allow user to create, alter or drop tablespaces and log file groups

X

CREATE TEMPORARY TABLES

Allow user to create a temporary table by using `CREATE TEMPORARY TABLE` statement

X

X

CREATE USER

Allow user to use the `CREATE USER, DROP USER, RENAME USER`, and `REVOKE ALL PRIVILEGES` statements.

X

CREATE VIEW

Allow user to create or modify the view.

X

X

X

DELETE

Allow user to use `DELETE` statement

X

X

X

DROP

Allow user to drop database, table and view

X

X

X

EVENT

Enable use of events for the Event Scheduler.

X

X

EXECUTE

Allow user to execute stored routines

X

X

X

FILE

Allow user to read any file in the database directory.

X

GRANT OPTION

Allow user to have privileges to grant or revoke privileges from other accounts.

X

X

X

X

X

INDEX

Allow user to create or drop indexes.

X

X

X

INSERT

Allow user to use the `INSERT` statement

X

X

X

X

LOCK TABLES

Allow user to use `LOCK TABLES` on tables for which you have the `SELECT` privilege

X

X

PROCESS

Allow user to see all processes with `SHOW PROCESSLIST` statement.

X

PROXY

Enable user proxying.

REFERENCES

Allow user to create a foreign key

X

X

X

X

RELOAD

Allow user to use `FLUSH` statement

X

REPLICATION CLIENT

Allow user to query to see where master or slave servers are

X

REPLICATION SLAVE

Allow the user to use replicate slaves to read binary log events from the master.

X

SELECT

Allow user to use `SELECT` statement

X

X

X

X

SHOW DATABASES

Allow user to show all databases

X

SHOW VIEW

Allow user to use `SHOW CREATE VIEW` statement

X

X

X

SHUTDOWN

Allow user to use mysqladmin shutdown command

X

SUPER

Allow user to use other administrative operations such as `CHANGE MASTER TO`, `KILL`, `PURGE BINARY LOGS`, `SET GLOBAL`, and mysqladmin command

X

TRIGGER

Allow user to use `TRIGGER` operations.

X

X

X

UPDATE

Allow user to use the `UPDATE` statement

X

X

X

X

USAGE

Equivalent to “no privileges”

In this tutorial, you have learned how to use the MySQL `GRANT` statement to grant privileges to a user.