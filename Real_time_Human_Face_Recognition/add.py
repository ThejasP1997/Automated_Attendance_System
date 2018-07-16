from pynput.keyboard import Key, Listener
from a import *
from db import *
from myftp import *
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

ftp_files=list_files()
for file in ftp_files:
   if not os.path.exists("./human_faces2/"+file):
		download_from_ftp(file)

root=Tk()

root.title("enter details")

root.configure(bg="#D7CCC8")

root.focus_set()

num=0;

def enter_the_value():

    name=e1.get()
    pid=e2.get()
    conn = mysql.connector.connect(host=my_host,database=my_database,user=my_user,password=my_password)
    cursor = conn.cursor()
    cursor.execute("select id from members;")
          
    a=add_member(name,pid)
    
    if(a==0):
          tkMessageBox.showinfo('Successful','Member Added Successfully....!!!')
    if(a==-1):
          tkMessageBox.showerror('Failed','Duplicate Entry....Member Not Added..!')
    if(a==-2):
          tkMessageBox.showerror('Error','Face Not Detected..!')
root.destroy
    

if __name__=="__main__":

    Label(root,text="ENTER THE DETAILS", fg='white', bg='#424242' ,font=("helvetica",40),width=23).grid(rowspan=2,columnspan=3,sticky=E+W+N+S,padx=5,pady=5)

    Label(root, text="Enter Name: ",font=("helvetica ",30),fg='#212121',bg="#D7CCC8").grid(row=2,sticky=E,column=0)

    Label(root, text="Enter UID: ",font=("helvetica ",30),fg='#212121',bg="#D7CCC8").grid(row=3,sticky=E,column=0)

    e1=Entry(root)

    e2=Entry(root)

    e1.grid(row=2,column=1,columnspan=2,sticky=W)

    e2.grid(row=3,column=1,columnspan=2,sticky=W)

    Button(root,text="Exit",font=("times new roman",30), fg="white",bg="#3E2723",command=root.quit).grid(row=4,column=0, pady=10,padx=10,sticky=E+W+N+S)

    Button(root,text="ENTER",font=("times new roman",30), fg="white",bg="#3E2723",command=enter_the_value).grid(row=4,column=1,pady=10,padx=10,sticky=E+W+N+S)

    #Label(root, text="total number of faces detected are: ",fg="#212121",bg="#607D8B",font=(10)).grid(row=5,column=0,sticky=E)
    
    #Label( root, textvariable=var1,fg="#000000",font=(10)).grid(row=5,column=1)

    #Button(root,text="NEXT",width=5,height=3,command=run_command).grid(row=6,columnspan=2)
root.destroy
root.mainloop()


	
	
        
