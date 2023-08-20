import tkinter as tk
import random

root = tk.Tk()
root.title('抽签')
root.geometry('400x300')




def get_value():
    value = entry.get()
    a = value.split('-')
    if len(a) == 2:
        sign = random.randint(int(a[0]),int(a[1]))
        sign_label.config(text=sign)



signal = tk.Label(root,text='请输入一个范围，格式: X-XX :',font=('黑体',20))
signal.pack()

sign = tk.Label(root,text='例: 1-100 1-50',font=('黑体',20))
sign.pack()

entry = tk.Entry(root,font=("黑体",30))
entry.pack()

sign = tk.Label(root,text="请输入要求格式",font=('黑体',20))
sign.pack()

get_sign_button = tk.Button(root,text='抽签',font=("黑体",30),command=get_value)
get_sign_button.pack()

sign_label = tk.Label(root,text='',font=('黑体',70))
sign_label.pack()





root.mainloop()