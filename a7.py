from tkinter import *
from datetime import date

root = Tk()
root.title(" Getting started with Widgets ")
root.geometry("300x400")

lbl=Label(root, text=" Hey There!", fg = "White", bg = "#072F5F", height = 1, width = 300)

name_lbl = Label( text = "Full Name:", bg = "#CA7BD6")
name_entry = Entry()

def display():
    name = name_entry.get()
    
    global message
    message = "Welcome To The Application! \nToday's date is: " 
    greet = "Hello, " + name + "\n"
    
    text_box.insert(END, greet )
    text_box.insert(END, message )
    text_box.insert(END, date.today())
    
text_box = Text(height = 3)
    
btn = Button(text = "begin", command=display, height = 1, bg = "#DFDD6B", fg = "White")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
    