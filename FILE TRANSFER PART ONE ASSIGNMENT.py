import shutil
import os
import schedule
import time
from tkinter import *
from tkinter import filedialog

def file_transfer():
    source = e1.get()
    destination = e2.get()
    files = os.listdir(source)

    for i in files:
        shutil.move(source+i, destination)

    schedule.every().day.at("01:00").do(file_transfer)

    while True:
        schedule.run_pending()
        time.sleep(60) # wait one minute


root = Tk()
root.title('File Transfer')
root.geometry('450x450+500+300')
source = StringVar()
destination = StringVar()

def files():
    root.filename = filedialog.askdirectory()

b1 = Button(root, text="FOLDER OPEN", command = files)
b1.pack()
b2 = Button(root, text="FILE TRANSFER", command = file_transfer)
b2.pack()
l1 = Label(root,text='Put source directory below').pack()
e1 = Entry(root, textvariable=source)
e1.pack()
l2 = Label(root,text='Put destination directory below').pack()
e2 = Entry(root, textvariable=destination)
e2.pack()


