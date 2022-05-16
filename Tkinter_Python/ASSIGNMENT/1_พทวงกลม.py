from tkinter import * 
from tkinter.font import BOLD
import tkinter.messagebox
root = Tk()
root.title("Area of Circle")
root.geometry('500x500')
def delet():
    et1.delete(0,END)   
    et2.delete(0,END)
    et2.config(state="disable")
def findArea():
    try:
        r = radius.get()
        area = 3.14*r*r
        et2.config(state="normal")
        et2.insert(0,area)
    except Exception:
        tkinter.messagebox.showerror('ERROR','กรอกค่าผิดดดดด')
Label(text='โปรแกรมคำนวณพื้นที่วงกลม',font=('TH Sarabun New',20,BOLD)).grid(row=0,column=1)
Label(text='ป้อนค่ารัศมี',font=('TH Sarabun New',18,BOLD)).grid(row=1,column=0)
radius=IntVar()
et1 = Entry(font=('TH Sarabun New',18),textvariable=radius)
et1.grid(row=1,column=1)
Label(text='ผลลัพธ์',font=('TH Sarabun New',18,BOLD)).grid(row=2,column=0)
et2 = Entry(font=('TH Sarabun New',18))
et2.grid(row=2,column=1)
et2.config(state="disable")
btn1 = Button(text="คำนวณ",font=('TH Sarabun New',18),fg='white',bg='green',command=findArea).grid(row=4,column=1)
btn2 = Button(text="ล้างข้อมูล",font=('TH Sarabun New',18),fg='white',bg='red',command=delet).grid(row=5,column=1)
root.mainloop()