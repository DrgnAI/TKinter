from tkinter import *
from tkinter import ttk
from database import *#database functions are imported for use
from tkinter import messagebox as ms

'''
Global variable is used so that it can be used in this function to get
past the problem of errors with the button functions handling of parameters
the entry returns nothing to the function otherwise
'''

list2 = []

def check(x):
    global identry
    global bookidentry
    bookidentry = StringVar()
    identry = StringVar()
    list2.append(x)
    Label(x, text = "What is your ID number:").pack()
    Label(x, text = "").pack()
    Label(x, text = "").pack()
    Entry(x, textvariable = identry).pack()
    Label(x, text = "").pack()
    Label(x, text = "Please enter the ID of the book you are checking out:").pack()
    Label(x, text = "").pack()
    Label(x, text = "").pack()
    Entry(x, textvariable = bookidentry).pack()
    Label(x, text = "").pack()
    Button(x, text = "Checkout Book",height = "2", width = "30", command = b).pack()


'''
these items are appended to the list so they can be used in the respective
database function
'''
def b():
    global identry
    global bookidentry
    try:
        int(identry.get())
    except:
        ms.showerror('Error!','Invalid ID, try again')
        return
    if 1000<int(identry.get())<9999:
        list2.append(identry.get())
        list2.append(bookidentry.get())
        checkdb(list2[0], (int(list2[1])), (list2[2]))
        del list2[-1]
        del list2[-1]
    else:
        ms.showerror('Error!','Invalid ID, try again')



if __name__ == "__main__":
    x = Tk()
    check(x)
    x.mainloop()