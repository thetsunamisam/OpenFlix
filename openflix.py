import os
import time
import math
from paramiko import *
from scp import *
ip  = "cellcraft.us.to" 
client = SSHClient()
print("Loading Keys")
client.load_system_host_keys()
client.connect(hostname='cellcraft.us.to',port=55892,username="zorg")
print("Connected to " + ip)
stdin, stdout, standerr = client.exec_command('ls')
lineout = stdout.readlines()
for items in lineout:
    print (items)
class Up():
    def __init__(self):
        pass
    def upload(self, clientDir, remoteDir):
        print("Uploading movie to database")
        scp = SCPClient(client.get_transport())
        scp.put(clientDir, recursive=True, remote_path=remoteDir)
        print("Done.\n" + clientDir + " sent to " + remoteDir)
        scp.close()
class Down():
    def __init__(self):
        pass
    def download(self, clientDir, remoteDir):
        scp = SCPClient(client.get_transport())
        scp.get(remoteDir, local_path = clientDir, recursive=True)
        title = remoteDir.replace("/home/zorg/","")
        print("Downloading " + title + " from database")
        scp.close()
class Command():
    def __init__(self):
        pass
    def list(self):
        print("test test")
        client = SSHClient()
        print("Loading Keys")
        client.load_system_host_keys()
        client.connect(hostname='cellcraft.us.to',port=55892,username="zorg")
        print("Connected to " + ip)
        stdin, stdout, standerr = client.exec_command("ls -l -h /media/zorg/'Big Chungus'/Movie_Database")
        lineout = stdout.readlines()
        for items in lineout:
            print (items)

#send = Up()
#send.upload(clientDir = "openflix.py", remoteDir = "/home/zorg")
#recv = Down()
#recv.download(clientDir = "/home/sam/Desktop", remoteDir = "/home/zorg/openflix.py")
