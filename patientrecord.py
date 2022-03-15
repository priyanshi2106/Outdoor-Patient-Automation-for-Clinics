from tkinter import *
from tkinter.messagebox import *
from connection import *
from tkcalendar import *

class patientrecord:

    def add(self):
        if self.textbox1.get() == "" or self.textbox2.get() == "" or self.textbox3.get() == "" or self.textbox4.get() == "" or self.textbox5.get() == "" or str(self.textbox6.get_date()) == "" or self.textbox7.get() == "" or self.textbox8.get(0.0,END) == "" or self.textbox9.get(0.0,END) == "":
            showinfo("", "Fields Marked Star Are Mandatory")
        elif str(self.textbox2.get()).count("@") != 1:
            showinfo("", "Invalid Email Address")
        elif str(self.textbox2.get()).count(".com") != 1:
            showinfo("", "Invalid Email Address")
        elif len(self.textbox3.get()) != 10:
            showinfo("", "Invalid Mobile Number")

        else:
            s = "insert into patient values(NULL,'" + self.textbox1.get() + "','" + self.textbox2.get() + "','" + self.textbox3.get() + "','" + self.textbox4.get() + "','" + self.textbox5.get() +"','" +str(self.textbox6.get_date())+"','" + self.textbox7.get() +"','" + self.textbox8.get(0.0, END) +"','" + self.textbox9.get(0.0, END) + "')"
            cr = conn.cursor()
            cr.execute(s)
            conn.commit()
            showinfo("", "Patient Added Successfully")

    def __init__(self):
        self.root = Tk()
        self.root.geometry("1024x800")
        self.root.config(background='#FFE4C4')
        self.lb1 = Label(self.root, text="PATIENT RECORD", bg="#66CDAA")
        self.lb2 = Label(self.root, text="Name *",  bg= "#FFE4C4")
        self.lb3 = Label(self.root, text="E-Mail *",  bg= "#FFE4C4")
        self.lb4 = Label(self.root, text="Mobile *",  bg= "#FFE4C4")
        self.lb5 = Label(self.root, text="Spouse Name *",  bg= "#FFE4C4")
        self.lb6 = Label(self.root, text="Father Name *",  bg= "#FFE4C4")
        self.lb7 = Label(self.root, text="DOB *",  bg= "#FFE4C4")
        self.lb8 = Label(self.root, text="Age *", bg= "#FFE4C4")
        self.lb9 = Label(self.root, text="Known Problems *",  bg= "#FFE4C4")
        self.lb10 = Label(self.root, text="Known Allergies *",  bg= "#FFE4C4")

        self.bt1 = Button(self.root, text="Add", command=self.add,  bg="#CDB79E")
        self.bt1.grid(row=11, column=1)

        self.lb1.grid(row=0, column=1)
        self.lb2.grid(row=1, column=0)
        self.lb3.grid(row=2, column=0)
        self.lb4.grid(row=3, column=0)
        self.lb5.grid(row=4, column=0)
        self.lb6.grid(row=5, column=0)
        self.lb7.grid(row=6, column=0)
        self.lb8.grid(row=7, column=0)
        self.lb9.grid(row=8, column=0)
        self.lb10.grid(row=9, column=0)

        self.textbox1 = Entry(self.root)
        self.textbox2 = Entry(self.root)
        self.textbox3 = Entry(self.root)
        self.textbox4 = Entry(self.root)
        self.textbox5 = Entry(self.root)
        self.textbox6 = DateEntry(self.root)
        self.textbox7 = Entry(self.root)
        self.textbox8 = Text(self.root, height=5)
        self.textbox9 = Text(self.root, height=5)

        self.textbox1.grid(row=1, column=1)
        self.textbox2.grid(row=2, column=1)
        self.textbox3.grid(row=3, column=1)
        self.textbox4.grid(row=4, column=1)
        self.textbox5.grid(row=5, column=1)
        self.textbox6.grid(row=6, column=1)
        self.textbox7.grid(row=7, column=1)
        self.textbox8.grid(row=8, column=1)
        self.textbox9.grid(row=9, column=1)

        self.root.mainloop()





