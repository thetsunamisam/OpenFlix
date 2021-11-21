import os
import subprocess
from tkinter import *
from openflix import *
import openflix as flix
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
root = Tk()
do = Command()
root.title("OpenFlix\nBy Sam Francis")
def send():
    sendMovie = Up()
    sendMovie.send(clientDir=client)
def getpath():
    print("guerilla debug")
    savemode = "Directory"
    #if mode == True:
        #savemode = 'Choose File to upload'
        #return savemode
    #else:
       # savemode = 'Choose Directory to save file' 
    path = filedialog.askopenfilename(initialdir='/',title = savemode ,filetypes=[("All files", "*.*")])
    return path
def getdir():
    savedir = filedialog.askdirectory()
    os.chdir(str(savedir))
    return savedir
    print('Moving to save directory\n'+str(savedir)+ ('\n(In the future saving will not require moving the entire working directory!)'))
def scan():
    titleList = do.list()
    #preclean = titleList.replace("'","")
    #titleListCleanSoon = preclean.replace("[","")
    #titleListClean = titleListCleanSoon.replace("]","")
    scanbox = Tk()
    titles = Label(scanbox, text=titleList)
    titles.pack()
    scanbox.mainloop()
    tk.messagebox.showinfo(root, message="Scan results are in the terminal output for now sorry")
def close():
    exit()
def start():
    print('starting transfer...')
    rd = titleEntry.get()
    tk.messagebox.showinfo(root, message="After you close this window the download start.\nThis program only runs on one process so the program will appear to freeze\nthis is expected behaviour. When the download is finished another message will appear")
    flix.Down().download(os.getcwd(), rd)
    root.after(1000, start)
    tk.messagebox.showinfo(root, message="Downloaded "+ rd + " to " + os.getcwd())
    print("if you get an error here you need to selelect a directory to save to")
titleEntry = Entry(root)
titleLabel = Label(root,text="Title\n(case sensitive)")
browseButton = Button(root, text="Browse", command = getpath)
saveButton =  Button(root,text="Save to", command=getdir)
scanButton = Button(root, text='Scan', command=scan)
startButton = Button(root, text='Start Download', bg="green", command=start)
quit = Button(root, text= "Quit", command=close)
titleLabel.pack()
titleEntry.pack()
browseButton.pack()
saveButton.pack()
scanButton.pack()
startButton.pack()
quit.pack()
root.mainloop()

