The file present in python language as full stack python contains a description of the previous SQLAlchemy concept, however, there have been some modifications in the new version 2.0.
this note will cover the concept of this new version although it will be a crash concept as detail definition and track down has been covered in the previous space provided in the above mentions file directory.
Let begin 

## Database connection establishment
To begin we need to create an establishment to the database we wish to use, 
```python
from sqlalchemy import create_engine, text  
  
url = "mysql+mysqldb://root:admin8634@localhost/new_sql"  
  
engine = create_engine(url, echo=True)  
  
"""  
creating this connection, we are going to use the with statement,  
the with statement basically closes the database after execution  
and possible commit have be completed, rather than using .close, the  
the with takes care of that  
"""  
  
with engine.connect() as connect:  
"""  
with the above, we create our connection using the as connect, hence  
we will be using the connect to communicate with the database, now,  
lets create a means to test our connection by using an sql language.  
This will need us to import the text module which serves as a tool to  
converting our python string literals into an executeable sql command  
"""  
db = connect.execute(text("select 'hello'"))  
print(db.all())

#the all provided there is used to print what was passed to the database, however if the all was not provided, it will rather print the memory at where the value was found. however, the above is not yet populated to the database not untill its commited, the above was just done to test our connection. 
```
In this second part, we are going to look into how to create modules with python through sqlalchemy
In the new version of sqlalchemy, there has been some modifications to what has been previously discussed. The declarative_base is now featured as a class which will be inherited to other attributes within our class definition, the below code give more clarity to this concepts and codes to justify it
dont forget to create a file =======

## Base Class creation 
before anything else, its best to create a Base class of which other attributes we will create will inherit.
```python 
from sqlalchemy.orm import declarative_base  
  
Base = declarative_base()  
"""  
this is older method of using declarative_base, class  
"""
```
### Newer version 
```python
from sqlalchemy.orm import DeclarativeBase  
  
class Base(DeclarativeBase):  
pass  
  
"""  
This is the newer version of creating this concept, the class definition  
in this sense allow us to inherit all the properties of the import  
"""
```

### Now lets create our data_base model
```python
from sqlalchemy.orm import DeclarativeBase  
  
class Base(DeclarativeBase):  
pass  
  
"""  
We are now going to create our models, in this aspect, we will be using  
User and Comment as our models  
"""  
class User(Base):  
pass  
  
class Comments(Base):  
pass
```

### Using the new model in the new sqlalchemy
```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  
  
class Base(DeclarativeBase):  
pass  
  
"""  
We are now going to create our models, in this aspect, we will be using  
User and Comment as our models  
"""  
class User(Base):  
__tablename__ = 'users'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) #the mapped_column is used to add extra attributes  
username: Mapped[str] = mapped_column(nullable=False)  
email_address: Mapped[str]  
"""  
In the new sqlalchemy, the means of associating data_types to a variable  
has been changed and configured unto mapping, in the new concept, every  
model attribute is mapped unto a python data_type declaration.  
  
To do this, we will import the mapped function to be able to use this  
feature as seen in this part  
"""  
class Comments(Base):  
__tablename__ = 'comments'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
```

## Foreign key
After the above creation of two or more tables, theres need to create a connection between the two table, here is the application of foreign key
```python 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  
from sqlalchemy import ForeignKey  
  
class Base(DeclarativeBase):  
pass  
  
  
class User(Base):  
__tablename__ = 'users'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) #the mapped_column is used to add extra attributes  
username: Mapped[str] = mapped_column(nullable=False)  
email_address: Mapped[str]  
  
class Comments(Base):  
__tablename__ = 'comments'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  
user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))  
"""  
In this section, we will need to create a relationship between the two  
table by using a foreign key that will create a connection between the  
users table and that of the comments  
By this, we will need to import a foreign key  
"""
```
further
```python 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  
from sqlalchemy import ForeignKey, Text  
  
class Base(DeclarativeBase):  
pass  
  
  
class User(Base):  
__tablename__ = 'users'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) #the mapped_column is used to add extra attributes  
username: Mapped[str] = mapped_column(nullable=False)  
email_address: Mapped[str]  
  
class Comments(Base):  
__tablename__ = 'comments'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  
user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)  
text: Mapped[str] = mapped_column(Text, nullable=False)  
"""  
The text field collect the comment passed by the user, meanwhile the Text  
within the mapped_column is a data type that provides a huge memory that  
will support large comment passed by users, it wont be wrong if that is not  
passed, depending on what you wish to achieve  
"""
```

## Relationship
At this point, we will need to create a relationship between the two tables such that we could have a mutable view. this will allow us to know comments associated by a user and as well as knowing the user that posted anything. I called it associative relationship
Note that the foreign key relationship is known as the one to many relationship but in this case we need to have an individual relationship

By creating this, we will be able to access a comment made by a specific user through user_object.name_comment. Lets see how this works

```python
#creating field for the relationship, note the relationship is yet to be created
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column  
from sqlalchemy import ForeignKey, Text  
from typing import List  
  
class Base(DeclarativeBase):  
pass  
  
  
class User(Base):  
__tablename__ = 'users'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) #the mapped_column is used to add extra attributes  
username: Mapped[str] = mapped_column(nullable=False)  
email_address: Mapped[str]  
"""  
Note that, filtering a comment made by user could and may not be one  
comment, hence we need to populate this in a list, we thereby need  
to Map the comment of our user into a list.  
To do this, we need to import the list object from the typing module  
"""  
comments: Mapped[list["Comment"]]  
'''  
The above line 20 implies that the list will be mapped with all comment  
provided by a certain user, however, lets explore the difference between  
using list and using the imported List  

Note, the comment definition above is the class and not the table
'''  
  
class Comment(Base):  
__tablename__ = 'comments'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  
user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)  
text: Mapped[str] = mapped_column(Text, nullable=False)  
"""  
Creating a relationship:  
Here we will define a relationship that will enable use to access comments  
made by a user.  
First we create a field to do this  
"""
```

Associating with relationship
```python 
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column  
from sqlalchemy import ForeignKey, Text  
from typing import List  
  
class Base(DeclarativeBase):  
pass  
  
  
class User(Base):  
__tablename__ = 'users'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) #the mapped_column is used to add extra attributes  
username: Mapped[str] = mapped_column(nullable=False)  
email_address: Mapped[str]  
"""  
in here we are using the back_populates to get to the comments the is populated  
by a certain user, note that the back_populates value will be use as variable  
when declaring same field in the comment class.  
"""  
comments: Mapped[list["Comment"]] = relationship(back_populates="user")  
  
  
class Comment(Base):  
__tablename__ = 'comments'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  
user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)  
text: Mapped[str] = mapped_column(Text, nullable=False)  
"""  
In this comment part, we are going to use the user as the variable name  
while the comment used as a variable name above will now be used as a  
back_populate in this class  
In addition, since we are not getting multiple feedback, offcourse, it only  
one user that is associated to many comment, hence, we wont define the list  
python typing variable here.  
Lastly, dont forger that the mapped values are the respective Classes  
"""  
user: Mapped["User"] = relationship(back_populates="comments")
```

## String Representation
Another thing we may like to do is to define a function for a string representation for our object using the *repr* 
```python
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column  
from sqlalchemy import ForeignKey, Text  
from typing import List  
  
class Base(DeclarativeBase):  
pass  
  
  
class User(Base):  
__tablename__ = 'users'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) #the mapped_column is used to add extra attributes  
username: Mapped[str] = mapped_column(nullable=False)  
email_address: Mapped[str]  
comments: Mapped[list["Comment"]] = relationship(back_populates="user")  
  
"""  
Lets define a string representation for our user and comment  
"""  
def __repr__(self):  
return "<User is {}".format(self.username)  
  
class Comment(Base):  
__tablename__ = 'comments'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  
user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)  
text: Mapped[str] = mapped_column(Text, nullable=False)  
user: Mapped["User"] = relationship(back_populates="comments")  
  
def __repr__(self):  
return "<Comment: {} was made by {}".format(Comment.text, User.username)
```

## Creating Table in the database
Now that we have created the fundamental part of our class definition, its now time to create a table that we will push this date into in our date base
Lets create a new file to do that 
```PYTHON
from models import Base, User, Comment  
from connect import engine  
  
"""  
At this point we need to use our base class to create our database table  
Basically you need to define a metadata object and then add all the class  
created into the one single meta object and bind it to one engine for you  
to be able to crate you database table.  
  
In this case, the sqlalchemy orm does it in an interesting was by defining  
a metadata object as seen below  
"""  
  
print("CREATING TABLES >>>")  
Base.metadata.create_all(bind=engine)
```

## FILES CREATED with minor debuging
model.py
```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session  
from sqlalchemy import ForeignKey, Text, String  
  
  
class Base(DeclarativeBase):  
pass  
  
  
class User(Base):  
__tablename__ = 'users'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) #the mapped_column is used to add extra attributes  
username: Mapped[str] = mapped_column(String(255), nullable=False)  
email_address = mapped_column(String(255), nullable=False)  
comments: Mapped[list["Comment"]] = relationship(back_populates="user")  
  
"""  
Lets define a string representation for our user and comment  
"""  
def __repr__(self):  
return "<User is {}".format(self.username)  
  
class Comment(Base):  
__tablename__ = 'comments'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  
user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)  
text: Mapped[str] = mapped_column(Text, nullable=False)  
user: Mapped["User"] = relationship(back_populates="comments")  
  
def __repr__(self):  
return "<Comment: {} was made by {}".format(self.text, self.user.username)
```

connect.py
```python
from sqlalchemy import create_engine, text  
  
url = "mysql+mysqldb://root:admin8634@localhost/new_sql"  
  
engine = create_engine(url, echo=True)  

  
with engine.connect() as connect:  

```

create_table.py
```python
from models import Base, User, Comment, Session
from connect import engine  
  
print("CREATING TABLES >>>")  
Base.metadata.create_all(bind=engine)
```

## Populating database
Hence we will continue from the previous to add values to our database, we begin with creatin a new file

first we create the data we need for the database
```python
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column  
from sqlalchemy import ForeignKey, Text, String  
from typing import List  
  
class Base(DeclarativeBase):  
pass  
  
  
class User(Base):  
__tablename__ = 'users'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) #the mapped_column is used to add extra attributes  
username: Mapped[str] = mapped_column(String(255), nullable=False)  
email_address = mapped_column(String(255), nullable=False)  
comments: Mapped[list["Comment"]] = relationship(back_populates="user")  
  
"""  
Lets define a string representation for our user and comment  
"""  
def __repr__(self):  
return "<User is {}".format(self.username)  
  
class Comment(Base):  
__tablename__ = 'comments'  
id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  
user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)  
text: Mapped[str] = mapped_column(Text, nullable=False)  
user: Mapped["User"] = relationship(back_populates="comments")  
  
def __repr__(self):  
return "<Comment: {} was made by {}".format(self.text, self.user.username)
```

To put those into the database, we need 

## The Session class
The session class works just as the cursor in MySQLdb, this provides us the flexibility to work with the database
```python
from models import User, Comment, Session  
from create_table import session  
  
# this is first user with two comments  
gentle = User(  
username="Gentle",  
email_address="engen.inyang@gmail.com",  
comments=[Comment(text="Software Engineering is fun"),\  
Comment(text="with ALX, mehn is difficult")]  
)  
# this is the second user with comments also  
angel = User(  
username="Blessing",  
email_address="dgentlecute@gmail.com",  
comments=[Comment(text="Make up is my calling"),\  
Comment(text="I love to be loved but i dont love")]  
)  
# the third user has no comment  
peace = User(  
username="Peace",  
email_address="ebrewongpeace@hotmail.com"  
)  
  
# to add those valuse, you can use session.add if it was a single user  
#if its more than one, then use all, then list the users into a list  
  
session.add_all([gentle, angel, peace])  
  
#then commit the changes to the data base  
  
session.commit()
```