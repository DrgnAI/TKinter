from tkinter import *
from tkinter import ttk
from database import *


list1 = []

def searchfunc(x):
    global searchentry
    searchentry = StringVar()
    list1.append(x)
    Label(x, text = "Search using keyword like book name or author\
(use _ instead of spaces and include capital letters where needed):").pack()
    Label(x, text = "").pack()
    Label(x, text = "").pack()
    Entry(x, textvariable = searchentry).pack()
    Label(x, text = "").pack()
    Button(x, text = "Search!",height = "2", width = "30", command = b).pack()


def b():
    global searchentry
    list1.append(searchentry.get())#Global variable is used so that it can be used in this function to get past the problem of errors with the button functions handling of parameters
    searchdb(list1[0], list1[1])
    del list1[-1]




if __name__ == "__main__":
    x = Tk()
    searchfunc(x)
    x.mainloop()