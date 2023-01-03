from tkinter import *
from tkinter import messagebox
# relx:relative coordinates; relwidth:relative width; x:absolute coordinate
# 一、create a root container
# className:set the window's name
root=Tk(className='place layout practice')
root['bg']='pink'
root.geometry('500x500+100+100')
f1=Frame(root,width=200,height=200,bg='blue')
# 二、place layout
f1.place(x=10,y=10)
# relx=0.5 means center
Button(root,text='basketball').place(relx=0.5,rely=0.5,relwidth=0.2,relheight=0.2)
Button(f1,text='tabletennis').place(x=0,y=0)

root.mainloop()

