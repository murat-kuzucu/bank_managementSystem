import datetime
import sqlite3
import tkinter.messagebox
from tkinter import *


class Withdraw:
    def __init__(self, ID):
        self.ID = ID
        self.root = Tk()
        self.root.title("The State Bank of Turkey")
        self.root.geometry("600x400+300+165")
        self.root.resizable(width=False, height=False)
        self.root.configure(bg="cyan")
        l1 = Label(self.root, text="Enter the Amount  :  ", bd=1, width=18, padx=10,
                   font="Times 20 bold", height=3, bg="cyan")
        l1.grid(row=1, column=0)
        self.e1 = Entry(self.root, bd=5, font="Times 18 bold", bg="yellow")
        self.e1.grid(row=1, column=1)
        self.e1.focus()
        b1 = Button(self.root, text="Withdraw", font="Times 18 bold", bd=15, width=15, height=1,
                    justify="right", relief='ridge', bg="green", activebackground="blue", command=self.gui_1)
        b1.grid(row=2, column=1)
        self.root.mainloop()

    def gui_1(self):
        if (self.e1.get()):
            db = sqlite3.connect("bank.db")
            c = db.cursor()
            ID = self.ID
            list1 = [(ID)]
            c.execute("select * from ACCOUNT where ID=?", list1)
            result2 = c.fetchall()
            z2 = eval(self.e1.get())
            if (result2[0][3] > z2):
                a2 = result2[0][3] - z2
                today = datetime.date.today()
                list3 = [(a2, str(today), ID)]
                c.executemany("update ACCOUNT set Balance=?,date1=? where ID=?", list3)
                db.commit()
                tkinter.messagebox.showinfo("Withdraw", "You have successfully withdraw ")
                self.root.destroy()
            else:
                answer = tkinter.messagebox.askokcancel("Withdraw",
                                                        "You don't have sufficient balance.")
                if (not (answer == True)):
                    self.root.destroy()
                else:
                    self.e1.delete(0, 'end')
        else:
            tkinter.messagebox.showinfo("Error", "Please Enter the amount")