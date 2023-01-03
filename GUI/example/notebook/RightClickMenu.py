from tkinter.colorchooser import askcolor
# from main import MyMenu
def modifycolor(self):
    color_tuple=askcolor(color='pink',title='colorBox practice')
    self.textArea.config(bg=color_tuple[1])
    self.config.save_color(color_tuple[1])