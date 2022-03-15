from tkinter import *
from tkinter.messagebox import *
from connection import *
from pymysql import *
from tkcalendar import *
from tkinter.ttk import *


class appointment:
    def callback(self, event):
        self.cb3.set("")
        self.cb3["values"] = ""
        doctorid = self.cb2.get()
        s = "select * from slot where doctorid='" + str(doctorid) + "'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()

        x = []
        for row in result:
            x.append(row[0])

        self.cb3["values"] = x

    def go(self):
        s = self.cb1.get()
        if s == "":
            showinfo("", "Select a patient_ID")
        else:
            s = "select * from patient where pid='" + s + "'"
            cr = conn.cursor()
            n = cr.execute(s)
            row = cr.fetchone()
            self.textbox1.delete(0, END)

            if n > 0:
                self.textbox1.insert(0, str(row[1]))

    def submit(self):
        # if self.textbox1.get()=="" or self.textbox2.get()=="" or self.textbox3.get()=="" or self.textbox4.get()=="" or self.textbox5.get()== "":
        #   showinfo("", "Fields Marked Star Are Mandatory")
        s1 = "select * from appointment where doctorid='"+str(self.cb2.get())+"' and date='"+str(self.textbox3.get_date())+"'and slotid='"+str(self.cb3.get())+"'"
        cr = conn.cursor()
        n = cr.execute(s1)

        token = 0
        s2 = "select maxcapacity from slot where doctorid='"+str(self.cb2.get())+"' and slotid='"+str(self.cb3.get())+"'"
        cr.execute(s2)
        row = cr.fetchone()
        maxcapacity = (int)(row[0])
        if n<=maxcapacity:
            cr.execute(s1)
            result = cr.fetchall()
            for row in result:
                token = (int)(row[10])
            token = token+1




            s = "insert into appointment values(NULL,'" + str(
            self.cb1.get()) + "','" + self.textbox1.get() + "','" + self.textbox2.get(0.0, END) + "','" + str(
            self.cb2.get()) + "','" + str(self.textbox3.get_date()) + "','" + str(
            self.cb3.get()) +"','"+ self.textbox4.get() + "','" + str(
            self.cb4.get()) + "','" + self.textbox5.get() + "','"+str(token)+"','pending','')"
            cr = conn.cursor()
            cr.execute(s)
            conn.commit()
            showinfo("", "Appointment Booked Successful")
        else :
            showinfo("", "Slot is Full")


    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x1000")
        self.root.config(background='#FFE4C4')
        self.lb1 = Label(self.root, text="APPOINTMENTS")
        self.lb2 = Label(self.root, text="Patient ID *")
        self.lb3 = Label(self.root, text="Name *")
        self.lb4 = Label(self.root, text="Previous History *")
        self.lb5 = Label(self.root, text="Select DoctorID *")
        self.lb6 = Label(self.root, text="Date *")
        self.lb7 = Label(self.root, text="Slot *")
        self.lb8 = Label(self.root, text="Amount *")
        self.lb9 = Label(self.root, text="Type of Booking *")
        self.lb10 = Label(self.root, text="Payment Recieved *")

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
        self.textbox2 = Text(self.root, height=3)
        self.textbox3 = DateEntry(self.root)
        self.textbox4 = Entry(self.root)
        self.textbox5 = Entry(self.root)

        self.textbox1.grid(row=2, column=1)
        self.textbox2.grid(row=3, column=1)
        self.textbox3.grid(row=5, column=1)
        self.textbox4.grid(row=7, column=1)
        self.textbox5.grid(row=9, column=1)

        self.cb1 = Combobox(self.root, state="readonly")
        self.cb2 = Combobox(self.root, state="readonly")
        self.cb3 = Combobox(self.root, state="readonly")
        self.cb4 = Combobox(self.root, values=("call", "Walkin"), state="readonly")

        self.cb1.grid(row=1, column=1)
        self.cb2.grid(row=4, column=1)
        self.cb3.grid(row=6, column=1)
        self.cb4.grid(row=8, column=1)

        self.bt1 = Button(self.root, text="GO", command=self.go)
        self.bt2 = Button(self.root, text="Submit", command=self.submit)

        self.bt1.grid(row=1, column=2)
        self.bt2.grid(row=10, column=1)

        s = "select * from patient"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        x = []
        for row in result:
            x.append(row[0])
        self.cb1['values'] = x

        s = "select * from doctors"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        x = []
        for row in result:
            x.append(row[0])
        self.cb2['values'] = x
        self.cb2.bind("<<ComboboxSelected>>", self.callback)

        self.root.mainloop()


