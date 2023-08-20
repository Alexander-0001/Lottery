import tkinter as tk
import random

root = tk.Tk()
root.title('DRAW')
root.geometry('400x400')




def get_value():
    value = entry.get()
    a = value.split('-')
    if len(a) == 2:
        b = random.randint(int(a[0]),int(a[1]))
        sign_label.config(text=b)



signal = tk.Label(root,text='Please enter a range,Form: X-XXX :',font=('黑体',16))
signal.pack()

sign = tk.Label(root,text='Example: 1-100 1-50',font=('黑体',19))
sign.pack()

entry = tk.Entry(root,font=("黑体",30))
entry.pack()

sign = tk.Label(root,text="PlEASE ENTER THE SPECTFIED FORM",font=('黑体',18))
sign.pack()

get_sign_button = tk.Button(root,text='DRAW',font=("黑体",30),command=get_value)
get_sign_button.pack()

sign_label = tk.Label(root,text='',font=('黑体',70))
sign_label.pack()





root.mainloop()