#### Introduction (First Program)
Learning from CodeAcademy
to use tkinter, import kinter
```python
from tkinter import *
```
in every GUI program, there must be an interface which is termed as windows basically called the root. it is essential to declare this before any other codes follows in tkinter.
In tkinter, everything is a widget, frame, button, checkbox and lots of widgets
```python
root = Tk()
#this code defines a root of the windows getting set for its use
```

#### Creating a basic Hello world program
to create this all we need is a label widget. basically a tkinter widget comes in two steps of implementation. first is creating the widget and the second is placing it on the screen. 
the code below justifies thie point
```python
mylabel = Label(root, text="Hello World!")
#that is the code to create a label with mylabel as the variable name that holds the Label widget, the root is the window that was declared above, implying that the code will be written upto the root window. the text is what will be displayed as the label on the window. and now we need to place the text on the screen. Basically, there are ways to do that but the basic though not proficient is pack.   Pack is just like parking a car on any available space. Hence it does not necesitate proper definition
mylabel.pack()

```
Lastly we need to create a main loop, this process makes the program to loop continuously untill something is done either by a click or something.
its defined thus
```python
roo.mainloop()
```
Let combine all to make sense
```python
from tkinter import *

root = Tk()
mylabel = Label(root, text="Hello World!")
mylabel.pack()

root.mainloop()
```

### Positioning in Python tkinters
the pack makes the content remain in the middle irrespective of how you adjust the windows. it does not grant self positioning, another way to do this is by using the grid option. Think of grid as columns and rows arrangement
lets use the below code to explain this
```python
from tkinter import *

root = Tk()
lbl1 = Label(root, text="Hello EnGentech")
lbl2 = Label(root, text="I love your programming concept")

lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)

root.mainloop()

```
When the code is executed, the program will place the content one after the next row. 
if the column is set to one, it will take the second content into row one column one, however if you change the content to column 5 or there about, it will not skip into 5 columns as they are relative to each other, try the code.
```python
from tkinter import *

root = Tk()
lbl1 = Label(root, text="Hello EnGentech")
lbl2 = Label(root, text="I love your programming concept")

lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=5)

root.mainloop()
```
from the code above, there will be no diffrence from using one, however to see the difference, use the code below and test the outputs
```python
from tkinter import *

root = Tk()
lbl1 = Label(root, text="Hello EnGentech")
lbl2 = Label(root, text="I love your programming concept")
lbl3 = Label("              ")

lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=4)
lbl3.grid(row=1, colum=1)

root.mainloop()
```
Note: this type of positioning is relative to each other


Since python is object oriented on its own, its actually needless to write the positioning on a different line, though it makes it easy to visualize. we can actuallly graps the object and position it at the end of the label as shown below
```python
from tkinter import *

root = Tk()
lbl1 = Label(root, text="Hello EnGentech").grid(row=0, column=0)
lbl2 = Label(root, text="I love your programming concept").grid(row=1, column=0)

root.mainloop()
```
however, writing the code in two lines make your code clearner and smart, hence I recommend you writting your code as seen before the above, note that personal preference comes in here.

## Making Buttons
buttons are made to facilitate actions when clicked, it can be simply written as that of label as seen below
```python
from tkinter import *  
  
root = Tk()  
button = Button(root, text="Click me")  
button.pack()  
  
root.mainloop()
```
from the code above, a button will be enabled when executed on the screen, however when clicked, it will not perform any action as no command is linked to it, however it can be disabled with the code below
```python
from tkinter import *  
  
root = Tk()  
button = Button(root, text="Click me", state=DISABLED)  
button.pack()  
  
root.mainloop()
```

We can change the size of the button using padding, we can padx and can pady, where x stands for the x axis and same with y. 
```python
from tkinter import *  
  
root = Tk()  
button = Button(root, text="Click me", padx=50)  
button.pack()  
  
root.mainloop()
```

we can get our button to do something when clicked, this is done by defining a function and then writing some codes in the function depending of our choice of desire. 
Lets create a function to count from one to ten using for loop and then call the button to run the program when clicked.
```python
from tkinter import *  
  
root = Tk()  
  
  
def count():  
for x in range(1, 11):  
print(x)  
  
  
button = Button(root, text="Click me", padx=50, pady=10, command=count)  
button.pack()  
  
root.mainloop()
```
anothe example
```python
from tkinter import *  
  
root = Tk()  
  
  
def count():  
lbl = Label(root, text="This is a test")  
lbl.pack()  
  
  
button = Button(root, text="Click me", padx=50, pady=10, command=count)  
button.pack()  
  
root.mainloop()
```

We can design the button a bit using some attributes as seen below
fg = for font color
bg = for background color
```python
from tkinter import *  
  
root = Tk()  
  
  
def count():  
lbl = Label(root, text="This is a test")  
lbl.pack()  
  
  
button = Button(root, text="Click me", padx=50, pady=10, command=count, fg="blue") 
#note that you dont call the function here with the (), if that is done, the function will run automatically when the profram is executed. except that is our desire then it can be done same
button.pack()  
  
root.mainloop()
```

### Creating input fields in python
In tkinter, an input widget is called entry. this is used in collecting fields from user depending of users choice of input. At a basic application, the use entry, we define it as below
```python 
from tkinter import *  
  
root = Tk()  
  

e = Entry(root, width=50, bg="grey")
e.pack()
#where e is the variable name holding the Entry widget which will be visibel on the root window
def count():  
lbl = Label(root, text="This is a test")  
lbl.pack()  
  
  
button = Button(root, text="Click me", padx=50, pady=10, command=count)  
button.pack()  
  
root.mainloop()
```

We can get the input from the text fied input from user and display it on the screen with this simple code
```python
from tkinter import *  
  
root = Tk()  
  
def name():  
lbl = Label(root, text=e.get())  
lbl.pack()  
  
  
e = Entry(root, width=50, bg="grey", fg="red", borderwidth=5)  
e.pack()  
  
btn = Button(root, padx=50, text="Click me", command=name)  
btn.pack()  
  
root.mainloop()
```

we can as well make your write up look good by concatenating it with some pre text like such
```python
from tkinter import *  
  
root = Tk()  
  
def name():  
#concatenating
lbl = Label(root, text="Hello " + e.get())  
lbl.pack()  
  
  
e = Entry(root, width=50, bg="grey", fg="red", borderwidth=5)  
e.pack()  
  
btn = Button(root, padx=50, text="Click me", command=name)  
btn.pack()  
  
root.mainloop()
```

we can make it pretty cool by re-writting our code to look decent like this 
```python
from tkinter import *  
  
root = Tk()  
  
def name(): 
hello = "Hello " + e.get()
lbl = Label(root, text=hello)  
lbl.pack()  
  
  
e = Entry(root, width=50, bg="grey", fg="red", borderwidth=5)  
e.pack() 
e.insert(0, "Enter your name:")
#the insert is use to place a value (call it placeholder) into the text field or any other desired content when the program is executed
  
btn = Button(root, padx=50, text="Click me", command=name)  
btn.pack()  
  
root.mainloop()
```

### Creating a simple calculator with tkinter
```python
from tkinter import *  
  
root = Tk()  
root.title("Simple Calculator")  
  
e = Entry(root, width=35, borderwidth=5)  
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)  
  
def btn_click(number):  
cur = e.get()  
e.delete(0, END)  
e.insert(0, str(cur) + str(number))  
  
  
def btn_clear():  
e.delete(0, END)  
  
  
def btn_add():  
fnum = e.get()  
global fstNum  
fstNum = int(fnum)  
e.delete(0, END)  
  
  
def btn_equal():  
curNum = e.get()  
e.delete(0, END)  
e.insert(0, fstNum + int(curNum))  
  
btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))  
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_click(2))  
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_click(3))  
btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_click(4))  
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_click(5))  
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_click(6))  
btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_click(7))  
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_click(8))  
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_click(9))  
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0))  
btn_plus = Button(root, text="+", padx=39, pady=20, command=btn_add)  
btn_clr = Button(root, text="Clear", padx=77, pady=20, command=btn_clear)  
btn_eq = Button(root, text="=", padx=86, pady=20, command=btn_equal )  
  
  
btn1.grid(row=3, column=0)  
btn2.grid(row=3, column=1)  
btn3.grid(row=3, column=2)  
btn4.grid(row=2, column=0)  
btn5.grid(row=2, column=1)  
btn6.grid(row=2, column=2)  
btn7.grid(row=1, column=0)  
btn8.grid(row=1, column=1)  
btn9.grid(row=1, column=2)  
btn0.grid(row=4, column=0)  
btn_clr.grid(row=4, column=1, columnspan=2)  
btn_plus.grid(row=5, column=0)  
btn_eq.grid(row=5, column=1, columnspan=2)  
  
root.mainloop()
```