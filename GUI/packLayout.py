from tkinter import *
from tkinter import messagebox
# create root container
root =Tk()
# set the size and position for root
root.geometry('500x500+100+100')
f1=Frame(root)
# pady :Vertical margins
f1.pack(pady=20)
f2=Frame(root)
f2.pack()

buttext=('pupulor','rock','light music','classical')
for index,text in enumerate(buttext):
    Button(f1,text=text,background='pink').grid(row=0,column=index,padx=10)
for index in range(0,8,1):
    Label(f2,width=5,height=10,bg='black' if index%2==0 else 'white').\
        grid(row=0,column=index,padx=10)
root.mainloop()