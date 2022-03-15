from tkinter import *
from tkinter .messagebox import *
from connection import *

class changepassword1:
    def change(self):
        if self.textbox1.get() == "" or self.textbox2.get() == "" or self.textbox3.get() == "":
            showinfo("", "Fields Marked Star Are Mandatory To Fill")
        elif len(self.textbox2.get()) < 4:
            showinfo("", "Password must contain 5-8 characters")
        elif len(self.textbox3.get()) < 4:
            showinfo("", "Password Must contain 5-8 characters")
        elif self.textbox2.get() != self.textbox3.get():
            showinfo("", "New Password and Confirm Password do not match")
        else:
            s = "update doctors set password='" + self.textbox3.get() + "'where email='" + self.globalemail + "'"
            cr = conn.cursor()
            cr.execute(s)
            conn.commit()
            showinfo("", "Password Updated")

    def __init__(self,email):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.config(background='#FFE4C4')
        self.globalemail = ""
        self.globalemail = str(email)
        self.root.geometry("500x500")

        self.lb1 = Label(self.root, text="CHANGE PASSWORD", bg="#66CDAA")
        self.lb2 = Label(self.root, text="Old Password *",  bg='#FFE4C4')
        self.lb3 = Label(self.root, text="New Password *",  bg='#FFE4C4')
        self.lb4 = Label(self.root, text="Confirm Password *",  bg='#FFE4C4')

        self.lb1.grid(row=0, column=1)
        self.lb2.grid(row=1, column=0)
        self.lb3.grid(row=2, column=0)
        self.lb4.grid(row=3, column=0)

        self.textbox1 = Entry(self.root, show="*")
        self.textbox2 = Entry(self.root, show="*")
        self.textbox3 = Entry(self.root, show="*")

        self.textbox1.grid(row=1, column=1)
        self.textbox2.grid(row=2, column=1)
        self.textbox3.grid(row=3, column=1)

        self.bt1 = Button(self.root, text="Change", command=self.change,  bg="#CDB79E")
        self.bt1.grid(row=4, column=1)

        self.root.mainloop()