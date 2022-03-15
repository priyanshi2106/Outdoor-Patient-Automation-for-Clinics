from tkinter import *
from tkinter.messagebox import*
from connection import *
from tkinter .ttk import*
from pymysql import*


class addslots:

    def display(self):

        if self.ans1.get()==1:
            self.lst[0] = "yes"

        if self.ans2.get()==1:
            self.lst[1] = "yes"

        if self.ans3.get()==1:
            self.lst[2] = "yes"

        if self.ans4.get()==1:
            self.lst[3] = "yes"

        if self.ans5.get()==1:
            self.lst[4] = "yes"

        if self.ans6.get()==1:
            self.lst[5] = "yes"

        if self.ans7.get()==1:
            self.lst[6] = "yes"


        print(self.ans1.get())
        print(self.ans2.get())
        print(self.ans3.get())
        print(self.ans4.get())
        print(self.ans5.get())
        print(self.ans6.get())
        print(self.ans7.get())


        s = "insert into slot values (NULL,'" + self.textbox1.get(0.0, END) + "','" + str(self.cb2.get()) + "','" + self.lst[0] + "','" + self.lst[1] + "','" + self.lst[2] + "','" + self.lst[3] + "','" + self.lst[4] + "','" + self.lst[5] + "','" + self.lst[6] + "','"+str(self.cb1.get())+"')"
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        showinfo("", "Slot Added Successfully")

    def __init__(self):

        self.root = Tk()
        self.root.config(background='#FFE4C4')
        self.lst = ["no", "no", "no", "no", "no", "no", "no"]
        self.root.geometry("1000x600")
        self.ans1 = IntVar()
        self.ans2 = IntVar()
        self.ans3 = IntVar()
        self.ans4 = IntVar()
        self.ans5 = IntVar()
        self.ans6 = IntVar()
        self.ans7 = IntVar()

        s = "select * from doctors"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        x = []
        for row in result:
            x.append(row[0])

        self.lb2 = Label(self.root, text="Add Slots")
        self.lb2.grid(row=0, column=1)
        self.lb1 = Label(self.root, text="select doctor id")
        self.cb1 = Combobox(self.root, values = x, state = "readonly" )
        self.cb1.grid(row=1, column=1)

        self.lb3 = Label(self.root, text="Slot Detail")
        self.lb4 = Label(self.root, text="Maximum Capacity")
        self.textbox1 = Text(self.root, height = 2)
        self.textbox1.grid(row=2, column=1)
        self.cb2 = Combobox(self.root, values = ("1", "2", "3", "4", "5", "6", "7", "8", "9" ,"10", "11", "12", "13", "14", "15"),state="readonly")
        self.cb2.grid(row=3, column=1)
        self.lb1.grid(row=1, column=0)
        self.lb3.grid(row=2, column=0)
        self.lb4.grid(row=3, column=0)

        self.ch1 = Checkbutton(self.root, text="Monday", variable=self.ans1)
        self.ch2 = Checkbutton(self.root, text="Tuesday", variable=self.ans2)
        self.ch3 = Checkbutton(self.root, text="Wednesday", variable=self.ans3)
        self.ch4 = Checkbutton(self.root, text="Thursday", variable=self.ans4)
        self.ch5 = Checkbutton(self.root, text="Friday", variable=self.ans5)
        self.ch6 = Checkbutton(self.root, text="Saturday", variable=self.ans6)
        self.ch7 = Checkbutton(self.root, text="Sunday", variable=self.ans7)
        self.bt1 = Button(self.root, text="Add", command=self.display)

        self.ch1.grid(row=4, column=0)
        self.ch2.grid(row=4, column=1)
        self.ch3.grid(row=5, column=0)
        self.ch4.grid(row=5, column=1)
        self.ch5.grid(row=6, column=0)
        self.ch6.grid(row=6, column=1)
        self.ch7.grid(row=7, column=0)
        self.bt1.grid(row=8, column=1)

        self.root.mainloop()
