
from tkinter import *
from tkinter import messagebox
# 一、create a root container
root =Tk(className='menu')
root.geometry('500x500+100+200')

# 二、menu
# a.scale
# 1.create a label for showing the value of scale
la1=Label(root,text='basket',bg='pink')
la1.place(relx=0.4,rely=0.45)
# 2.create a scale
def modifySize(value):
    newFont=('黑体',value)
    la1.config(font=newFont,text=f'basket\nsize:{value}')
# get value of scale via command.the scale will pass the value to command function
sc1=Scale(root,from_=0,to=100,length=200,tickinterval=10,orient=HORIZONTAL,command=modifySize)
sc1.place(relx=0.4,rely=0)
# 三、loop
root.mainloop()