from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser

root = Tk(className= 'WORKSTATION STARTUP')
root.geometry("500x500")

##FONTS

def hwOpen():
    webbrowser.open_new('https://learning.fresno.edu/my/')

hw = Button(root, fg='white', bg='green', bd=15, anchor=CENTER, relief=RAISED, text="HOMEWORK", font=("Impact",25), command=hwOpen)
hw.pack()

L = Label(root, anchor=CENTER, relief=RAISED, font=("Impact",25), text="Will we be doing work?")
L.pack()

root.mainloop()