video resource: quality one: [(54) SQLAlchemy ORM Crash Course - Manage Databases With Python - YouTube](https://www.youtube.com/watch?v=70mNRClYJko&list=PLEt8Tae2spYlxiF1scFTTIGG37TouiF2t)

INTRO:
An SQLAchemy is a database that allows us to communicate in ORM (Object Relational Mapper).
It is a python based Object Relational Mapper where we can communicate with or SQL Databases from python programs.
It permits read, write, update and delete operations

Here table are classes and fields within tables are attributes
![[Pasted image 20230617185818.png]]

## Steps to using SQLAchemy
1. Create engine
2. Create session 
3. Create table
4. Migrate

link: [Object Relational Tutorial — SQLAlchemy 1.3 Documentation](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)

To get started, we will need to import some basic aspects of the sqlalchemy
First we will need to import the declarative_Base which our class will inherit hence to create an instance of our attribute e.g
```python 
from sqlalchemy.ext.declarative import declarative_base   
  
Base = declarative_base()
```
we hence will create a table mapping that will be used in our database. To do this we define a class with a name instantiating it the the variable name of the declarative_base() in this case Base, in the class, we first need to title our table just like using the sql command "Create table table name" but in here, the creation is done as if it was an instance attribute as seen below
```python 
from sqlalchemy.orm import declarative_base  
from sqlalchemy import Column, String, Integer, DateTime  
from datetime import datetime  
  
Base = declarative_base()  
  
class User(Base):  
__tablename__ = 'user'  
id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)  
name = Column(String(255), nullable=False)  
nickname = Column(String(50))  
date_crated = Column(DateTime(), default=datetime.utcnow())  
  
new_user = User(name="Gentle", nickname="EnGentech")  
print(new_user)
```
in there, we have some declaration of attributes that will be seen on our database when called upon
On printing the above where a new user has been declared to possess the attribute of the class User, printing it will show the memory location at where the values are stored, now lets see how to get the real values by declaring a method to print the values. 

The method to be created will return a string representation of the object that was found in the memory, to do that we use the __repr__ 
```python
from sqlalchemy.orm import declarative_base  
from sqlalchemy import Column, String, Integer, DateTime  
from datetime import datetime  
  
Base = declarative_base()  
  
class User(Base):  
__tablename__ = 'user'  
id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)  
name = Column(String(255), nullable=False)  
nickname = Column(String(50))  
date_created = Column(DateTime(), default=datetime.utcnow())  
  
def __repr__(self):  
return ("<User name={}, nickname={}, date_created={}>".format(self.name, self.nickname, self.date_created))  
  
new_user = User(name="Gentle", nickname="EnGentech")  
print(new_user)
```
What we have done so far resides with python, what if we want to store it to a database? then we need an engine
An Engine, is simply an interface provided by sqlalchemy to link python to different sort of databases supported by the orm. to do that we create and engine. 
first we need to import a function called create_engine from the sqlalchemy
```python
from sqlalchemy import create_engine
```
after the above we need to create our url which is basically the link to the sql connection.
you can choose to hardcode the path linking to that but its not advisable instead its best to use argv to get the values rather than hardcoding as saving such vital information on the internet will render your database vulnerable but for now, we are going to use the hardcoding technic.
```python
from sqlalchemy.orm import declarative_base  
from sqlalchemy import Column, String, Integer, DateTime, create_engine  
from datetime import datetime  
  
url = "mysql+mysqldb://root:admin8634@localhost/my_db"  
Base = declarative_base()  
  
engine = create_engine(url, echo=True)  
engine.connect()  
  
class User(Base):  
__tablename__ = 'user'  
id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)  
name = Column(String(255), nullable=False)  
nickname = Column(String(50))  
date_created = Column(DateTime(), default=datetime.now())  
  
def __repr__(self):  
return ("<User name={}, nickname={}, date_created={}>".format(self.name, self.nickname, self.date_created))  
  
new_user = User(name="Gentle", nickname="EnGentech")  
print(new_user)
```
the above is the code to create a connection between your python to the database. note that the echo = True is optional, it only serve as means to get information on the database keyword usage like SELECT DATABASE() etc

Lets run a little test waooooooo00
After the above created, head onto terminal and run some code checks to see how your data base will respond to your calls, meanwhile at this point it is not needed to run the connection yet though it will have no negative effect hence the engine.connect() could be put to a pause.
on the terminal perform the following
```cmd
from main import User
#Note that the main is the python file name and
#User is the class defined 
User //this will test and run the class name
User.__tablename__ //this will print the table name
User.__table__ //this will reveal attribute and data types or the metadata of the table
```

At this point we are going to create a connection to the database and bind our metadata to it such that we could create connections, lets create a seperate file for this but you can also do same in the same main file but note that its best to do it seperately as it creates visuality 

good video resources to this: [(54) SQLAlchemy ORM Crash Course - Manage Databases With Python - YouTube](https://www.youtube.com/watch?v=70mNRClYJko&list=PLEt8Tae2spYlxiF1scFTTIGG37TouiF2t)

For us to create a database we are going to use our base class to be able to extract our date to bind it to our engine. after creating a new file, import the previous file with the class name, engine we created and the Base declaration as seen below
```python 
from main import User, engine, Base
```
In this case we are going to get a metadata of the class already created and hence create a data using the engine we created as seen below
```python 
from main import User, engine, Base  
  
Base.metadata.create_all(engine)
```
Now lets view the above in terminal. run the code either on terminal or pycharm. with the echo set to true, we would notice that a table will be created with all the parameters we passed as our metadata. this takes care of the process of create table table_name value stuff in sql command. 
Checking your database, all the filed created should be seen in there

Having created the first instance of the database, lets see how to populate our database by creating, deleting, updating and doing some stuffs on it 

To make our work look readable, lets create another file to handle creation of users
```python
#create new file here
```
To work on the datebase, the sqlalchemy has what is known as session, this allows us to make some transactions with the database using python through sqlalchemy, lets see how this works.

First we will need to import a sessionmaker from sqlalchemy orm. 
this can be done in the new file but since we are importing properties form the main, it is pertinent to import it alongside with the declarative_base
```python
from sqlalchemy.orm import declarative_base, sessionmaker


#within the body of the main create the instance of the sessionmaker
session = sessionmaker()
```

Now we are cool to communicate and transact with our database so we head to the new crated file. 
```python 
from My_python_codes.main import User, session, engine  
local_sec = session(bind=engine)  
new_user = User(name="Blessing", nickname="Angel")  
  
local_sec.add(new_user)  
local_sec.commit()
```
For you to use the session in communicating with the database, we instantiate it with a variable at which we will be calling to perform our transaction, in this sense, i use locad_sec which will be used to bind the engine unto the session created, this is done so that the values created will be added to the database, the add is used to add the values to be added to the database just like that of git add, and finally the commit is applied to commit changes to the database just like that of MySQLdb

Now lets populate our database with several names using a list of dictionary
```python
from My_python_codes.main import User, session, engine  
local_sec = session(bind=engine)  
  
users = [  
{  
"name": "Gentle",  
"nickname": "EnGentech"  
},  
{  
"name": "Macauley",  
"nickname": "Techguy"  
},  
{  
"name": "Emmanuel Iren",  
"nickname": "Emmyjay"  
},  
{  
"name": "Ekott",  
"nickname": "chaimo"  
},  
{  
"name": "Precious",  
"nickname": "biggib"  
},  
{  
"name": "Akaninyene",  
"nickname": "w_wrapper"  
},  
{  
"name": "Mfet",  
"nickname": "Itut"  
},  
{  
"name": "Inyang",  
"nickname": "obongowo"  
},  
{  
"name": "Godswill",  
"nickname": "Seneta chairmo"  
}  
]  
  
  
new_user = User(name="Blessing", nickname="Angel")  
  
local_sec.add(new_user)  
local_sec.commit()
```

having the dictionary with all the values, we need to populate the database at once and to do that we need to loop through each dictionary items, through the repr we created before, we can test to see how it will be printed before committing it the the database. lets check that out

```python
from My_python_codes.main import User, session, engine  
local_sec = session(bind=engine)  
  
users = [  
{  
"name": "Gentle",  
"nickname": "EnGentech"  
},  
{  
"name": "Macauley",  
"nickname": "Techguy"  
},  
{  
"name": "Emmanuel Iren",  
"nickname": "Emmyjay"  
},  
{  
"name": "Ekott",  
"nickname": "chaimo"  
},  
{  
"name": "Precious",  
"nickname": "biggib"  
},  
{  
"name": "Akaninyene",  
"nickname": "w_wrapper"  
},  
{  
"name": "Mfet",  
"nickname": "Itut"  
},  
{  
"name": "Inyang",  
"nickname": "obongowo"  
},  
{  
"name": "Godswill",  
"nickname": "Seneta chairmo"  
}  
]  
  
  
new_user = User(name="Blessing", nickname="Angel")  
  
#local_sec.add(new_user)  
#local_sec.commit()  
  
for x in users:  
print(User(name=x['name'], nickname=x["nickname"]))
```

Lastly, lets add everything to database
```python
from My_python_codes.main import User, session, engine  
local_sec = session(bind=engine)  
  
users = [  
{  
"name": "Gentle",  
"nickname": "EnGentech"  
},  
{  
"name": "Macauley",  
"nickname": "Techguy"  
},  
{  
"name": "Emmanuel Iren",  
"nickname": "Emmyjay"  
},  
{  
"name": "Ekott",  
"nickname": "chaimo"  
},  
{  
"name": "Precious",  
"nickname": "biggib"  
},  
{  
"name": "Akaninyene",  
"nickname": "w_wrapper"  
},  
{  
"name": "Mfet",  
"nickname": "Itut"  
},  
{  
"name": "Inyang",  
"nickname": "obongowo"  
},  
{  
"name": "Godswill",  
"nickname": "Seneta chairmo"  
}  
]  
  
  
new_user = User(name="Blessing", nickname="Angel")  
  
#local_sec.add(new_user)  
#local_sec.commit()  
  
for x in users:  
new_us = (User(name=x['name'], nickname=x["nickname"]))  
local_sec.add(new_us)  
local_sec.commit()  
print("Added {}".format(x["name"]))
#Note everything is added to the loop such that it adds at sequentially and as well printing the names of successfull added categories
```
We can confirm from the database to validate what we have done 

waooooo,,, interesting right?

Now lets see how to retrieve our files from database 
create a new file called retrieve.py lets begin 
We may like to query all users from our database. the code below illustrates that action

```python
from main import User, engine, session  
  
re_session = session(bind=engine)  
#this is used to get all user table in the database  
all_users = re_session.query(User).all()  
#this is used to loop throgh all users   
for user in all_users: 
#the .nickname is used to get only nickname, however, is user is passed, it will get the entire table from the database
print(user.nickname)
```

## Limits
if we want to limit the result obtained from database, we add 
```python
from main import User, engine, session  
  
re_session = session(bind=engine)  
  
all_users = re_session.query(User).all()[:3] 
  
for user in all_users:  
print(user.nickname)
```

To retrieve a particular object, we can use the below code
```python
from main import User, engine, session  
  
re_session = session(bind=engine)  
  
# all_users = re_session.query(User).all()  
#  
# for user in all_users:  
# print(user.nickname)  
  
gentle = re_session.query(User).filter(User.name == 'Gentle').all()  
print(gentle)
```
that works same as using select from where this is equal to that in sql.

the .all is used to get all the available type of you desire, however, you can use first() if you are expecting only one result from the database.

## Getting data from an existing database (the text module())
```python
from sqlalchemy import create_engine, text  
from sqlalchemy.orm import sessionmaker  
  
url = "mysql+mysqldb://root:admin8634@localhost/my_db"  
  
engine = create_engine(url)  
connection = engine.connect()  
  
  
query = text("SELECT * FROM user")  
get = connection.execute(query)  
  
for x in get:  
print(x)
```

## Updating database
create another file for this and repeat the same import process or values
```python
from main import engine, session, User  
  
del_session = session(bind=engine)  
  
delme = del_session.query(User).filter(User.name == "Mfet").first()  
  
del_session.delete(delme)  
del_session.commit()
#Note if you are to delete more than a single line, you have to loop through each of the values to delete as sql does not delete all items at the same time
```

## Ascending and Decending Order
by default query with order_by uses an ascending order to list values, if descending is need, then we need to import that but ascending or does not need importation, lets start with ascending order
```python
from main import User, engine, session  
  
order_session = session(bind=engine)  
  
query_asc_order = order_session.query(User).order_by(User.name).all()  
  
for order in query_asc_order:  
print(order.name, order.nickname)
```

the below is the descending order code
```python
from main import User, engine, session  
from sqlalchemy import desc  
  
order_session = session(bind=engine)  
  
query_desc_order = order_session.query(User).order_by(desc(User.name)).all()  
  
for order in query_desc_order:  
print(order.name, order.nickname)
#notice the desc imported and used within the query item

```

## The like function.
this is used to filter the database containing a certain character is applied just as the like in sql
```python 
#!/usr/bin/python3
"""This code deals with sqlalchemy
basically written to connect with our mysqldb
get all the list of states present in there
and list them in ascending order to out python snippet"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    uname = sys.argv[1]
    pas = sys.argv[2]
    db = sys.argv[3]

    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(uname, pas, db)
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    engine.connect()

    session = sessionmaker()
    local_session = session(bind=engine)

    all_state = local_session.query(State)\
        .filter(State.name.like("%a%")).order_by(State.id).all()

    for states in all_state:
        print("{}: {}".format(states.id, states.name))

# Coded by EnGentech
```

## Important (Basic connection code)
```python 
import sys  
from model_state import Base, State  
from sqlalchemy.orm import sessionmaker  
from sqlalchemy import create_engine  
  
uname = sys.argv[1]  
pas = sys.argv[2]  
db = sys.argv[3]  
  
url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\  
.format(uname, pas, db)  
  
if __name__ == "__main__":  
  
engine = create_engine(url)  
engine.connect()  
  
Base.metadata.create_all(engine)  
  
session = sessionmaker()  
city_session = session()  
  
print(city_session)

#note where base is not imported, then the declarative_base must be used properly
```

## Working with two tables (The join function)
the below code illutrates how to relate two common table together using the join keyword and filtering values best on desire
```python
import sys  
from model_state import Base, State  
from sqlalchemy.orm import sessionmaker  
from sqlalchemy import create_engine  
from model_city import City  
  
uname = sys.argv[1]  
pas = sys.argv[2]  
db = sys.argv[3]  
  
url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\  
.format(uname, pas, db)  
  
if __name__ == "__main__":  
  
engine = create_engine(url)  
engine.connect()  
  
Base.metadata.create_all(engine)  
  
session = sessionmaker(bind=engine)  
city_session = session()  
  
all_table = city_session.query(State, City).join(State)\  
.order_by(City.id).all()  
  
for x, y in all_table:  
print("{}: ({}) {}".format(x.name, y.id, y.name))
```

## Foreign keys
A foreignKey is simply an identifier of a certain table when relationship is created, take for instance, a post is made on facebook, we will need to know who made the post, hence the post class will have a foreign key that connects to the id of the user. in this sense, when a post is made, the foreignkey create the relationship to the user that make the post
```python
"""
class User:
id: int pk
name: usernamme

class Post:
id: int pk
title: str
content: str
user_id: int foreignkey
```

Lets create table from the above
```python
from sqlalchemy.orm import declarative_base  
from sqlalchemy import (  
Column,  
Integer,  
ForeignKey,  
String  
)  
  
#creating base class for inheritance  
  
Base = declarative_base()  
  
"""creating classes """  
  
class User(Base):  
__tablename__ = "users"  
id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)  
name = Column(String(255), nullable=False)  
nickname = Column(String(10), nullable=False)  
  
def __repr__(self):  
return "<User =={}== ({})".format(self.id, self.name)  
  
  
class Post(Base):  
__tablename__ = "posts"  
id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)  
title = Column(String(255), nullable=False)  
content = Column(String(255), nullable=False)  
user_id = Column(Integer, ForeignKey("users.id"))  
  
def __repr__(self):  
return "<Post =={}== ({})".format(self.id, self.title)
```
After creating the above, there is need to know which post belongs to a particular user hence the need for relation ship.

## Relationships
Relationship is a means of identifying the content between two or more tables, take for instance, in a room, there are multiple phones, we may need to know the owner of those phone, hence the relationship may be the sim present in it or in the case of biological disparity, DNA can be the relationship between a child and the father or mother, to do this, behold the code
```python 
#first we need to import the relationshiop methon in sqlalchemy
from sqlalchemy.orm import relationship
```
At this point we need to create the relationship between the two classes. to do that we need to reference the class name from the user class using backref='author' as seen below
```python
from sqlalchemy.orm import declarative_base, relationship  
from sqlalchemy import (  
create_engine,  
Column,  
Integer,  
ForeignKey,  
String,  
)  
  
#creating base class for inheritance  
url = 'mysql+mysqldb://root:admin8634@localhost/relationship'  
Base = declarative_base()  
  
engine = create_engine(url, echo=True)  
  
"""creating classes """  
  
class User(Base):  
__tablename__ = "users"  
id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)  
name = Column(String(255), nullable=False)  
nickname = Column(String(10), nullable=False)  
#we reference the class Post while creating the relationship 
#the backref is used to check the user that created a post by specifying post.user
posts = relationship('Post', backref='author')  
  
def __repr__(self):  
return "<User =={}== ({})".format(self.id, self.name)  
  
  
class Post(Base):  
__tablename__ = "posts"  
id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)  
title = Column(String(255), nullable=False)  
content = Column(String(255), nullable=False)  
user_id = Column(Integer, ForeignKey("users.id"))  
  
def __repr__(self):  
return "<Post =={}== ({})".format(self.id, self.title)  
  
Base.metadata.create_all(engine)
```

from the above code when we run it, the echo=True will create print the object created to us via the console, 
Now that we have created our database table, we are going crate our database object and see how to establish a relationship between a user as well as the post, first we need to create a session which enables us to communicate with the database
```python
from sqlalchemy.orm import sessionmaker

session = sessionmaker()(bind=engine)
```

Lets create a new file called pupoulate.py, though this can be done within the same file but to make our work look neat and readable, its best to create this differently
in it, lets have this code. 

In here we are first going to create a new user
```python
from sqlalchemy.orm import sessionmaker  
from main import User, Post, engine  
  
session = sessionmaker()(bind=engine)  
  
#lets create a user  
new_user = User(name="Gentle", nickname="EnGentech")  
  
session.add(new_user)  
session.commit()
```

Now lets create a post for the user above
```python
from sqlalchemy.orm import sessionmaker  
from main import User, Post, engine  
  
session = sessionmaker()(bind=engine)  
  
# #lets create a user  
# new_user = User(name="Gentle", nickname="EnGentech")  
#  
# session.add(new_user)  
# session.commit()  
  
multiple_post = [  
{  
"title": "Learning in progress",  
"content": "learning programing has been a huge success"  
},  
{  
"title": "Today is sunday",  
"content": "Behold its fathers day in the country"  
},  
{  
"title": "KingMaker",  
"content": "Making kings is my job"  
},  
{  
"title": "Money",  
"content": "What money cannot buy more money can buy"  
},  
{  
"title": "Friendenemy",  
"content": "One enemy, many, 100 friends too small"  
},  
]  
  
#lets add the post unto the data base  
  
for post in multiple_post:  
new_post = Post(  
title=post['title'],  
content=post['content']  
)  
session.add(new_post)  
session.commit()
```

One more thing we need to do is to link up the post populated unto a user, meanwhile remember that we have only one user at the moment so lets link the post to that very user

Note: do not run the above yet, if you do, delete all post as the values may be duplicated since we didnt use unique during creating the class attributes

```python 
from sqlalchemy.orm import sessionmaker  
from main import User, Post, engine  
  
session = sessionmaker()(bind=engine)  
  
# #lets create a user  
# new_user = User(name="Gentle", nickname="EnGentech")  
#  
# session.add(new_user)  
# session.commit()  
  
multiple_post = [  
{  
"title": "Learning in progress",  
"content": "learning programing has been a huge success"  
},  
{  
"title": "Today is sunday",  
"content": "Behold its fathers day in the country"  
},  
{  
"title": "KingMaker",  
"content": "Making kings is my job"  
},  
{  
"title": "Money",  
"content": "What money cannot buy more money can buy"  
},  
{  
"title": "Friendenemy",  
"content": "One enemy, many, 100 friends too small"  
},  
]  
  
# Query a user  
user = session.query(User).filter(User.id == 1).first()  
#lets add the post unto the data base  
  
for post in multiple_post:  
new_post = Post(  
title=post['title'],  
content=post['content'],  
author=user  
#this author is used becasue is was added as a relationship to our post class
)  
session.add(new_post)  
session.commit()  
print("{} created".format(post["title"]))
```

Now we can use our backref to create one to many relationship. now we can fetch out the post made by a user by calling the posts which was attributed to the Post class
our code now becomes
```python
from sqlalchemy.orm import sessionmaker  
from main import User, Post, engine  
  
session = sessionmaker()(bind=engine)  
  

  
# Query a user  
user = session.query(User).filter(User.id == 1).first()  
#lets add the post unto the data base  
  
  
  
print(user.posts)
```

We may also wish to know the user that made a certain post, because of the relationship created, this is possible 
```python
from sqlalchemy.orm import sessionmaker  
from main import User, Post, engine  
  
session = sessionmaker()(bind=engine)  
  

  
# Query a user  
post = session.query(Post).filter(Post.id == 1).first()  
#lets add the post unto the data base  
  
  
  
print(post.author)

```

another type of the relationship is the back_populates, the difference here is that we need to reference the relationship amongst tables 
```python 
#for the user we will have
author=relationship("User", back_populates="posts")

#and the Post class we will have
posts = relationship('Post', back_populates="author")
```

## Cascade Relationship
now that we are able to relate with the user and post, we may want to delete a certain user and all the post attribute of that user. let see how to do that 
```python 
# to do this, add cascade to the relationship level
posts = relationship('Post', back_populates='author', cascade='all, delete')
```

Lets create a new file to implement the delete function
```python
from main import User, Post  
from populate import session  
  
user_to_delete = session.query(User).filter(user.id == 1).first()  
  
posts=session.query(Post).all()  
  
session.delete(user_to_delete)  
session.commit()
#doing the above will delete post made from the user defined
```

## More on relationship
```python
from sqlalchemy.orm import declarative_base, relationship  
from sqlalchemy import (  
create_engine,  
Column,  
Integer,  
ForeignKey,  
String,  
)  
  
#creating base class for inheritance  
url = 'mysql+mysqldb://root:admin8634@localhost/relationship'  
Base = declarative_base()  
  
engine = create_engine(url, echo=True)  
  
"""creating classes """  
  
class parent(Base):  
__tablename__ = "parents"  
id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)  
name = Column(String(40), nullable=False)  
child = relationship("Child", back_populates='parent', uselist = False)  
def __repr__(self):  
return "<Parent {}>".format(self.id)  
  
class Child(Base):  
__tablename__ = "children"  
id = Column(Integer, primary_key=True)  
name = Column(String(25), nullable=False)  
parent_id = Column(Integer, ForeignKey("parents.id"))  
parent = relationship("Parent", back_populates='child')  
def __repr__(self):  
return "<Child {}>".format(self.id)
```

