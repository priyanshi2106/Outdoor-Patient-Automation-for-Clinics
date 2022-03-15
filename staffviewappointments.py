from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from pymysql import *
from connection import *
from tkcalendar import *


class staffviewappointments:

    def search(self):
        self.t1.delete(*self.t1.get_children())
        s = "select * from appointment where date= '" + str(
            self.textbox1.get_date()) + "' and status ='"+"pending'"+""
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        i = 0
        for row in result:
            self.t1.insert("", index=i, values=row)
            i = i + 1

    def __init__(self):
        self.root = Tk()
        self.root.config(background='#FFE4C4')
        self.p1 = PanedWindow(self.root)
        self.p2 = PanedWindow(self.root)
        self.p1.pack()
        self.p2.pack()
        self.textbox1 = DateEntry(self.p1)
        self.textbox1.grid(row=0, column=2)
        self.lb1 = Label(self.p1, text="Select Appointment Date")
        self.lb1.grid(row=0,column=1)
        self.bt1 = Button(self.p1, text="Search", command=self.search)
        self.bt1.grid(row=0, column=3)

        self.t1 = Treeview(self.p2, column=("appointmentid", "pid", "name", "previoushistory", "doctorid", "date", "slotid", "amount", "typeofbooking","paymentrecieved", "token", "status", "diagnosis"))
        self.t1.heading("appointmentid", text="Appointment ID")
        self.t1.heading("pid", text="Patient ID")
        self.t1.heading("name", text="Name")
        self.t1.heading("previoushistory", text="Previous History")
        self.t1.heading("doctorid", text="Doctor ID")
        self.t1.heading("date", text="Date")
        self.t1.heading("slotid", text="Slot ID")
        self.t1.heading("amount", text="Amount")
        self.t1.heading("typeofbooking", text="Type Of Booking")
        self.t1.heading("paymentrecieved", text="Payment Recieved")
        self.t1.heading("token", text="Token")
        self.t1.heading("status", text="Status")
        self.t1.heading("diagnosis", text="Diagnosis")


        self.t1.column("appointmentid", width=100)
        self.t1.column("pid", width=100)
        self.t1.column("name", width=100)
        self.t1.column("previoushistory", width=100)
        self.t1.column("doctorid", width=100)
        self.t1.column("date", width=100)
        self.t1.column("slotid", width=100)
        self.t1.column("amount", width=100)
        self.t1.column("typeofbooking", width=100)
        self.t1.column("paymentrecieved", width=100)
        self.t1.column("token", width=100)
        self.t1.column("status", width=100)
        self.t1.column("diagnosis", width=100)
        self.t1["show"] = "headings"

        self.t1.pack()
        self.root.mainloop()
