from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from pymysql import *
from connection import *
from tkcalendar import *
from reportlab.lib.pagesizes import A5
from reportlab.pdfgen import canvas

import subprocess
import random


class doctorviewappointments:

    def generatepdf(self):
        name = str(random.randint(0, 100))
        name_pdf = str("doctorbills//a" + str(name) + ".pdf")
        my_canv = canvas.Canvas(name_pdf, pagesize=A5)
        my_canv.setFont('Helvetica', 14)
        my_canv.setLineWidth(.2)
        y = 580
        my_canv.drawString(160, y, 'Doctor Bills')
        my_canv.line(10, y - 3, 400, y - 3)

        my_canv.setFont('Helvetica', 10)
        my_canv.drawString(30, y - 12, "Appointment ID")
        my_canv.drawString(130, y - 12, "Patient Name")
        my_canv.drawString(230, y - 12, "Slot ID")
        my_canv.drawString(330, y - 12, "Fee Amount")
        y = y - 12
        my_canv.line(10, y - 3, 400, y - 3)
        my_canv.setFont('Helvetica', 8)
        y = y - 3
        s = []
        q = "select * from appointment where doctorid='" + str(self.doctorid) + "' and date= '" + str(
            self.textbox1.get_date()) + "' and status ='confirmed'"
        cr = conn.cursor()
        cr.execute(q)
        result = cr.fetchall()
        for row in result:
            lst = []
            lst.append(row[0])
            lst.append(row[2])
            lst.append(row[6])
            lst.append(row[7])
            s.append(lst)

        tp = 0.0

        for i in range(0, len(s)):
            my_canv.drawString(30, y - 12, str(s[i][0]))
            my_canv.drawString(130, y - 12, str(s[i][1]))
            my_canv.drawString(230, y - 12, str(s[i][2]))
            my_canv.drawString(330, y - 12, str(s[i][3]))
            y = y - 12
            tp = tp+(float)(s[i][3])
        my_canv.line(10, y - 3, 400, y - 3)
        y = y - 3
        my_canv.drawString(230, y - 12, "Total Bill")
        my_canv.drawString(330, y - 12, str(tp))
        my_canv.save()

        subprocess.Popen([name_pdf], shell=True)
        showinfo("", "pdf report saved at" +str("doctorbills//a" +str(name)+".pdf"))

    def search(self):
        self.t1.delete(*self.t1.get_children())
        s = "select * from appointment where doctorid='" + str(self.doctorid) + "' and date= '" + str(self.textbox1.get_date()) + "' and status ='confirmed'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        i = 0
        for row in result:
            self.t1.insert("", index=i, values=row)
            i = i + 1

    def __init__(self, email):
        self.root = Tk()
        self.root.config(background='#FFE4C4')
        self.doctorid = ""
        self.p1 = PanedWindow(self.root)
        self.p2 = PanedWindow(self.root)
        self.p3 = PanedWindow(self.root)
        self.p1.pack()
        self.p2.pack()
        self.p3.pack()
        self.bt2 = Button(self.p3, text="Generate PDF", command=self.generatepdf)
        self.bt2.grid(row=2, column=1)
        self.textbox1 = DateEntry(self.p1)
        self.textbox1.grid(row=0, column=2)
        self.lb1 = Label(self.p1, text="Select Appointment Date")
        self.lb1.grid(row=0,column=1)
        self.bt1 = Button(self.p1, text="Search", command=self.search)
        self.bt1.grid(row=0, column=3)

        self.t1 = Treeview(self.p2, column=("appointmentid", "pid", "name", "previoushistory", "doctorid", "date", "slotid", "amount", "typeofbooking","paymentrecieved", "token", "status", "diagnosis"))
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
        self.t1.column("appointmentid", width=100)
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
        s = "select * from doctors where email='" + email + "'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        self.doctorid = result[0]
        self.t1.pack()
        self.root.mainloop()
