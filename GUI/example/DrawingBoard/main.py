from tkinter import *
from tkinter.colorchooser import askcolor

from configmodel import config
class DrawBoard(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.config=config
        self.master=master
        # current choice default:line
        self.name='line'
        self.penColor='#000000'
        self.createWidget()
        self.x=0
        self.y=0
        self.firstpress=True
        self.lastDrawId=0
        self.shortcut()
    def createWidget(self):
        self.canvas=Canvas(root,bg=config.get_color(),width=600,height=500)
        self.canvas.pack()

        # button
        pen_button=Button(self.master,text='pen',name='pen',height=3,width=5)
        pen_button.pack(side='left',padx=15)
        line_button = Button(self.master,text='line', name='line',height=3,width=5)
        line_button.pack(side='left',padx=15)
        rect_button = Button(self.master,text='rect', name='rect',height=3,width=5)
        rect_button.pack(side='left',padx=15)
        eraser_button = Button(self.master,text='eraser', name='eraser',height=3,width=5)
        eraser_button.pack(side='left',padx=15)
        color_button=Button(self.master,text='color',name='color',height=3,width=5)
        color_button.pack(side='left',padx=15)
        clear_button=Button(self.master,text='clear',name='clear',height=3,width=5)
        clear_button.pack(side='left',padx=15)

        # add event for every button
        pen_button.bind_class('Button', '<Button-1>', self.eventManager)

        # right click menu
        self.rightClickMenu=Menu(self.master)
        self.rightClickMenu.add_command(label='background',command=lambda :self.modifyColor())
        self.master.bind('<Button-3>',self.postMenu)

    def postMenu(self,e):
        self.rightClickMenu.post(e.x_root,e.y_root)

    def modifyColor(self):
        color_tuple = askcolor(color='pink', title='colorBox practice')
        self.canvas.config(bg=color_tuple[1])
        self.config.save_color(color_tuple[1])
    def eventManager(self,e:Event,name=None):
        if name == None:
            self.name=e.widget.winfo_name()
        else:
            self.name=name
        if self.name == 'line' :
            self.canvas.bind('<B1-Motion>',self.myLine)
            self.canvas.bind('<ButtonRelease-1>',self.release)
        if self.name == 'pen':
            self.canvas.bind('<B1-Motion>', self.myPen)
            self.canvas.bind('<ButtonRelease-1>', self.release)
        if self.name == 'clear':
            self.canvas.delete('all')
        if self.name=='color':
            color_tuple = askcolor(color='pink', title='colorBox practice')
            self.penColor=color_tuple[1]

    def myLine(self,e):
        if self.firstpress==True:
            self.firstpress=False
            self.x=e.x
            self.y=e.y
        self.canvas.delete(self.lastDrawId)
        self.lastDrawId=self.canvas.create_line(self.x,self.y,e.x,e.y,fill=self.penColor)
    def release(self,e):
        self.lastDrawId=0
        self.firstpress=True

    def myPen(self,e):
        if self.firstpress==True:
            self.firstpress=False
            self.x=e.x
            self.y=e.y
        self.canvas.delete(self.lastDrawId)
        self.lastDrawId=self.canvas.create_line(self.x,self.y,e.x,e.y,fill=self.penColor)
        self.x=e.x
        self.y=e.y
        self.lastDrawId=0

    def shortcut(self):
        self.master.bind('<Control-l>',lambda e:self.eventManager(e,'line'))
        self.master.bind('<Control-p>',lambda e:self.eventManager(e,'pen'))

if __name__ == '__main__':
    root=Tk(className='DrawBoard')
    drawB=DrawBoard(root)
    drawB.pack()
    root.geometry('600x600+100+100')
    root.mainloop()