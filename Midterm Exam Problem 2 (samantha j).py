from tkinter import *

class MyWindow:
    def __init__(self, win):

        self.lbl1 = Label(win, text = "Enter Given Name:")
        self.lbl1.place(x =100, y = 50)

        self.lbl2 = Label(win,text = "Enter Middle Name:")
        self.lbl2.place(x=100,y=75)

        self.lbl3 = Label(win,text = "Enter Last Name:")
        self.lbl3.place(x=100,y=100)

        self.lbl3 = Label(win, text="My Full Name is:")
        self.lbl3.place(x=100, y=150)

        self.lbl4 = Label(win, text="My Full Name")
        self.lbl4.place(x=180, y=25)

        self.txt1 = Entry(win , bd = 2)
        self.txt1.place(x = 225, y = 50)

        self.txt2 = Entry(win, bd= 2)
        self.txt2.place(x = 225, y = 75)

        self.txt3 = Entry(win, bd = 2)
        self.txt3.place(x = 225, y = 100)

        self.nm = Entry(win, bd = 2)
        self.nm.place(x = 225, y = 150)

        self.btnadd = Button(win, text = "Show Full Name:")
        self.btnadd.place(x = 180, y = 200)
        self.btnadd.bind('<Button-1>', self.add)


    def add(self, add):

        self.nm.delete(0, 'end')
        num1 = str(self.txt1.get())
        num2 = str(self.txt2.get())
        num3 = str(self.txt3.get())
        result = num1 + " " + num2 + " " + num3
        self.nm.insert(END, str(result))


window = Tk()
mywin = MyWindow(window)
window.geometry("500x300+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()