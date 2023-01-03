from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfilename
from main import MyMenu

def new(self:MyMenu):
    self.textArea.delete(1.0, END)
    # create new file via
    self.filePath=asksaveasfilename(title='new file',initialdir=r'E:\programme\Python\practice',filetypes=[('text file','.txt')],
                      defaultextension='.txt')
    # Refresh the current path
    self.label['text']=f'current:{self.filePath}'


def open_file(self):
    self.textArea.delete(1.0,END)
    with askopenfile(title='filebox practice',initialdir=r'E:\programme\Python\practice',filetypes=[('text file','.txt')]) as f:
        self.filePath=f.name
        print(self.filePath)
        self.textArea.insert(INSERT,f.read())
        # Refresh the current path
        self.label['text'] = f'current:{self.filePath}'

def save(self):
    with open(self.filePath,'w') as f:
        text=self.textArea.get(1.0,END)
        f.write(text)


def exit(self):
    self.master.quit()