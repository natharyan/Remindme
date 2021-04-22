from tkinter import *
from tkinter import Label

root = Tk()
root.title("Draw Yourself!")
root.geometry("1000x1000")
root.configure(bg='red')

def moveup(e):
    global i

    label1 = Label(root, text="*",bg="red")
    l.append(label1)

    l[i].place(x=l[i - 1].winfo_x(), y=l[i - 1].winfo_y() - 15)

    i = i + 1

def movedown(e):
    global i
    label1 = Label(root, text="*",bg="red")
    l.append(label1)
    l[i].place(x=l[i - 1].winfo_x(), y=l[i - 1].winfo_y() + 15)

    i += 1

def moveleft(e):
    global i
    label1 = Label(root, text="*",bg="red")
    l.append(label1)
    l[i].place(x=l[i - 1].winfo_x() - 15, y=l[i - 1].winfo_y())

    i += 1

def moveright(e):
    global i
    label1 = Label(root, text="*",bg="red")

    l.append(label1)
    l[i].place(x=l[i - 1].winfo_x() + 15, y=l[i - 1].winfo_y())

    i += 1

    #i-1 index in list take value
    #append label inside list
i=0
root.bind("<Up>", moveup)
root.bind("<Down>", movedown)
root.bind("<Left>", moveleft)
root.bind("<Right>", moveright)

l=[]
root.mainloop()


#piano
#mental health quiz
#hangman
