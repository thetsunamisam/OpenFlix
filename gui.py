from tkinter import *
from openflix import *
root = Tk()
root.title("OpenFlix\nBy Sam Francis")
def send():
    sendMovie = Up()
    sendMovie.send(clientDir=client)
sendLabel = Label(text="Send", command=send)
root.mainloop()

