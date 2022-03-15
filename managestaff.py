from tkinter import *
from tkinter.messagebox import *
from pymysql import*
from connection import*
from tkinter.ttk import *

class managestaff:

    def update(self):
        s = "update staff set name='"+self.textbox1.get()+"',email='"+self.textbox2.get()+"',"+"mobile='"+self.textbox3.get()+"'" \
                                    ",password='"+self.textbox4.get()+"',designation='"+self.textbox5.get()+"'where staff_id="+self.cb1.get()

        cr=conn.cursor()
        cr.execute(s)
        conn.commit()
        showinfo("", "Data Updated")

    def delete(self):
        cr = conn.cursor()
        s = "delete from staff where staff_id="+self.cb1.get()
        cr.execute(s)
        conn.commit()
        showinfo("", "Staff Record Deleted")
        self.textbox1.delete(0, END)
        self.textbox2.delete(0, END)
        self.textbox3.delete(0, END)
        self.textbox4.delete(0, END)
        self.textbox5.delete(0, END)
        s = "select * from staff"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        x = []
        for row in result:
            x.append(row[0])
        self.cb1["values"] = x
        self.cb1.current(0)

    def search(self):
        if self.cb1.get() == "":
            showinfo("", "Please enter staff id ")
        else:

            s = "select * from staff where staff_id="+self.cb1.get()
            cr = conn.cursor()
            n = cr.execute(s)
            row = cr.fetchone()

            if n > 0:
                self.bt2["state"] = "normal"
                self.bt3["state"] = "normal"
                self.textbox1.delete(0, END)
                self.textbox2.delete(0, END)
                self.textbox3.delete(0, END)
                self.textbox4.delete(0, END)
                self.textbox5.delete(0, END)
                self.textbox1.insert(0, str(row[1]))
                self.textbox2.insert(0, str(row[2]))
                self.textbox3.insert(0, str(row[3]))
                self.textbox4.insert(0, str(row[4]))
                self.textbox5.insert(0, str(row[5]))

    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.config(background='#FFE4C4')
        s = "select * from staff"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        x = []
        for row in result:
            x.append(row[0])
        self.cb1 = Combobox(self.root, values=x, state="readonly")
        self.cb1.grid(row=0,column=1)

        self.lb1 = Label(self.root, text="Select Staff_ID")
        self.lb2 = Label(self.root, text="Name")
        self.lb3 = Label(self.root, text="E-Mail")
        self.lb4 = Label(self.root, text="Mobile")
        self.lb5 = Label(self.root, text="Password")
        self.lb6 = Label(self.root, text="Designation")

        self.lb1.grid(row=0, column=0)
        self.lb2.grid(row=1, column=0)
        self.lb3.grid(row=2, column=0)
        self.lb4.grid(row=3, column=0)
        self.lb5.grid(row=4, column=0)
        self.lb6.grid(row=5, column=0)

        self.textbox1 = Entry(self.root)
        self.textbox2 = Entry(self.root)
        self.textbox3 = Entry(self.root)
        self.textbox4 = Entry(self.root, show ="*")
        self.textbox5 = Entry(self.root)

        self.textbox1.grid(row=1, column=1)
        self.textbox2.grid(row=2, column=1)
        self.textbox3.grid(row=3, column=1)
        self.textbox4.grid(row=4, column=1)
        self.textbox5.grid(row=5, column=1)

        self.bt1 = Button(self.root, text="Get Details", command=self.search)
        self.bt2 = Button(self.root, text="Delete", state="disabled", command=self.delete)
        self.bt3 = Button(self.root, text="Edit", state="disabled", command=self.update)

        self.bt1.grid(row=0, column=2)
        self.bt2.grid(row=7, column=0)
        self.bt3.grid(row=7, column=2)

        self.root.mainloop()



