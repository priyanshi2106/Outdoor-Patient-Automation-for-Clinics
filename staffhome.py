from tkinter import *
from tkinter.messagebox import *
from patientrecord import *
from changepassword import*
from staffviewappointments import *

class staffhome:

    def view(self):
        obj = staffviewappointments()

    def update(self,email):
        obj = changepassword(self.globalemail)

    def add(self):

        obj = patientrecord()

    def __init__(self,email):
        self.root = Tk()
        self.root.config(background='#FFE4C4')
        self.globalemail = ""
        self.globalemail = str(email)
        self.root.geometry("300x300")
        self.globalemail = str(email)
        self.lb1 = Label(self.root, text="Welcome  " + str(email))
        self.lb1.grid(row=0,column=1)
        self.bt1 = Button(self.root, text="Change Password", command=self.update)
        self.bt1.grid(row=1, column=0)
        self.bt2 = Button(self.root, text="Add Patient",command=self.add)
        self.bt2.grid(row=1, column=1)
        self.bt3 = Button(self.root, text="View Appointments", command=self.view)
        self.bt3.grid(row=1, column=2)

        self.root.mainloop()



