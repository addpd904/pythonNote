# layout manager
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('500x500+400+200')
root.iconbitmap(r'E:\programme\Python\practice\others\app.ico')
but1=Button(root)
but1['text']='first button'
# pack() is a layout
but1.pack()
def clickfun(e):
    messagebox.showinfo('message','the button was clicked')
but1.bind('<Button-1>',clickfun)
# mainloop(): event loop(while ,to listen the operation of user)
root.mainloop()