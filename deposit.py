"""
Import modules tkinter sqlite3 datetime
"""
import tkinter.messagebox
from tkinter import *
import sqlite3
import datetime

"""
Import gui module
"""
from gui import *



"""
Class deposit
For deposit money

"""
class Deposit:
    def gui(self):
        if (self.e1.get()):
            db = sqlite3.connect("samp1.db") # Database connection
            c = db.cursor() # Cursor
            z = eval(self.e1.get()) # Get database
            id = self.id
            list1 = [(id)]
            c.execute("select * from Bank3 where id=?", list1)
            result_1 = c.fetchall()
            a = result_1[0][3] + z
            today = datetime.date.today() # Get today datetime
            list4 = [(a, str(today), id)]
            c.executemany("update Bank3 set bal=?,date1=? where id=?", list4) # Update query
            db.commit()
            tkinter.messagebox.showinfo("Deposit", "You have successfully deposited")
            self.root.destroy()
        else:
            tkinter.messagebox.showinfo("Error", "Please Enter the amount")

    def __init__(self, id): # Gui __init__
        self.id = id
        self.root = Tk()
        self.root.title("The State Bank of Turkey")
        self.root.geometry("600x400+300+165")
        self.root.resizable(width=False, height=False)
        self.root.configure(bg="cyan")
        l1 = Label(self.root, text="Enter the Amount  :  ", bd=1, width=18, padx=10,
                   font="Times 20 bold", height=3, bg="cyan")
        l1.grid(row=1, column=0)
        self.e1 = Entry(self.root, bd=5, font="Times 18 bold", bg="yellow")
        self.e1.focus()
        self.e1.grid(row=1, column=1)

        b1 = Button(self.root, text="Deposit", font="Times 20 bold", bd=15, width=15, height=1,
                    justify="right", relief='ridge', bg="green", activebackground="blue", command=lambda: self.gui())
        b1.grid(row=2, column=1)

        self.root.mainloop() # Main tkinter loop
