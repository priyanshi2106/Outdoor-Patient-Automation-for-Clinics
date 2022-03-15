from tkinter import*
from tkinter import ttk

from addstaff import*
from patientscreen import *
from viewstaff import *
from managestaff import *
from patientrecord import *
from viewpatients import *
from adddoctor import *
from viewdoctor import*
from appointment import *
from stafflogin import *
from addslots import *
from doctorlogin import *
from PIL import Image,ImageTk

class main:
    def fire1(self):
        x = addstaff()
    def fire2(self):
        x = viewstaff()
    def fire3(self):
        x = managestaff()
    def fire4(self):
        x = stafflogin()
    def fire5(self):
        x =patientrecord()
    def fire6(self):
        x = viewpatients()

    def fire7(self):
        x = adddoctor()
    def fire8(self):
       x= viewdoctor()
    def fire9(self):
        x = addslots()
    def fire10(self):
        x = appointment()
    def fire11(self):
        x = patientscreen()
    def fire12(self):
        x = doctorlogin()

    def __init__(self):
        self.root = Tk()
        self.root.geometry("10240x800")
        self.root.config(background="#76EEC6")
        self.a = Image.open("ps1.png").resize((1400,700), Image.ANTIALIAS)
        dp = ImageTk.PhotoImage(self.a)
        Label(self.root, image=dp, background="#76EEC6").pack()

        self.mymenu = Menu(self.root)
        self.root.title("WELCOME TO MY OPD SOFTWARE")

        self.root.config(menu=self.mymenu)

        self.submenu1 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Add", menu=self.submenu1)
        self.submenu1.add_command(label="Add Staff", command=self.fire1)
        self.submenu1.add_command(label="Add Doctor", command=self.fire7)
        self.submenu1.add_command(label="Add Appointment", command=self.fire10)
        self.submenu1.add_command(label="Add Patient", command=self.fire5)

        self.submenu2 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="View", menu=self.submenu2)
        self.submenu2.add_command(label="View Patients",command=self.fire6)
        self.submenu2.add_command(label="View Staff", command=self.fire2)
        self.submenu2.add_command(label="View Doctor", command=self.fire8)

        self.submenu3 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage", menu=self.submenu3)
        self.submenu3.add_command(label="Manage Staff",command=self.fire3)
        self.submenu3.add_command(label="Manage Doctors", command=self.fire9)
        self.submenu3.add_command(label="Manage Patients", command=self.fire11)

        self.submenu4 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Login", menu=self.submenu4)
        self.submenu4.add_command(label="Staff Login",command=self.fire4)
        self.submenu4.add_command(label="Doctor Login", command=self.fire12)

        self.root.mainloop()
