from tkinter import *
from openflix import *
from tkinter import filedialog
root = Tk()
this = Command()
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
    root.message.showinfo(root, text="Scan results are in the terminal output for now sorry"
    this.list()
browseButton = Button(root, text="Browse", command = getpath)
saveButton =  Button(root,text="Save to", command=getdir)
scanButton = Button(root, text='Scan', command=scan)
browseButton.pack()
saveButton.pack()
scanButton.pack()
root.mainloop()

