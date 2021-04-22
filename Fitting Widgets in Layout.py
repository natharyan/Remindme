from tkinter import *

root = Tk()

one = Label(root, text="One", bg="red", fg="white") #bg- background of label #fg- foreground/ colour of font in label
one.pack() #about 60 pixels wide
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X) #grows in x-diection when expanding window
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT,fill=Y)
root.mainloop()

