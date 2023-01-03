from tkinter import *
from tkinter import messagebox
# create root container
root =Tk()
root.geometry('400x400+100+100')
fr1=Frame(root)
fr1.pack()
fr2=Frame(root)
fr2.pack()
butText=(('MC','M+','M-','MR'),
         ('C','+','/','X'),
         (7,8,9,'+'),
         (4,5,6,'-'),
         (1,2,3,'='),
         (0,'.'))
Entry(fr1).grid(row=0,column=0,pady=10)
for rindex,r in enumerate(butText):
    for cindex,text in enumerate(r):
        if text==0:
            Button(fr2, text=text).grid(row=rindex , column=cindex, sticky='NSWE',columnspan=2)
        elif text=='=':
            Button(fr2, text=text).grid(row=rindex, column=cindex , sticky='NSWE',rowspan=2)
        elif text=='.':
            Button(fr2, text=text).grid(row=rindex , column=cindex+1, sticky='NSWE')
        else:
            Button(fr2, text=text).grid(row=rindex , column=cindex, sticky='NSWE')

root.mainloop()