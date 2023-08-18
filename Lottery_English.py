#用rkinter写一个1-100抽签
from tkinter import *
import random

root = Tk()
root.title("1-100 Draw")
root.geometry("300x100")

def get_number():
    number = random.randint(1,100)
    print(number)
    label.config(text=number)

label = Label(root,text="")
label.pack()

button = Button(root,text="Draw",command=get_number)
button.pack()

root.mainloop()