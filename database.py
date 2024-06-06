#Imports utilised in the database functions
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
from datetime import datetime#used to append date to logfile
from matplotlib import *#matplotlib for plotting bar chart
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import os

'''
searches textfile and appends to list
returns list values to the tkinter frame as a label
'''
def searchdb(x, searching):
    b=0
    list = []
    f = open("database.txt", "r")
    for line in f.readlines(): 
        info = line.split()
        if searching in line:
            list.append(line)
    if list == []:
        Label(x, text = "No book found").pack()
        return
    
    else:
        for i in list:
            Label(x, text = i).pack()

'''
1st block - checks if a valid book ID has been inputted
2nd block - checks if books been checked out
            if not it appends details to list
3rd block - updates book details with students ID
4th block - appends new details to logbook
'''
def checkdb(x, id, bookid):
    nlist = []
    list = []
    f = open("database.txt", "r")
    lines = f.read().splitlines()
    last_line = lines[-1]
    list_lastline = last_line.split()
    lastID = int(list_lastline[0])
    if int(bookid)>lastID or int(bookid)<0:
        ms.showerror('Error!','Input a valid book ID')
        return
    f.close()



    f = open("database.txt", "r")
    for line in f.readlines():
        info = line.split()
        if int(bookid)==int(info[0]):         #info is details of a book in a list
            if info[5] == '!':          #the 5th item of the list stores who has the book
                list.append(line)
            else:
                ms.showerror('Error!','This Book has been checked out, try later')
                return
    f.close()



    #confirms id entered is valid
    if 1000<id<9999:
        w = open("database.txt", "r+")#read the lines and find where to replace
        for line in w:
            nline = line.strip()
            if bookid == nline[0:len(bookid)]:#searches the range from 0 to length of book
                nline = nline.replace('!', str(id))
            nlist.append(nline + '\n')#adds all the values to a list
        w.close()
        wr = open("database.txt", "w")
        for x in range (len(nlist)):
            wr.write(nlist[x])
        wr.close()

        #this code is for appending values to the log book
        log = open("logfile.txt", "a+")
        x = datetime.today().strftime('%d-%m-%Y')
        log.write(bookid+" ")
        log.write(x+"\n")
        ms.showinfo('Success!','Book Withdrawn Successfully')

'''
1st block - checks if book has already been returned
2nd block - outputs label saying what book is being returned
3rd block - reverts books details to being in libraries possesion
4th block - updates log file
'''
def returndb(x, returnentry):
    list = []
    f = open("database.txt", "r")
    for line in f.readlines(): # Read the lines
        info = line.split()
        if int(returnentry) == int(info[0]):#info is details of a book in a list
            if info[5] != '!':
                list.append(line)
            else:
                ms.showerror('Error!','This Book has already been \
returned, please check that you have entered correct book ID.')
                return
        
    f.close()
    Label(x, text = "You are returning:").pack()
    for i in list:
        Label(x, text = i).pack()#line containing book id

    w = open("database.txt", "r+")#read the lines and find where to replace
    nlist = []

    for line in w:
        nline = line.strip()
        info = line.split()
        lastelement = info[5].split()[-1]
        if returnentry == nline[0:len(returnentry)]:
            nline = nline.replace(lastelement, '!')


        nlist.append(nline + '\n')#adds all the values to a list
    w.close()
    wr = open("database.txt", "w")
    for x in range (len(nlist)):
        wr.write(nlist[x])#re-writes new and updated values to list
    wr.close()
    log = open("logfile.txt", "r+")
    x = datetime.today().strftime('%d-%m-%Y')                           #replace variables that have x
    loglist = []
    for line in log:
        nline = line.strip()
        info = line.split()
        if returnentry == nline[0:len(returnentry)]:
            if len(info) == 2:
                nline = (nline + " " + x)
        loglist.append(nline + '\n')#adds all the values to a list
    log.close()
    logw = open("logfile.txt", "w")
    for x in range (len(loglist)):
        logw.write(loglist[x])#re-writes new and updated values to list
    wr.close()
    ms.showinfo('Success!','Return Successful!')



'''
lists are used to store different parts of the textfile,
so that the data can be manipulated for the bar graph to be
based on book name rather than book copies



'''
def weeddb(x, screen):
    templist = []
    loglist = []
    idlist = []
    booknlist = []
    flist = []
    nlist = []

#This is appending book names to booknlist(not copies)
    with open("database.txt", "r") as readlog:
        for line in readlog:
            nline = line.strip()
            info = line.split()
            if info[2] in booknlist:
                pass
            else:
                booknlist.append(info[2])

    #find a way to append all id numbers that belong to the book name

    with open("database.txt", "r") as readlog2:
        for line in readlog2:
            info = line.split()
            templist.append(info)


    for k in templist:
        idlist.append(k[0])

    #for each id look through log files and see how many times the id appears in log file
    with open("logfile.txt", "r") as readrecords:
        for line in readrecords:
            info = line.split()
            loglist.append(info[0])

    #create a list of 0s equal to the amount of books there are
    for i in idlist:
        n = 0
        n = loglist.count(i)
        flist.append(n)

            

    
    for n in range(len(booknlist)):
        nlist.append(0)

    for i in booknlist:
        for k in templist:
            ind = (booknlist.index(i))
            if i == (k[2]):
                b = int(k[0])
                nlist[ind] = nlist[ind] + flist[(b)-1]           
    #use n list and booknlist for the matplotlib
#figsize=(5,4)
    f = Figure(figsize=(20,20))
    ax = f.add_subplot(111)


    ind = np.arange(len(booknlist))  # the x locations for the groups
    width = (len(booknlist)/20)

    ax.bar(booknlist, nlist, width)
    ax.set_ylabel('Checkouts')
    ax.set_xlabel('Books')

    canvas = FigureCanvasTkAgg(f, master=x)
    canvas.draw()
    canvas.get_tk_widget().pack()