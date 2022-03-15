from tkinter import *
from tkinter.messagebox import *

from PIL import ImageTk

from connection import *
from doctorhome import *
from tkinter import simpledialog
from http.client import *

class doctorlogin:
    def forget(self):
        answer = simpledialog.askstring("input", "What is your registered mobile no", parent=self.root)
        if answer is not None:
            s = "select password from doctors where mobile='"+answer+"'"
            #conn = connect( "opdpriyanshi", "VMMeducation@123","opdpriyanshi")
            conn = Connect("127.0.0.1", "root", "", "opd")
            cr = conn.cursor()
            cr.execute(s)
            result = cr.fetchone()
            msg = "your password is "+ str(result[0])
            mobileno=answer
            msg = msg.replace(' ','%20')
            conn = HTTPConnection("server1.vmm.education")
            conn.request('GET', "/VMMCloudMessaging/AWS_SMS_Sender?""username=priyanshi&password=F4V2YEWG&message=" + msg + "&phone_numbers=" + mobileno)
            response = conn.getresponse()
            print(response.read())
            showinfo("", "Sms Sent")
        else:
            print("Enter Mobile Number")

    def login(self):
        if self.textbox1.get() == "" or self.textbox2.get() == "":
            showinfo("","Fields Marked Are Mandatory")
        elif str(self.textbox1.get()).count("@") != 1:
            showinfo("", "Invalid Email")
        elif str(self.textbox1.get()).count(".com") != 1:
            showinfo("", "Invalid Email")
        elif len(self.textbox2.get())<=4:
            showinfo("","Password must contain 6 to 8 characters")
        else:
            s = "select * from doctors where email='"+self.textbox1.get()+"'and password='"+self.textbox2.get()+"'"
            cr = conn.cursor()
            n = cr.execute(s)
            if n > 0:
                showinfo("", "Login successfull")
                obj = doctorhome(self.textbox1.get())

            else:
                showinfo("", "Login Failed")

    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x300")
        self.root.config(background='#FFE4C4')
        self.lb1 = Label(self.root, text="DOCTOR LOGIN", bg="#66CDAA")
        self.lb2 = Label(self.root, text="E-Mail", bg="#FFE4C4")
        self.lb3 = Label(self.root, text="Password", bg="#FFE4C4")

        self.lb1.grid(row=0, column=1)
        self.lb2.grid(row=1, column=0)
        self.lb3.grid(row=2, column=0)

        self.textbox1 = Entry(self.root)
        self.textbox2 = Entry(self.root, show="*")

        self.textbox1.grid(row=1,column=1)
        self.textbox2.grid(row=2,column=1)

        self.bt1 = Button(self.root, text="Login", command=self.login,bg="#CDB79E")
        self.bt1.grid(row=3,column=1)

        self.bt2 = Button(self.root, text="Forgot Password",command=self.forget,  bg="#CDB79E")
        self.bt2.grid(row=3, column=0)


        self.root.mainloop()
