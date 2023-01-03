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
        # a.create a Radiobutton
        self.v=StringVar()
        self.v.set('f')
        self.rb1=Radiobutton(self,text='man',value='m',variable=self.v).pack(side='left')
        self.rb2 = Radiobutton(self, text='women', value='f', variable=self.v).pack(side='left')
        Button(self,text='confirm',command=self.confirm).pack(side='left')
    def confirm(self):
        messagebox.showinfo('hint','choose: '+self.v.get())
if __name__ == '__main__':
    root =Tk()
    root.geometry('500x500+400+400')
    app=Application(master=root)
    root.mainloop()