from tkinter import *
import filemodel as fl
import RightClickMenu as rcm
from configmodel import config
class MyMenu(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.filePath = None
        self.config=config
        # normal menu
        self.creatNormalMenu()
        # right click menu(shortcut menu)
        self.creatRightClickMenu()
        #bind event for posting right click menu
        self.bindRightClick()
        # create a textarea
        self.createTextArea()
        # create a label to show current path
        self.createLabel()

     # 一、normal menu
    def creatNormalMenu(self):
        # 1.create a main menu bar
        main_menu_bar=Menu(self.master)

        # 2.create submenu
        menu_file=Menu(main_menu_bar)
        menu_edit=Menu(main_menu_bar)
        menu_help=Menu(main_menu_bar)
        # add the items for submenu
        menu_file.add_command(label='new',command=lambda :fl.new(self))
        menu_file.add_command(label='open', command=lambda :fl.open_file(self))
        menu_file.add_command(label='save', command=lambda :fl.save(self))
        menu_file.add_command(label='exit', command=lambda :fl.exit(self))

        # 3.add submenu to main menu
        main_menu_bar.add_cascade(label='file',menu=menu_file)
        main_menu_bar.add_cascade(label='edit',menu=menu_edit)
        main_menu_bar.add_cascade(label='help',menu=menu_help)

        # 4.add the main menu to root window
        # self.master['menu']=main_menu_bar
        self.master['menu'] = main_menu_bar

    # --------------------------------------------
    # 二、right click menu
    def creatRightClickMenu(self):
        # 1.create a menu and add items
        self.RCliMenu=Menu(root)
        self.RCliMenu.add_command(label='font')
        self.RCliMenu.add_command(label='background',command=lambda :rcm.modifycolor(self))

    def postRightClickMenu(self,e):
        self.RCliMenu.post(e.x_root,e.y_root)
    # 2.bind event for posting right click menu
    def bindRightClick(self):
        self.master.bind('<Button-3>',self.postRightClickMenu)

    # --------------------------------------------
    def createTextArea(self):
        self.textArea=Text(self.master,bg=self.config.get_color())
        self.textArea.place(relx=0,rely=0,relwidth=1,relheight=1)
    def createLabel(self):
        self.label=Label(self.master,text=f'current:{self.filePath}')
        self.label.pack()

if __name__ == '__main__':
    root=Tk(className='menu practice')
    root.geometry('500x400')
    menu=MyMenu(root)
    menu.place(relx=0,rely=0)
    root.mainloop()


