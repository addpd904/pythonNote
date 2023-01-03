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
        # a.create a checkbutton
        self.video=IntVar()
        self.code=IntVar()
        self.basketball=IntVar()
        Label(self,text='hobby').pack(side='left')
        Checkbutton(self,text='video',onvalue=1,offvalue=0,
                   variable=self.video).pack(side='left')
        Checkbutton(self, text='basketball',
                    onvalue=1, offvalue=0,variable=self.basketball).pack(side='left')
        Checkbutton(self, text='code',
                    onvalue=1, offvalue=0, variable=self.code).pack(side='left')
        Button(self,text='confirm',command=self.confirm).pack(side='left')
    def confirm(self):
        hobby=' vi ' if self.video.get() == 1 else ''
        hobby+=' bas ' if self.basketball.get() == 1 else ''
        hobby+=' cod ' if self.code.get() == 1 else ''
        messagebox.showinfo('hint',hobby)
if __name__ == '__main__':
    root =Tk()
    root.geometry('500x500+400+400')
    app=Application(master=root)
    root.mainloop()