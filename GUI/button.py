# Label
# layout manager
# set options to control component's color ,status ...
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
        # a button
        # the option command just like listener to listen click event
        self.button1=Button(self,text='log in',command=self.login,background='pink')
        # []:redefine built - in functions
        self.button1.pack()
        #multi-line text
    def login(self):
        messagebox.showinfo('login', 'log in successfully')

if __name__ == '__main__':
    root =Tk()
    root.geometry('500x500+400+400')
    app=Application(master=root)
    root.mainloop()