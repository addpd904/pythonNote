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
        # a.create a textarea
        self.texta1=Text(self,width=50,height=10,
                         background='gray')
        self.texta1.pack()
        self.texta1.insert(1.0,'hello')
        self.texta1.insert(END,'world,day day study')
        # 1.insert text
        Button(self,text='insert text',command=self.inserttex).pack(side='left')
        # 2.get text
        Button(self, text='get all text', command=self.gettext).pack(side='left')
        #3.mark text and operate
        Button(self,text='mark',command=self.mark).pack(side='left')
    def inserttex(self):
        self.texta1.insert(INSERT,' wonderful ')
        self.texta1.insert(END,' perfect ')
    def gettext(self):
        messagebox.showinfo('text',self.texta1.get(1.0,END))
    def mark(self):
        # make a mark for specific text
        self.texta1.tag_add('mark1',1.0,1.2)
        # operate the mark
        self.texta1.tag_config('mark1',background='pink')
        # bind a event
        self.texta1.tag_bind('mark1','<Button-1>',self.markevent)
    def markevent(self,e):
        messagebox.showinfo('hint', 'click the area that is marked')
if __name__ == '__main__':
    root =Tk()
    root.geometry('500x500+400+400')
    app=Application(master=root)
    root.mainloop()