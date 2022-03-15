from http.client import *
from tkinter import *
from tkinter.messagebox import *
from addstaff import *
from connection import *


class test:

    def go(self):
        s = "select password from staff where mobile='"+self.textbox1.get()+"'"
        cr = conn.cursor()
        cr.execute(s)





    def __init__(self):
        self.root=Tk()
        self.lb=Label(self.root,text="Enter Mobile Number1")
        self.textbox1=Entry(self.root)

        self.lb2=Label(self.root,text="Enter SMS ")
        self.textbox2=Entry(self.root)

        self.bt1=Button(self.root,text="Submit",command=self.sendsms)

        self.lb.grid(row=0,column=0)
        self.textbox1.grid(row=0,column=1)

        self.lb2.grid(row=1,column=0)
        self.textbox2.grid(row=2,column=1)


        self.bt1.grid(row=3,column=2)
        self.bt2 = Button(self.root, text="Go",command=self.go)
        self.bt2.grid(row=1, column=1)

        self.root.mainloop()
    def sendsms(self):
        msg=self.textbox2.get()
        mobile=self.textbox1.get()
        msg=msg.replace(" ","%20")
        conn=HTTPConnection("server1.vmm.education")
        conn.request('GET',"/VMMCloudMessaging/AWS_SMS_Sender?""username=priyanshi&password=F4V2YEWG&message="+msg+"&phone_numbers=1"+mobile)
        response=conn.getresponse()
        print(response.read())
        showinfo("Title","SMS Sent")
#------------------------------------------------------------------------------------------------------------------


