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