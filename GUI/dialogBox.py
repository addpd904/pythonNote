
from tkinter import *
from tkinter import messagebox
# 一、create a root container
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askinteger

root =Tk(className='menu')
root.geometry('500x500+100+200')

# 二、dialog
# a.simple dialog
def getAge():
    # return the value that user input
    a=askinteger(title='input age',prompt='age',maxvalue=100)
    textA.insert(INSERT,f'age:{a}')
textA=Text(root,bg='pink')
textA.pack()
Button(root,text="input age",command=getAge).pack()
# a.simple dialog
# 三、message
def hint():
    value=showinfo(title='hint',message='welcome!')
    textA.insert(INSERT,f'value:{value}')
Button(root,text='hint',command=hint).pack()
root.mainloop()