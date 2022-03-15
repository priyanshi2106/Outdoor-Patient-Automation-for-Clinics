from tkinter import *
from tkinter.messagebox import*
from connection import*

class adddoctor:

    def add(self):
        if self.textbox1.get() == "" or self.textbox2.get() == "" or self.textbox3.get() == "":
            showinfo("", "Fields Marked Star Are Mandatory")
        elif str(self.textbox2.get()).count("@") != 1:
            showinfo("", "Invalid Email Address")
        elif str(self.textbox2.get()).count(".com") != 1:
            showinfo("", "Invalid Email Address")
        elif len(self.textbox3.get()) != 10:
            showinfo("", "Invalid Mobile Number")
        else:
            s = "insert into doctors values(NULL,'" + self.textbox2.get() + "','" + self.textbox1.get() + "','" + self.textbox3.get() + "','"+self.textbox4.get()+ "')"
            cr = conn.cursor()
            cr.execute(s)
            conn.commit()
            showinfo("", "Doctor Added Successfully")

    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x300")
        self.root.config(background='#FFE4C4')
        self.lb1 = Label(self.root, text="ADD DOCTOR",  bg="#66CDAA")
        self.lb2 = Label(self.root, text="Name *",  bg='#FFE4C4')
        self.lb3 = Label(self.root, text="E-Mail *" ,  bg='#FFE4C4')
        self.lb4 = Label(self.root, text="Mobile *",  bg='#FFE4C4')
        self.bt1 = Button(self.root, text="Add", command=self.add,  bg="#CDB79E")
        self.lb5 = Label(self.root, text="Password",  bg="#CDB79E")

        self.lb1.grid(row=0, column=1)
        self.lb2.grid(row=1, column=0)
        self.lb3.grid(row=2, column=0)
        self.lb4.grid(row=3, column=0)
        self.bt1.grid(row=5, column=1)
        self.lb5.grid(row=4, column=0)

        self.textbox1 = Entry(self.root)
        self.textbox1.grid(row=1, column=1)
        self.textbox2 = Entry(self.root)
        self.textbox2.grid(row=2, column=1)
        self.textbox3 = Entry(self.root)
        self.textbox3.grid(row=3, column=1)
        self.textbox4 = Entry(self.root, show="*")
        self.textbox4.grid(row=4, column=1)

        self.root.mainloop()

