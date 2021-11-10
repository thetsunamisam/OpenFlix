from openflix import *

print("Welcome to Openflix CLI Edition")
mode = input("Upload to server or download(u/d)")
if mode == "u":
    localDir = input("File you would like to send>")
    #remoteDir = input("Location on database (leave blank for default)>") 
    print("Uploading file to server...")
    send = Up()
    send.upload(clientDir = localDir, remoteDir="/home/zorg/openflix.py")
elif mode == "d":
    title = input("Input Title Name(Case Sensetive> ")
    title2 = title.replace(" ", "")
    titleFormated = str("/home/zorg/"+title2+".mp4")
    localDir = input("Save title to this directory>")
    recv = Down()
    recv.download(clientDir = localDir, remoteDir = titleFormated)
else:
    print("No joy, you put something in wrong")
