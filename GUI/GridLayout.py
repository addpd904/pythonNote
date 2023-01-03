# row,column;columspan ;ipadx;padx;sticky
# columspan:The number of colums spanned
# layout manager
from tkinter import *
from tkinter import messagebox
# DIY component class
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.creatWidget()
    def creatWidget(self):
        # create widget
        # a.username
        Label(self,text='username').grid(row=0,column=0)
        Entry(self).grid(row=0,column=1)
        # b.password
        Label(self, text='password').grid(row=1, column=0)
        Entry(self,show='*').grid(row=1, column=1)
        # c.button
        Button(self,text='login').grid(row=2,column=0,sticky=EW)
        Button(self,text='cancle').grid(row=2,column=1,sticky=E)

if __name__ == '__main__':
    root =Tk()
    root.geometry('500x500+400+400')
    app=Application(master=root)
    root.mainloop()