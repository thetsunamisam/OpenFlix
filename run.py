'''to do
add shell interface
send
revc
list
auto'''
from openflix import *
import openflix as flix
from tkinter import *
import tkinter as ttk
import paramiko
from tkinter.scrolledtext import ScrolledText
root = Tk()
do = Command()
shell_output = str(do.list()) 
shell = Text(root, height = 24 , width = 80)
shell.insert(ttk.END, shell_output)
shell.pack()
root.mainloop()
