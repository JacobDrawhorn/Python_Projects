import shutil
import os
import schedule
import time
from datetime import datetime, timedelta
from tkinter import *
from tkinter import filedialog

def file_transfer():
    source = e1.get()
    destination = e2.get()
    files = os.listdir(source)
    for i in files:
        if os.path.getmtime(i) <= timedelta(1).total_seconds():
            shutil.move(source+ '/' + i, destination)

root = Tk()
root.title('File Transfer')
root.geometry('450x450+500+300')
source = StringVar()
destination = StringVar()

def folder1():
    folder = root.filename = filedialog.askdirectory()
    if folder is not None:
        e1.insert(END, folder)

def folder2():
    folder = root.filename = filedialog.askdirectory()
    if folder is not None:
        e2.insert(END, folder)

b1 = Button(root, text="SELECT SOURCE FOLDER", command = folder1)
b1.pack()
b2 = b1 = Button(root, text="SELECT DESTINATION FOLDER", command = folder2)
b2.pack()
b3 = Button(root, text="INITIATE FILE TRANSFER", command = file_transfer)
b3.pack()
l1 = Label(root,text='Source path below').pack()
e1 = Entry(root, textvariable=source)
e1.pack()
l2 = Label(root,text='Destination path below').pack()
e2 = Entry(root, textvariable=destination)
e2.pack()

root.mainloop()




