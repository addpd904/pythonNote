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
        # a.create a canvas
        self.can1=Canvas(self,width=300,height=400,bg='pink')
        self.can1.pack()
        # draw line
        self.can1.create_line(1,1,30,49,200,177)
        # draw oval
        self.can1.create_oval(40,40,90,90)
        # add a photo
        global photo
        photo=PhotoImage(file=r'E:\programme\Python\practice\dogcard.gif')
        self.can1.create_image(0,0,image=photo)
if __name__ == '__main__':
    root =Tk()
    root.geometry('500x500+400+400')
    app=Application(master=root)
    root.mainloop()