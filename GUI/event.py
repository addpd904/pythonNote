# event loop(endless loop):to listen event
# <Button-1>:press left mouse button
# <KeyPress-a>:press key a
# <Alt-KeyPress-a>:press key a and Alt at the same time

from tkinter import *
# 一、create a root container and label
root=Tk(className='event practice')
root.geometry('500x500')
label1=Label(root,text='current:enent',bg="pink")
label1.place(rely=0,relx=0.40,height=60)
# 二、event
# a.bind
# 1.<B1-Motion>:drag
def drag(e):
    label1['text']=f'left mouse button drag\nx:{e.x}' \
                   f'\nx_root:{e.x_root}'
root.bind('<B1-Motion>',drag)
# 2.# < B1 - Motion >:left mouse button drag
def click(e):
    # x:reference system:root container
    # x_root:reference system:window
    label1['text']=f'left mouse button click\nnum:{e.num}\nx:{e.x}' \
                   f'\nx_root:{e.x_root}'
root.bind('<Button-1>',click)
# 3.<KeyPress>:press key
def pressKey(e):
    label1['text'] = f'press: {e.char}\nkeysym:{e.keysym}\nx:{e.x}' \
                     f'\nx_root:{e.x_root}'
root.bind('<KeyPress>',pressKey)
# b.property command; bind_class:
# 1.command
# shortcomings:no event object
def click1():
    # x:reference system:root container
    # x_root:reference system:window
    label1['text']=f'bind left click event via command'
Button(root,text='basket',command=click1).place(relx=0.5,rely=0.3)
# bind_class
def click2(e):
    label1['text']=f'bind right click event via bind_class\nnum:{e.num}\nx:{e.x}' \
                   f'\nx_root:{e.x_root}'
b2=Button(root,text='basket')
b2.place(relx=0.5,rely=0.5)
b3=Button(root,text='basket')
b3.place(relx=0.5,rely=0.7)
b2.bind_class('Button','<Button-3>',click2)
# 三、loop
root.mainloop()
