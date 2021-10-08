import Grapher as GP
import Scraper as SP
import tkinter as tk
from tkinter import *

root = Tk()
root.title("Leaderboard Graph Generator")
root.minsize(800,450)

SD = tk.BooleanVar()
SD.set(False)

ZL = tk.BooleanVar()
ZL.set(False)

def push(rng):
	InfoBox.insert(END,rng)

def replace(rng):
    InfoBox.delete(1.0,END)
    InfoBox.insert(END,rng)

def replace(rng):
    InfoBox.delete(1.0,END)
    InfoBox.insert(END,rng)

def get():
	return [Index.get(), NumLen.get()]

def analyse(values, sd, zl):

	statsF = [sd, zl]

	x = SP.SCRAPE(values[0], values[1])

	"""
	x[0] is a dictionary with each username and rank,
	x[1] is the numbers of messages
	x[2] is the exp ranking
	x[3] is the title
	"""
	index  = x[0]
	msgDex = x[1]
	expDex = x[2]
	title  = x[3]

	GP.PLOT(x[0], x[1], x[2], x[3], statsF)


TITLE = Label(root,text="MEE6 Leaderboard Graph Generator",fg="#161648",bg="#fff",font="Arial 32 bold")
TITLE.place(relx=0.5,rely=0.1,anchor='center')

InfoBox = Text(root, width=46,height=8, bg="white", fg="black", font="Arial 14")
InfoBox.place(relx=0.5, rely=0.4, anchor='center')
InfoBox.insert(END,
"""Welcome to my program! By Mahir-Islam.
To use this, enter the server index and the number of
users you wish to analyse.

Warning: while this program does not provide with
constraints, it is not recommended that you index
more than 40 users."""
	)

Index = Entry(root, width=22, bg="white", fg="black", font="Arial 14")
Index.place(relx=0.335, rely=0.675, anchor='center')
Index.insert(END,"Server Code")

NumLen = Entry(root, width=22, bg="white", fg="black", font="Arial 14")
NumLen.place(relx=0.665, rely=0.675, anchor='center')
NumLen.insert(END,"Number of Users")

GENBTN = Button(root,text="Generate",bg="#ccc",fg='#222',font="Arial 30",borderwidth=0,command=lambda: push( analyse(list(map(int, get())) , SD.get(), ZL.get() )  ) )
GENBTN.place(relx=0.5,rely=0.85,anchor='center')

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
menubar = Menu(root)

"""
filemenu = Menu(menubar, tearoff=0) #File
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu) #File

editmenu = Menu(menubar, tearoff=0)  #Edit
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu) #Edit

helpmenu = Menu(menubar, tearoff=0) #Help
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu) #Help
"""

analysis = Menu(menubar, tearoff=0) #Analysis

analysis.add_checkbutton(label="Standard Deviation", onvalue=1, offvalue=0, variable=SD)
analysis.add_checkbutton(label="Zipf's Law", onvalue=1, offvalue=0, variable=ZL)
menubar.add_cascade(label="Analysis", menu=analysis)

aboutmenu = Menu(menubar, tearoff=0) #About
aboutmenu.add_command(label="Source Code", command=donothing)
menubar.add_cascade(label="About", menu=aboutmenu) #Help

root.config(menu=menubar)

root.mainloop()