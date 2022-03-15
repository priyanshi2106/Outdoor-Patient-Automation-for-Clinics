from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from pymysql import *

from connection import *


class viewpatients:

    def delete(self):
        f=self.t1.focus()
        d=self.t1.item(f)
        l=d['values']
        if len(l)>0:
            pid = l[0]
            s = "delete from patient where pid='"+str(pid)+"'"
            cr = conn.cursor()
            cr.execute(s)
            conn.commit()
            for row in self.t1.get_children():
                self.t1.delete(row)
            s = "Select * from patient"
            cr = conn.cursor()
            cr.execute(s)
            result = cr.fetchall()
            showinfo('', 'patient deleted successfully')

            i = 0
            for row in result:
                self.t1.insert("", index=i, values=row)
                i = i + 1
        else:
            showinfo('', ' select any patient in view')

    def __init__(self):

        self.root = Tk()
        self.root.config(background='#FFE4C4')
        self.p1 = PanedWindow(self.root)
        self.p2 = PanedWindow(self.root)
        self.p1.pack()
        self.p2.pack()
        self.bt1 = Button(self.p2, text="Delete", command=self.delete)
        self.bt1.grid(row=0, column=2)
        self.t1 = Treeview(self.p1, columns=("pid", "pname", "email", "mobile", "spousename", "fathername", "dob", "age", "knownproblems", "knownallergies"))
        self.t1.heading("pid", text="Patient ID")
        self.t1.heading("pname", text="Patient Name")
        self.t1.heading("email", text="Email")
        self.t1.heading("mobile", text="Mobile")
        self.t1.heading("spousename", text="Spouse Name")
        self.t1.heading("fathername", text="Father Name")
        self.t1.heading("dob", text="DOB")
        self.t1.heading("age", text="Age")
        self.t1.heading("knownproblems", text="Known Problems")
        self.t1.heading("knownallergies", text="Known Allergies")

        self.t1.column("pid", width=100)
        self.t1.column("pname", width=100)
        self.t1.column("email", width=100)
        self.t1.column("mobile", width=100)
        self.t1.column("spousename", width=100)
        self.t1.column("fathername", width=100)
        self.t1.column("dob", width=100)
        self.t1.column("age", width=100)
        self.t1.column("knownproblems", width=100)
        self.t1.column("knownallergies", width=100)
        self.t1["show"] = "headings"

        s = "Select * from patient"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()

        i = 0
        for row in result:
            self.t1.insert("",index = i, values = row)
            i=i+1
        self.t1.pack()
        self.root.mainloop()

