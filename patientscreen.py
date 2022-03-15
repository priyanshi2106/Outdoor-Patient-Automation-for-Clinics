import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from connection import *
from pymysql import *
import pyttsx3
from tkcalendar import *
from http.client import HTTPConnection


class patientscreen:

    def sound(self,s1,s2):
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 0.9)
        engine.say(s1)
        engine.say(s2)

        engine.runAndWait()

    def search(self):

        s = "select token from appointment where doctorid='"+str(self.cb1.get())+"' and date='"+str(self.textbox1.get_date())+"' and status='pending'"
        cr = conn.cursor()
        n= cr.execute(s)
        tkn =0
        if n>0:
             result = cr.fetchone()
             tkn = int(result[0])
             self.sound("Attention Everyone", "Next Turn is of token number " + str(tkn))
             self.t1.delete(*self.t1.get_children())
             print(str(self.textbox1.get()))

        s = "Select * from appointment where doctorid='" + str(self.cb1.get()) + "' and date='" + str(
            self.textbox1.get_date()) + "' and status='pending'"
        cr = conn.cursor()
        n=cr.execute(s)
        if n>=0:

             result = cr.fetchall()
             i = 0
             for row in result:
                 self.t1.insert("",index=i, values=row)
                 i = i+1
        else:
            showinfo("", "No Record Available")


    def change(self):

        if self.textbox2.get()=="":
            showinfo("","Enter Diagnosis")
        else:
            f = self.t1.focus()
            d = self.t1.item(f)
            l = d['values']
            if len(l) > 0:
               tn=(int)(l[10])+1
               conn = connect("opdpriyanshi.db.7623447.2e4.hostedresource.net", "opdpriyanshi", "VMMeducation@123",
                              "opdpriyanshi")
               #conn = Connect("127.0.0.1", "root", "", "opd")
               p = "select mobile from patient where pid='"+str(l[1])+"'"
               cr = conn.cursor()
               cr.execute(p)
               rs = cr.fetchone()
               self.sound("Attention Everyone", "Next turn is of token number "+str(tn))
               appointmentid = l[0]
               conn = connect("opdpriyanshi.db.7623447.2e4.hostedresource.net", "opdpriyanshi", "VMMeducation@123",
                              "opdpriyanshi")
               #conn = Connect("127.0.0.1", "root", "", "opd")
               s = "update appointment set status='"+"confirmed'"+"where appointmentid='"+str(appointmentid)+"'"
               cr = conn.cursor()
               cr.execute(s)
               conn.commit()
               for row in self.t1.get_children():
                   self.t1.delete(row)
               s = "Select * from appointment where doctorid='" + str(self.cb1.get()) + "' and date='" + str(
                   self.textbox1.get_date()) + "' and status='pending'"
               cr = conn.cursor()
               cr.execute(s)
               result = cr.fetchall()
               # showinfo('', 'Status Updated successfully')
               i = 0
               for row in result:
                   self.t1.insert("", index=i, values=row)
                   i = i + 1
               s = "update appointment set diagnosis='" + self.textbox2.get() + "'  where appointmentid='" + str(
                   appointmentid) + "'"
               cr = conn.cursor()
               cr.execute(s)
               conn.commit()
               dg = self.textbox2.get()
               msg = "Diagnosis report "+str(dg)
               mobileno = str(rs[0])
               msg = msg.replace(' ', '%20')
               conn = HTTPConnection("server1.vmm.education")
               conn.request('GET',
                            "/VMMCloudMessaging/AWS_SMS_Sender?""username=priyanshi&password=F4V2YEWG&message=" + msg + "&phone_numbers=" + mobileno)
               response = conn.getresponse()
               print(response.read())
               showinfo("", "sms sent")

               showinfo("", "Diagnosis sms Sent")

            else:
                showinfo('', ' select any appointment in view')

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.config(background='#FFE4C4')
        self.p1 = tkinter.PanedWindow(self.root)
        self.p2 = tkinter.PanedWindow(self.root)
        self.p3 = tkinter.PanedWindow(self.root)
        self.p1.pack()
        self.p2.pack()
        self.p3.pack()
        self.p1.config(background='#FFE4C4')
        self.p3.config(background='#FFE4C4')
        s1 = "select * from doctors "
        cr = conn.cursor()
        cr.execute(s1)
        result = cr.fetchall()
        y=[]
        for row in result:
            y.append(row[0])
        self.lb1 = tkinter.Label(self.p1, text="Date")
        self.lb1.grid(row=0, column=2)

        self.lb2 = tkinter.Label(self.p1, text="Doctor ID")
        self.lb2.grid(row=0, column=0)
        self.textbox1 = DateEntry(self.p1)
        self.textbox1.grid(row=0, column=3)

        self.bt1 = tkinter.Button(self.p3, text="Change Status", command=self.change)
        self.bt1.grid(row=2, column=1)

        self.lb3 = Label(self.p3, text="Diagnosis")
        self.lb3.grid(row=3,column=0)

        self.textbox2 = Entry(self.p3)
        self.textbox2.grid(row=3, column=1)

        self.bt2 = tkinter.Button(self.p1, text ="Search", command=self.search)
        self.bt2.grid(row=0, column=4)

        self.cb1 = Combobox(self.p1, values= y)
        self.cb1.grid(row=0, column=1)

        self.t1 = Treeview(self.p2, column=("appointmentid", "pid", "name", "previoushistory", "doctorid", "date", "slotid", "amount", "typeofbooking", "paymentrecieved", "token", "status", "diagnosis"))
        self.t1.heading("appointmentid", text="Appointment ID")
        self.t1.heading("pid", text="Patient ID")
        self.t1.heading("name", text="Name")
        self.t1.heading("previoushistory", text="Previous History")
        self.t1.heading("doctorid", text="Doctor ID")
        self.t1.heading("date", text="Date")
        self.t1.heading("slotid", text="Slot ID")
        self.t1.heading("amount", text="Amount")
        self.t1.heading("typeofbooking", text="Type Of Booking")
        self.t1.heading("paymentrecieved", text="Payment Recieved")
        self.t1.heading("token", text="Token")
        self.t1.heading("status", text="Status")
        self.t1.heading("diagnosis", text="Diagnosis")
        self.t1.column("appointmentid",width=100)
        self.t1.column("pid", width=100)
        self.t1.column("name", width=100)
        self.t1.column("previoushistory", width=100)
        self.t1.column("doctorid", width=100)
        self.t1.column("date", width=100)
        self.t1.column("slotid", width=100)
        self.t1.column("amount", width=100)
        self.t1.column("typeofbooking", width=100)
        self.t1.column("paymentrecieved", width=100)
        self.t1.column("token", width=100)
        self.t1.column("status", width=100)
        self.t1.column("diagnosis", width=100)
        self.t1["show"] = "headings"

       # s = "select * from appointment where date='"+str(self.textbox1.get_date())+"'"
        #cr = conn.cursor()
        #cr.execute(s)
        #result = cr.fetchall()

       # i=0
        #for row in result:
         #   self.t1.insert("", index=i,values=row)
          #  i = i+1
        self.t1.pack()
        self.root.mainloop()
