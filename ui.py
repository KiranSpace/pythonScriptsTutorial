from tkinter import *
root = Tk()
var = StringVar()
label = Label(root,textvariable=var,relief=RAISED)
var.set("GOOD MORNING!!! HAW ")
label.pack()
root.mainloop()
