from tkinter import *

root = Tk()


"""def printName():
    print("Chello my name is Aryan")"""

"""button_1 = Button(root, text="Print my name", command=printName)"""  # command=start function
def printName(event): #event=click,scroll,etc..
    print("Chello my name is Aryan")

button_1 = Button(root, text="Print my name",)
button_1.bind("<Button-1>", printName) #<Button-1>=left clcik on mouse

root.mainloop()
