from tkinter import *
class MyMenu(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        # normal menu
        self.creatNormalMenu()
        # right click menu(shortcut menu)
        self.creatRightClickMenu()
        #bind event for posting right click menu
        self.bindRightClick()

     # 一、normal menu
    def creatNormalMenu(self):
        # 1.create a main menu bar
        main_menu_bar=Menu(self)

        # 2.create submenu
        menu_file=Menu(main_menu_bar)
        menu_edit=Menu(main_menu_bar)
        menu_help=Menu(main_menu_bar)
        # add the items for submenu
        menu_file.add_command(label='new',command=self.new)
        menu_file.add_command(label='open', command=self.open)
        menu_file.add_command(label='save', command=self.save)
        menu_file.add_command(label='exit', command=self.exit)

        # 3.add submenu to main menu
        main_menu_bar.add_cascade(label='file',menu=menu_file)
        main_menu_bar.add_cascade(label='edit',menu=menu_edit)
        main_menu_bar.add_cascade(label='help',menu=menu_help)

        # 4.add the main menu to root window
        self.master['menu']=main_menu_bar

    # --------------------------------------------
    # 二、right click menu
    def creatRightClickMenu(self):
        # 1.create a menu and add items
        self.RCliMenu=Menu(root)
        self.RCliMenu.add_command(label='font')
        self.RCliMenu.add_command(label='background')

    def postRightClickMenu(self,e):
        self.RCliMenu.post(e.x,e.y)
    # 2.bind event for posting right click menu
    def bindRightClick(self):
        self.master.bind('<Button-3>',self.postRightClickMenu)

    # --------------------------------------------

    def new(self):
        pass
    def open(self):
        pass
    def save(self):
        pass
    def exit(self):
        pass
if __name__ == '__main__':
    root=Tk(className='menu practice')
    root.geometry('500x400')
    menu=MyMenu(master=root)
    menu.pack()
    root.mainloop()


