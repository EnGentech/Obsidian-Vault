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
