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
        # a label
        self.label1=Label(self,text='a label',height=3,
                          bg='pink',fg='yellow',font=('黑体',25))
        # []:redefine built - in functions
        self.label1['text']='hello'
        self.label1.pack()
        #multi-line text
        self.label2=Label(self,text='today is a good day\nhoware you'
                          ,borderwidth=2,relief='solid',
                          justify='right')
        self.label2.pack()

if __name__ == '__main__':
    root =Tk()
    root.geometry('500x500+400+400')
    app=Application(master=root)
    root.mainloop()