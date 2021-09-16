from tkinter import *
import webbrowser

def wbbrowser():
    text = wbEntry.get()
    f = open('index.html','w')
    message_p1 = "<html><head></head><body><h1>"
    message_p2 = "</h1></body</html>"
    message = message_p1 + text + message_p2
    f.write(message)
    f.close()
    webbrowser.open_new_tab('index.html')

wbGui = Tk()
source = StringVar()

wbGui.geometry('450x450+500+300')
wbGui.title('Web Browser')

wblabel = Label(wbGui,text='Type Your Text Below').pack()

wbbutton = Button(wbGui,text="Open Browser",command = wbbrowser).pack()

wbEntry = Entry(wbGui,textvariable=source)
wbEntry.pack()
