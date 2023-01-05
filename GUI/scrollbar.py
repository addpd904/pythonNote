from tkinter import *
root=Tk(className='scroll')
root.iconbitmap(r'E:\programme\Python\practice\others\app.ico')
root.geometry('500x500+200+200')

# creat vertical scrollbar
vbar=Scrollbar(root,orient=VERTICAL)
# vbar.pack(fill=Y)

mylist=Listbox(root,yscrollcommand=vbar.set)
for i in range(30):
    mylist.insert(END,f'{i}st\n')

# relate method yview via command
vbar.config(command=mylist.yview)
mylist.pack(fill=BOTH)

root.mainloop()
