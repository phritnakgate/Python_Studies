from tkinter import *
root = Tk()
root.title("Data Entry")
root.geometry('300x300')

Label(text='ชื่อ').grid(row=0,column=0)
Label(text='สกุล').grid(row=0,column=2)
Label(text='เบอร์').grid(row=1,column=0)
et1 = Entry()
et1.grid(row=0,column=1)
et1.insert(0,"Phrit")

et2 = Entry()
et2.grid(row=0,column=3)
et2.insert(0,"Nakgate")

et3 = Entry()
et3.grid(row=1,column=1)
et3.insert(0,"0870871983")

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)
button = Button(text="ล้างข้อมูล",command=deleteText).grid(row=3,column=1)
root.mainloop()