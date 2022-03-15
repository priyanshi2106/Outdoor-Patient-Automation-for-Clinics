from tkinter import *
from tkinter.messagebox import *
from doctorviewappointments import *
from changepassword1 import *


class doctorhome:
    def update(self):
        obj = changepassword1(self.globalemail)

    def add(self):

        obj = doctorviewappointments(self.globalemail)

    def __init__(self, email):
        self.root = Tk()
        self.globalemail=""
        self.globalemail= str(email)
        self.root.geometry("300x300")
        self.root.config(background='#FFE4C4')
        self.lb1 = Label(self.root, text="Welcome  " + str(email),  bg="#66CDAA")
        self.lb1.grid(row=0,column=1)
        self.bt1 = Button(self.root, text="Change Password",command=self.update,  bg="#CDB79E")
        self.bt1.grid(row=1, column=0)
        self.bt2 = Button(self.root, text="View Appointments",command=self.add,  bg="#CDB79E")
        self.bt2.grid(row=1, column=1)

        self.root.mainloop()



