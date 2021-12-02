
import threading
import os
import time
import math
from paramiko import *
from scp import *
hostname  ='cellcraft.us.to' 
ip = hostname
client = SSHClient()
print("Loading Keys")
client.load_system_host_keys()
client.connect(hostname=hostname,port=55892,username="zorg")
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
        remoteDirClean = remoteDir.replace(' ', '')
        scp.get("/home/zorg/Movie_Database/Movie_Database/" + remoteDirClean+".mp4", local_path = clientDir, recursive=True)
        title = remoteDir.replace("/home/zorg/","")
        print("Downloading " + title + " from database")
        scp.close()
class Command():
    def __init__(self):
        pass
    def list(self):
        client = SSHClient()
        print("Loading Keys and mounting disks\nThe may take sometime if they arent spinning yet")
        client.load_system_host_keys()
        client.connect(hostname=hostname ,port=55892,username="zorg")
        print("Connected to " + ip)
        stdin, stdout, standerr = client.exec_command("ls -l -h /home/zorg/Movie_Database/Movie_Database/")
        lineout = stdout.readlines()
        for items in lineout:
            print (items)
        return lineout
    def listupdate(self,rate):
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(hostname=hostname, port=55892, username='zorg')
        stdin, stdout, standerr = client.exe_command('while sleep 1; do ll -l -h/home/zorg/Movie_Database/Movie_Database/; done')
    def search(self):
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(hostname=hostname) 
class Debug():
    def __init__(self):
        pass
    def probe(self):
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(hostname = hostname, port=port, username = username)
        stdin, stdout, stdanderr = client.exe_command('./probe-test')
    def netstat(self):
        print("Running network tests...")
        
      
