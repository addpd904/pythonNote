from tkinter import *
# DIY a  container
class CardCon(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.pack()
        self.creatWidget()
    def creatWidget(self):
        self.photo = PhotoImage(file=r'E:\programme\Python\practice\dogcard1.gif')
        for i in range(0,10,1):
            label=Label(self.master, image=self.photo)
            label.place(x=0+i*80, y=200)
            # bind click event
            label.bind('<Button-1>',self.pushCard)

    def pushCard(self,e):
        if e.widget.winfo_y()==200:
            e.widget.place(y=170)
        else:
            e.widget.place(y=200)

if __name__ == '__main__':
    root=Tk(className='cards')
    root.geometry('900x600')
    car_container=CardCon(master=root)
    root.mainloop()
