
from tkinter import *
from tkinter import messagebox
# 一、create a root container
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile

root =Tk(className='menu')
root.geometry('500x500+100+200')

# 二、menu
# a.color box
def creratColorBox():
    # return a tuple that include selected color.like ((255, 192, 203), '#ffc0cb')
    c1:tuple=askcolor(color='pink',title='colorBox practice')
    print(c1)
    # config:configure the parameter of window
    root.config(bg=c1[1])
Button(root,text='select color for window',command=creratColorBox).place(relx=0.25,rely=0)
# b.file box
# caution:there are many functions.see the document for details
text_area=Text(root,bg='pink')
text_area.place(relx=0,rely=0.5)
def openText():
    # return a file object.
    f1=askopenfile(title='filebox practice',initialdir='e:/',filetypes=[('text file','.txt')])
    text_str:str=f1.read()
    # INSERT:insert from first line
    text_area.insert(INSERT,text_str)
Button(root,text='select a text file',command=openText).pack()
# 三、loop
root.mainloop()