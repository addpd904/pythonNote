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
        # 1.a label
        self.label1=Label(self,text='login')
        self.label1.pack()
        # 2.a entry,username
        self.entry1=Entry(self)
        v1=StringVar()
        # bind v1 to entry(Bidirectional association)
        self.entry1['textvariable']=v1
        self.entry1.pack()
        # 2.a entry,passerword
        self.entry2 = Entry(self,show='*')
        v2 = StringVar()
        # bind v1 to entry(Bidirectional association)
        self.entry1['textvariable'] = v2
        self.entry2.pack()
        # 4.a login button
        # command just like listener to listen click event
        self.butlog=Button(self,text='exit',command=self.clickfun)
        self.butlog.pack()
    def clickfun(self):

            # we can get the value of entry via get()
            username=self.entry1.get()
            password=self.entry2.get()
            messagebox.showinfo('message', f'username:{username}\npassword={password}')

if __name__ == '__main__':
    root =Tk()
    root.geometry('500x500+400+400')
    app=Application(master=root)
    root.mainloop()