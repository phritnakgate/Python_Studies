#เมนู
from tkinter import *
import tkinter.messagebox #เอา messagebox เข้ามา
root = Tk()
root.title("MY GUI")
root.geometry('300x300')

#การสร้างเมนู
myMenu = Menu()
root.config(menu = myMenu)

#Help Window
def showHelp():
    helpwin = Tk()
    helpwin.title('Help')
    helpwin.geometry('300x300')

#About Box
def AboutProgram():
    tkinter.messagebox.showinfo("รายละเอียดโปรแกรม","BuikemProgramVersion Beta 1")

#Exit Box
def ExitProgram():
    tkinter.messagebox.askyesno("QUIT","ออกจากโปรแกรมป่าว?")
    if tkinter.messagebox.YES:
        root.destroy()

#เมนูย่อย(Menu Item)
menuitem = Menu()
menuitem.add_command(label='New File')
menuitem.add_command(label='Open')
menuitem.add_command(label='Save')
menuitem.add_command(label='About',command=AboutProgram)
menuitem.add_command(label='Exit',command=ExitProgram)

menuHelp = Menu()
menuHelp.add_command(label='Help(F1)',command=showHelp)

#เพิ่มเมนู
myMenu.add_cascade(label="File",menu=menuitem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="Help",menu=menuHelp)


root.mainloop()