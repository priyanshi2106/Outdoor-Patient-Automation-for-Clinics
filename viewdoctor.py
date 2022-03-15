from tkinter import *
from tkinter.ttk import *
from connection import *
from pymysql import *
from tkinter.messagebox import *

class viewdoctor:

    def __init__(self):
        self.root = Tk()
        self.root.config(background='#FFE4C4')
        self.p1 = PanedWindow(self.root)
        self.p2 = PanedWindow(self.root)
        self.p1.pack()
        self.p2.pack()

        self.t1 = Treeview(self.p1, columns= ("doctorid", "email", "name", "mobile"))
        self.t1.heading("doctorid", text="Doctor ID")
        self.t1.heading("email", text="E-Mail")
        self.t1.heading("name", text="Name")
        self.t1.heading("mobile", text="Mobile")
        self.t1["show"] = "headings"

        s = "Select * from doctors"

        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()

        i = 0

        for row in result:
            self.t1.insert("", index = i, values = row)
            i = i+1
        self.t1.pack()
        self.root.mainloop()

