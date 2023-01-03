
from tkinter import *
from tkinter import messagebox
# 一、create a root container
root =Tk(className='menu')
root.geometry('500x500+100+200')

# 二、menu
# a.optionMenu
# v1: to store the value that is selected
v1=StringVar()
v1.set('video')
om=OptionMenu(root,v1,'basket','video','code')
om.place(relx=0.5,rely=0)
def showSelect():
    messagebox.showinfo(message=f'selected:{v1.get()}')
Button(root,text='comfirm',command=showSelect).place(relx=0.5,rely=0.1)
# 三、loop
root.mainloop()