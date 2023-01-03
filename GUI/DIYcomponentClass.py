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
        # a normal button
        self.but1=Button(self)
        self.but1['text']='a button'
        self.but1.pack()
        self.but1.bind('<Button-1>',self.clickfun)
        # a exit button
        # command just like listener to listen click event
        self.butexit=Button(self,text='exit',command=root.destroy)
        self.butexit.pack()
    def clickfun(self,e):
            messagebox.showinfo('message', 'the button was clicked')

if __name__ == '__main__':
    root =Tk()
    root.geometry('500x500+400+400')
    app=Application(master=root)
    root.mainloop()