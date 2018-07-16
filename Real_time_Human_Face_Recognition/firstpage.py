#import module from tkinter for UI
from Tkinter import *

import os
from a import *
from b import *
#creating instance of TK
root=Tk()

root.configure(background="#80D8FF")

#root.geometry("600x600")

def function1():
    
    os.system("python add.py")
    
    
    
def function2():
    #data=log_member()
    #tkMessageBox.showinfo(data[0],data[2])
    os.system("python log.py")
    
#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="SELECT YOUR OPTION",font=("helvatica",40),fg="white",bg="#00BFA5",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating a button
Button(root,text="Add Faces",font=("times new roman",30),bg="#3F51B5",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="For Attendance",font=("times new roman",30),bg="#3F51B5",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating quit button
Button(root,text="Exit",font=("times new roman",30),bg="#3F51B5",fg='white',command=root.quit).grid(row=5,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)


root.mainloop()
