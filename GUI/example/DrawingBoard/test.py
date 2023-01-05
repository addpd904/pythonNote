from tkinter import *
root=Tk()
root.geometry('500x500+1001+100')
can=Canvas(root,bg='pink')
can.place(relheight=1,relwidth=1)
x1=0
y1=0
x2=1
y2=1
for i in range(0x1,0x200):
    hexstr=hex(i).replace('0x','')
    for i in range(0,6-len(hexstr)):
        hexstr+='0'
    colorstr='#'+hexstr
    can.create_line(x1,y1,x2,y2,fill=colorstr)
    x1+=1
    x2+=1
    y1+=1
    y2+=1

r=1
g=1
b=1
end=1000
print(0xffffff)

root.mainloop()