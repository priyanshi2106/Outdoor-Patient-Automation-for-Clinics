from tkinter import *
from tkinter.ttk import Treeview
from pymysql import *
from connection import *


class viewstaff:

    def __init__(self):
        self.root = Tk()
        self.root.config(background='#FFE4C4')
        self.t1 = Treeview(self.root, columns=("staff_id", "staff name", "email", "mobile", "password", "designation"))
        self.t1.heading("staff_id", text="Staff_ID")
        self.t1.heading("staff name", text="Staff Name")
        self.t1.heading("email", text="Email")
        self.t1.heading("mobile", text="Mobile Number")
        self.t1.heading("password", text="Password")
        self.t1.heading("designation", text="Designation")
        self.t1["show"] = "headings"

        s = "Select * from staff"

        cr = conn.cursor()
        cr.execute(s)

        result = cr.fetchall()

        i = 0
        for row in result:
            self.t1.insert("", index=i, values=row)
            i = i + 1


        self.t1.pack()
        self.root.mainloop()

