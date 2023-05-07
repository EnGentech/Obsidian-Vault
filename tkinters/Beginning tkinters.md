## Intro to python tkinter

Hello World program with tkinter

The code in the github explains the creation of the Hello world using tkinters library in the python program. 
```python
from tkinter import *
#import the library of tkinter into the python module while the * is to import everything within the library

#define a variable name for the Label option used in the tkinter
#the none within the label is an instance of inheritance from the library
name = Label(None, text="Hello World")

#unpack the file and place the content in within the center of the window if theres no argument. however, place and grip can be used in this case.
name.pack()

#the main lunching of the program
name.mainloop()
```

### Tkinter Events and Bindings

### Mouse events
	<Button-1>      left mouse botton
	<Button-2>      middle mouse button (on mouse with 3 button mouse)
	<Button-3>      rightmost mouse button
	<B1-Motion>     mouse moved with left button depressed
	<ButtonRelease-1>     left button released
	<Double-Button-1>     double click on button 1
	<Enter>         mouse pointer entered widget
	<Leave>         mouse pointer leave the widget
### Keyboard events
	<Focusin>       Keyboard focus moved to a widget
	<Focusout>      Keyboard focus moved to another widget
	<Return>        Enter key depressed
	<Key>           A key was depressed
	<Shift-Up>      Up arror while pressing shift key
	<Configure>     widget changed size or location

## Event Handling
* Event sources (widgets) can specify their handlers
   * command handlers
   * Callbacks
   * Function along with buttons

### TK Widgets
	Button  |  Similar to a Label but provides additional functionality for mouse-overs, presses, and releases, as well as keyboard activity/events
	Canvas  |  Provides ability to draw shapes (lines, oval, polygons, rectangles), can contain images or bipmapts
	Checkbutton  |  Set of boxes, of which any number can be checked
	Entry  |  Single-line text field with which to collect keyboard input
	Frame  |  Pure container for other widgets
	LabelFrame  |  Combo of a label and a frame but with extra label attributes
	Listbox  |  Presents the user with a list of choices from which to choose
	Menu  |  Actual list of choices "hanging" from a Menubutton from which the user can choose
	Menubutton  |  Provides infrastructure to contain menus (pulldown, cascading, etc.)
	Message  |  Similar to a Label, but displays multiline text
	PanedWindow  |  A container widget with which you can control other widgerts placed within it 
	Radiobutton  |  Set of button,s of whihc only one can be pressed
	Scale  |  Linear "slider" widget providing an exact value at current setting; with defined starting and ending values
	Scrollbar  |  Provides scrolling functionality to supporting widgets, for example, text, canvas listbox and entry
	Spinbox  |  Combination of an entry with a button letting you adjust its value
	Text  |  Multiline text filed with which to collect of display text from user
	Toplevel  |  Similar to a frame, but provides a seperate window container

### Advantages offered by Tkinter
1. Layered implementation 
2. Accessibility
3. Portability 
4. Availability

### Drawback of Tkinter
* Due to layered approach used in its implementation, execution speed becomes a concern
* Multi-threaded applications are hard to execute

### Label in tkinter
Label could be unpacked to the standard output using .pack, .place or .grid

## .pack
the .pack could be applied with no argument or with argument
arguments used with .pack
* fill=BOTH, 
* pady=value
* padx=value
* expand=True or False

## .grid
* argument(row=value, column=value)

### Button
Button is a basically used for click events. 
basically the relief values applied to a button could be
* RIDGE
* GROOVE
* RAISED
* SUNKEN

## Basic application of button and label
```python
from tkinter import *  
  
win = Tk()  
win.geometry("500x500")  
win.title("Sorting Algorithm")  
  
lbl1 = Label(win, text="First Program", fg="brown", bg="white", relief="solid", font=("arial", 16, "bold"))  
lbl1.place(x="150", y="50")  
  
btn1 = Button(win, text="Click me", fg="white", bg="black", relief='ridge')  
btn1.place(x="150", y="150")  
  
  
win.mainloop()
```

## Registration form
```python
from tkinter import *
window=Tk()
window.geometry("500x500")
window.title("Registration Form")

def printt():
	print("Demo tkinter")

def exit1():
	exit()

label1=Label(window, text="Registration Form", relief="solid",width=20, font=("arial", 19, "bold"))
label1.place(x=90, y=53)

label2=Label(window, text="FirstName:",width=20, font=("arial", 10, "bold"))
label2.place(x=80, y=130)

label3=Label(window, text="LastName:",width=20, font=("arial",10,"bold"))
label3.place(x=80,y=179)

btn1=Button(window, text="Login", width=12, bg="brown", fg='white', command=printt())
btn1.place(x=150, y=380)

btn2=Button(window, text="Exit", width=12, bg="brown", fg='white', command=exit())
btn2.place(x=280, y=380)


```

## Updating the previous concept
### Adding image to tkinter window
To do this, the python needs to be updated, login into your cmd environment and type the code below
```bash
python.exe -m pip install --upgrade pip
#after the above installation, run the below command
pip install pillow
```

### Adding picture to tkinter
```python
from tkinter import *  
from PIL import Image, ImageTk

window = Tk()  
window.geometry("500x500")  
window.title("Registration Form")  

img = Image.open("image path")
photo = ImageTk.PhotoImage(img)

label_image = Label(image=photo)
label_image.pack()
  
def signup():  
f_name = fn.get()  
l_name = ln.get()  
birth = dob.get()  
ctry = var.get()  
print("Thank you for signing up, your details are found below:")  
print("Your full name is: {} {}".format(f_name, l_name))  
print("Your age is: {}".format(birth))  
print("You are from {}".format(ctry))  
  
  
fn = StringVar()  
ln = StringVar()  
dob = StringVar()  
var = StringVar()  
  
  
def exit1():  
exit()  
  
  
label1 = Label(window, text="Registration Form", bg="white", width=20, font=("arial", 19, "bold"))  
label1.place(x=90, y=53)  
  
label2 = Label(window, text="FirstName:", width=20, font=("arial", 10, "bold"))  
label2.place(x=80, y=130)  
  
entry1 = Entry(window, textvar=fn)  
entry1.place(x=240, y=130)  
  
label3 = Label(window, text="LastName:", width=20, font=("arial", 10, "bold"))  
label3.place(x=80, y=179)  
  
entry2 = Entry(window, textvar=ln)  
entry2.place(x=240, y=179)  
  
label4 = Label(window, text="Date of Birth:", width=20, font=("arial", 10, "bold"))  
label4.place(x=87, y=225)  
  
entry3 = Entry(window, textvar=dob)  
entry3.place(x=240, y=225)  
  
label5 = Label(window, text="Country:", width=20, font=("arial", 10, "bold"))  
label5.place(x=73, y=275)  
  
#this line creates a drop down menu
countries = ['America', 'South-Africa', 'Kenya', 'Nigeria', 'Senegal', 'Morocco', 'Egypt', 'Canada', 'Russia',  
'India', 'Argentina', 'Portugal', 'France']  
droplet = OptionMenu(window, var, *countries)  
#.set is provided to create a placeholder value in the dropdown list menu items
var.set("Select Country")
#.config is use to configure the appearance of the dropdown list
droplet.config(width=15)  
droplet.place(x=235, y=265)  
  
btn1 = Button(window, text="Sign-Up", width=12, bg="brown", fg='white', command=signup)  
btn1.place(x=150, y=380)  
  
  
btn2 = Button(window, text="Exit", width=12, bg="brown", fg='white', command=exit1)  
btn2.place(x=280, y=380)  
  
window.mainloop()
```

### Adding Radio button and Messagebox and checkboxes
For this purpose (messagebox), we will need to import messagebox using the below import code
```python
from tkinter import *
import tkinter.messagebox
```
the messagebox can be used with the code
```python
tkinter.messagebos.showinfo("box_title", "message to be displayed")
```

full code sample with radio button 
```python
from tkinter import *  
import tkinter.messagebox  
  
window = Tk()  
window.geometry("500x500")  
window.title("Registration Form")  
  
  
def signup():  
f_name = fn.get()  
l_name = ln.get()  
birth = dob.get()  
ctry = var.get()  
lang = chk  
lang = chk1  
gen = choose.get()  
print("Thank you for signing up, your details are found below:")  
print("Your full name is: {} {} and a {} gender".format(f_name, l_name, gen))  
print("Your age is: {}".format(birth))  
print("You are from {}".format(ctry))  
print("Your preferred programming language is {}".format(lang))  
tkinter.messagebox.showinfo("Welcome", "You have successfully signed up, thank you")  
  
  
fn = StringVar()  
ln = StringVar()  
dob = StringVar()  
var = StringVar()  
chk = "Python"  
chk1 = "Java"  
choose = StringVar()  
  
  
def exit1():  
exit()  
  
  
label1 = Label(window, text="Registration Form", bg="white", width=20, font=("arial", 19, "bold"))  
label1.place(x=90, y=53)  
  
label2 = Label(window, text="FirstName:", width=20, font=("arial", 10, "bold"))  
label2.place(x=80, y=130)  
  
entry1 = Entry(window, textvar=fn)  
entry1.place(x=240, y=130)  
  
label3 = Label(window, text="LastName:", width=20, font=("arial", 10, "bold"))  
label3.place(x=80, y=179)  
  
entry2 = Entry(window, textvar=ln)  
entry2.place(x=240, y=179)  
  
label4 = Label(window, text="Date of Birth:", width=20, font=("arial", 10, "bold"))  
label4.place(x=87, y=225)  
  
entry3 = Entry(window, textvar=dob)  
entry3.place(x=240, y=225)  
  
label5 = Label(window, text="Country:", width=20, font=("arial", 10, "bold"))  
label5.place(x=73, y=275)  
  
countries = ['America', 'South-Africa', 'Kenya', 'Nigeria', 'Senegal', 'Morocco', 'Egypt', 'Canada', 'Russia',  
'India', 'Argentina', 'Portugal', 'France']  
droplet = OptionMenu(window, var, *countries)  
var.set("Select Country")  
droplet.config(width=15)  
droplet.place(x=235, y=265)  
  
label6 = Label(window, text="Gender:", width=20, font=("arial", 10, "bold"))  
label6.place(x=72, y=315)  
  
pick = Radiobutton(window, text='Male', variable=choose, value="Male")  
pick.place(x=240, y=315)  
  
pick1 = Radiobutton(window, text='Female', variable=choose, value="Female")  
pick1.place(x=300, y=315)  
  
label7 = Label(window, text="Prog Language:", width=20, font=("arial", 10, "bold"))  
label7.place(x=95, y=355)  
  
check = Checkbutton(window, text="Python", variable=chk)  
check.place(x=240, y=355)  
check = Checkbutton(window, text="Java", variable=chk1)  
check.place(x=320, y=355)  
  
btn1 = Button(window, text="Sign-Up", width=12, bg="brown", fg='white', command=signup)  
btn1.place(x=150, y=420)  
  
  
btn2 = Button(window, text="Exit", width=12, bg="brown", fg='white', command=exit1)  
btn2.place(x=280, y=420)  
  
window.mainloop()
```