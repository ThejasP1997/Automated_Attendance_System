from pynput.keyboard import Key, Listener
from a import *
import time
from b import *
import re
import sys
from pynput.keyboard import Key, Listener
from myftp import *
from Tkinter import *
import tkMessageBox


import os
if not os.path.exists("human_faces1"):
    os.makedirs("human_faces1")
if not os.path.exists("human_faces2"):
    os.makedirs("human_faces2")

root=Tk()
while True:
	ftp_files=list_files()
	for file in ftp_files:
		if not os.path.exists("./human_faces2/"+file):
			download_from_ftp(file)
		
        print("---------------")
        data=log_member()
        tkMessageBox.showinfo(data[1],data[2])
        
        time.sleep(5)
	print("---------------")
	    
	
	
