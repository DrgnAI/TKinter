from tkinter import *
from tkinter import ttk
from database import *

list3 = []

def returnfunc(x):
    global returnentry
    returnentry = StringVar()
    list3.append(x)
    Label(x, text = "What is the ID of the book you're returning:").pack()
    Label(x, text = "").pack()
    Label(x, text = "").pack()
    Entry(x, textvariable = returnentry).pack()
    Label(x, text = "").pack()
    Button(x, text = "Return Book",height = "2", width = "30", command = b).pack()



def b():
    global returnentry
    list3.append(returnentry.get())#Global variable is used so that it can be used in this function to get past the problem of errors with the button functions handling of parameters
    returndb(list3[0], list3[1])
    del list3[-1]



if __name__ == "__main__":
    x = Tk()
    returnfunc(x)
    x.mainloop()