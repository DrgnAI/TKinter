'''
All of the imports listed below
'''
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import sys

sys.path.append('\Tkinter Submission\modules')
import modules.booksearch
import modules.bookcheckout
import modules.bookreturn
import modules.bookweed

'''
Creation of tkinter screen and frames
'''
screen = Tk()
pad=3
screen.title("Library Management System")
screen.geometry(("{0}x{1}+0+0".format(
        screen.winfo_screenwidth()-pad, screen.winfo_screenheight()-pad)))

searchentry = StringVar()

program = ttk.Notebook(screen)
program.pack()

mainmenu = Frame(program, width=(screen.winfo_screenwidth()-pad), height = (screen.winfo_screenheight()-pad))
search = Frame(program, width=(screen.winfo_screenwidth()-pad), height = (screen.winfo_screenheight()-pad))
checkout = Frame(program, width=(screen.winfo_screenwidth()-pad), height = (screen.winfo_screenheight()-pad))
returnbk = Frame(program, width=(screen.winfo_screenwidth()-pad), height = (screen.winfo_screenheight()-pad))
weed = Frame(program, width=(screen.winfo_screenwidth()-pad), height = (screen.winfo_screenheight()-pad))


mainmenu.pack(fill="both", expand=1)
search.pack(fill="both", expand=1)
checkout.pack(fill="both", expand=1)
returnbk.pack(fill="both", expand=1)
weed.pack(fill="both", expand=1)

program.add(mainmenu, padding=[12, 12], text="Main Menu")
program.add(search, padding=[12, 12], text="Search")
program.add(checkout, padding=[12, 12], text="Checkout a Book")
program.add(returnbk, padding=[12, 12], text="Return a Book")
program.add(weed, padding=[12, 12], text="Weed out a Book")

'''
This is for the quit button
'''
def quitfunc():
        screen.destroy()


'''
These are the functions being imported into each frame
'''
fontStyle = tkFont.Font(family="Arial", size=50)
fontStyle2 = tkFont.Font(family="Arial", size=30)
welcome = Label(mainmenu,  text = "Welcome To The Library Management System!", font=fontStyle).pack()
mainpromt = Label(mainmenu,  text = "Please navigate through the program using the tabs above.", font=fontStyle2).pack()
quit = Button(mainmenu, text = "Quit",height = "5", width = "30", command = quitfunc).pack()
searchlabel = modules.booksearch.searchfunc(search)
checklabel = modules.bookcheckout.check(checkout)
returnlabel = modules.bookreturn.returnfunc(returnbk)
weedlabel = modules.bookweed.weedfunc(weed, screen)


if __name__ == "__main__":
    screen.mainloop()