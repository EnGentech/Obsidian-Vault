link: relational mapping: [Object-relational Mappers (ORMs) - Full Stack Python](https://www.fullstackpython.com/object-relational-mappers-orms.html)

sql documentation: [Welcome to MySQLdb’s documentation! — MySQLdb 1.2.4b4 documentation (mysqlclient.readthedocs.io)](https://mysqlclient.readthedocs.io/)

mysql introduction with python: [Introduction - Python MySQL Documentation (mikusa.com)](https://www.mikusa.com/python-mysql-docs/introduction.html)

## Installing MySQL-python on linux
```linux
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
```

## Installing sqlachemy on windows
```windows
pip install pyglet
```

getting to know MySQL: [MySQLdb User’s Guide — MySQLdb 1.2.4b4 documentation (mysqlclient.readthedocs.io)](https://mysqlclient.readthedocs.io/user_guide.html#installation)

## Setup your database by installing mysql workbench and server respectively
do that through mysql download link
to set up meet EnGentech
lunch the server using 
```sql
mysql -u root -p

```
enter password to load.
to your python, lets connect 
use the code
```python
import MySQLdb

#ensure to install the module using pip
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1")
#note that the db is optional at the moment if it was not initially crated
print(db)
```

After above, before creating table and other stuffs on database, you need to create a cursor, the cursor is what gives privilege to you to have a communication process to the database. 
Note that the above should be connected before going into this step

```python
cu = db.cursor()
```
after the above, you can now evaluate the database code in python by using the execute function as seen below
```python
cu.execute("CRAETE DATABASE my_db")
```
Having done the above, we could now check to find out the data bases present in my sql including the one we just created using the code below
```python
cu.execure("SHOW DATABASES")
for x in cu:
	print(x)
```
the above will print all the databases currently present in python 
After the above, lets say we need to crate a table, but before doing that, we need to specify which db we are to create the table into, hence declaring the last value in the first connected parameters is valid, we update the above with 
```python
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1", database="my_db")
```

Now lets create a table
```python
import MySQLdb  
  
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1", db="my_db")  
  
cur = db.cursor()  
cur.execute("create table student_profile (name varchar(255), age integer (3))"
```
to check the above then key in the code 
```python
import MySQLdb  
  
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1", db="my_db")  
  
cur = db.cursor()  
cur.execute("show tables")  
for x in cur:  
print(x)
```

you can also use the terminal to find out by typing 
```terminal
use database_name
show tables
```

## Populating the database with python
Before population the database table, it is needful to declare a formula which can be used at anytime a student needs to be populated in the storage engine as described in the code below
```python
import MySQLdb  
  
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1", db="my_db")  
  
cur = db.cursor()  
#defining a formular for your insertion into the table we created  
formula = "insert into student_profile (name, age) values (%s, %s)"  
std1 = ("Gentle", 30)  
  
#after the above, we can pass in the values defined into the execute function as seen below  
cur.execute(formula, std1)
db.commit()
#the commit is used to make changes to the table otherwise the effect wont be seen on the workbench
```

to view the above changes in workbench, open the workbench and ensure you use the db and query the data needed as seen below. note the code below is for workbench
```workbench
use my_db
select* 
from student_profile
```

Lets say we want to add many items to database at the same time then we could do the as seen below
```python 
import MySQLdb  
  
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1", db="my_db")  
  
cur = db.cursor()  
#defining a formular for your insertion into the table we created  
formula = "insert into student_profile (name, age) values (%s, %s)"  
stds = [("Blessing", 28),  
("Macauley", 35),  
("Precious", 21),  
("Imaobong", 23)]  
  
#after the above, we can pass in the values defined into the execute function as seen below  
cur.executemany(formula, stds)  
db.commit()
```
adding the below code will print all the stored data values
```python 
cur.execute("select* from student_profile")  
for x in cur:  
print(x)

#or we can use the below method  
  
profile = cur.fetchall()  
for x in profile:  
print(x)
```
we may choose to select only a given data instead of selecting the whole data, that can be done by 
```python
import MySQLdb  
  
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1", db="my_db")  
  
cur = db.cursor()  
  
cur.execute("select age from student_profile")  
#for x in cur:  
# print(x)  
#or we can use the below method  
  
profile = cur.fetchall()  
for x in profile:  
print(x)
```
we could use the fetchone command to get only the first found item in the databese, e.g
```python profile = cur.fetchone()
```

## the where method
You can search a value in the database depending on what you wish to search for, example, from the student database, we can search for on students whose age is at a particular range or exactly using your corresponding logical statement as seen below
```python
import MySQLdb  
  
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1", db="my_db")  
  
cur = db.cursor()  
#defining a formular for your insertion into the table we created  
formula = "insert into student_profile (name, age) values (%s, %s)"  
stds = [("Blessing", 28),  
("Macauley", 35),  
("Precious", 21),  
("Imaobong", 23)]  
  
#after the above, we can pass in the values defined into the execute function as seen below  
cur.executemany(formula, stds)  
cur.execute("select age from student_profile")  
#for x in cur:  
# print(x)  
#or we can use the below method  
  
profile = cur.fetchall()  
for x in profile:  
print(x)
```

## The like 
The like option enable us to search the database on a value that looks like or have a start value like something specified
the syntax is
```python
search = "select * from table_name where property_name like 'value%'"
```
the percentage serves as a wild card character implying the database to search for values with possible value assigned to it, to further explain, lets say we have the code with hi%, this means that, it should search the database for any value that precedes with hi, however if the % is before the hi like %hi, if means any value that ends with hi, but if the % if in front and the end of a value like %hi%, it means any value with hi within its boundaries. 
the below code will justify that
```python
import MySQLdb  
  
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1", db="my_db")  
cursor = db.cursor()  
  
find_uderage = "select * from student_profile where name like 'bl%'"  
#if you need to search strickly for a case sensitive value, then you use binary like the below
#find = "select * from student_profile where binary name like 'bl%'"
  
cursor.execute(find_uderage)  
for x in cursor:  
print(x)  
  
#or  
  
value = cursor.fetchall()  
for x in value:  
print(x)

```

Theres always a problem of SQL injections which is the most common hacking technic in web programming, it is best not to write your code like the above but rather use a placeholder, that way, its saver and more secure hence the code below
```python
import MySQLdb  
  
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1", db="my_db")  
cursor = db.cursor()  
  
find_uderage = "select * from student_profile where name = %s"  
  
cursor.execute(find_uderage, ("Gentle", ))  
  
value = cursor.fetchall()  
for x in value:  
print(x)
```

## Ascending and Descending order
```python
import MySQLdb  
  
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1", db="my_db")  
cursor = db.cursor()  
  
find_uderage = "select * from student_profile order by name asc"  
  
cursor.execute(find_uderage)  
  
value = cursor.fetchall()  
for x in value:  
print(x)
```

## Update and Limit
Update is used when a change is needed in the database, take for instance we need to change the age of Gentle in the student_profile to 32, in such we do the below code
```python
import MySQLdb  
  
db = MySQLdb.connect(host="localhost", user="root", passwd="admin@1", db="my_db")  
cursor = db.cursor()  
  
update = "update student_profile set age = 32 where name = 'Gentle'"  
  
cursor.execute(update)  
  
db.commit()
```
the limit function is used to limit how many result could be printed, take for instance, we try to print all students in a database, and we had like a million of them, if maybe the first 10 were needed, the limit function could be applied here
```python
command = "SELECT * from student limit 5"
```
another applied case if called OFFSET
offset is used to determine where to begin, take for instance we have student up to 100 and we wish to print student from 5 to the 50th student, we could use both limit and offset to perform this action as seen below
```python
command = "select * from student limit 45 offset 5"
```

## Deleting a value
this is used to delete a value in the database as seen below
```python
command = "Delete from student where name = 'Gentle'"
#to delete a table
command = "Drop table student"
#to avoid erro use
command = "drop table if exist student"
```

## The join command
The join command is used to relate two or more tables together whose link is based on a certain primary and foreign key e.g
there are two table created with its relation as base_id on both sides using the inner join, we could perform this 
```sql
select * from table1 inner join table2 on table1.base_id = table2.base_id
```
doing the above will generate all fields and then we could select the one we desire.

## Types of join
1. Inner join
2. left join
3. right join
4. full join

Inner Join: this returns connected and matching rows

Left Join: this returns all connected rows and non connected rows from the left table, if the right table has no match on the left table, it will return null

Right Join: this will return all rows on the right table even if there's is no match on the left table, it will thereby return null to table not match on the left hand side

Full Join: the full join return all table on the left and the right irrespective of matching, it will thereby return null on either when theres no match found

## Pictorial representation of the above using set theorem
![[Pasted image 20230617165901.png]]
lets use this code to illustrate
```python
import MySQLdb  
import sys  
  
if __name__ == '__main__':  
name = sys.argv[1]  
pas = sys.argv[2]  
dbname = sys.argv[3]  
  
mydb = MySQLdb.connect(host="localhost", port=3306, user=name, passwd=pas, db=dbname)  
mycursor = mydb.cursor()  
  
command = "select cities.id, cities.name, states.name \  
from cities inner join states on\  
cities.state_id = states.id order by cities.id asc;"  
mycursor.execute(command)  
  
for cities in mycursor:  
print(cities)  
  
mycursor.close()  
mydb.close()
```
from the above we notice that the usage of cities and states could be cumbersome, hence we could create an alias to represent them as seen below using the AS keyword
```python
import MySQLdb  
import sys  
  
if __name__ == '__main__':  
name = sys.argv[1]  
pas = sys.argv[2]  
dbname = sys.argv[3]  
  
mydb = MySQLdb.connect(host="localhost", port=3306, user=name, passwd=pas, db=dbname)  
mycursor = mydb.cursor()  
  
command = "select c.id, c.name, s.name \  
from cities AS c inner join states AS s on\  
c.state_id = s.id order by c.id asc;"  
mycursor.execute(command)  
  
for cities in mycursor:  
print(cities)  
  
mycursor.close()  
mydb.close()
```
taking a look, we notice that all cities have been represented as C and same as States with c. that awesome right?

video link to detail explanation: [(49) Learn SQL with Socratica |¦| SQL Tutorial |¦| SQL for Beginners - YouTube](https://www.youtube.com/watch?v=nWyyDHhTxYU&list=PLi01XoE8jYojRqM4qGBF1U90Ee1Ecb5tt)

## Beautiful concept in tuple utilization to join function
```python
import MySQLdb  
import sys  
  
if __name__ == '__main__':  
name = sys.argv[1]  
pas = sys.argv[2]  
dbname = sys.argv[3]  
choice = sys.argv[4]  
  
  
mydb = MySQLdb.connect(host="localhost", port=3306, user=name, passwd=pas, db=dbname)  
mycursor = mydb.cursor()  
  
command = "SELECT c.name FROM cities AS c" \  
" inner join states AS s on " \  
"c.state_id = s.id where s.name = %s ORDER BY c.id ASC;"  
mycursor.execute(command, (choice, ))  
  
cities = mycursor.fetchall()  
  
lst = []  
for city in cities:  
lst.append(city[0])  
  
print(", ".join(lst))  
  
mycursor.close()  
mydb.close()
```

