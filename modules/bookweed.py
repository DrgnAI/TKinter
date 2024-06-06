from tkinter import *
from tkinter import ttk
from database import *



def weedfunc(x, screen):
    Button(x, text = "Weed Book Chart",height = "2", width = "30", command = weeddb(x, screen)).pack()


if __name__ == "__main__":
    x = Tk()
    pad = 3
    program = ttk.Notebook(x)
    program.pack()
    weed = Frame(program, width=(x.winfo_screenwidth()-pad), height = (x.winfo_screenheight()-pad))
    program.add(weed, padding=[12, 12], text="Weed out a Book")
    weed.pack(fill="both", expand=1)
    weedfunc(weed, x)
    x.mainloop()