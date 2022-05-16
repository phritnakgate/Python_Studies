from tkinter import * 
from tkinter.font import BOLD
from tkinter import ttk

root = Tk()
root.title("โปรแกรมแปลงสกุลเงิน")
root.geometry('600x600')
def exchange():
    m = money.get()
    c = choice.get()
    if c == "EUR":
        finish = m*0.026
        Label(text=(finish,"EUR"),font=('TH Sarabun New',18)).grid(row=6,column=2)
    elif c == "JPY":
        finish = m*3.486
        Label(text=(finish,"JPY"),font=('TH Sarabun New',18)).grid(row=6,column=2)
    elif c == "USD":
        finish = m*0.031
        Label(text=(finish,"USD"),font=('TH Sarabun New',18)).grid(row=6,column=2)
    elif c == "GBP":
        finish = m*0.023
        Label(text=(finish,"GBP"),font=('TH Sarabun New',18)).grid(row=6,column=2)
def delet():
    et1.delete(0,END)
Label(text='โปรแกรมแปลงสกุลเงิน',font=('TH Sarabun New',20,BOLD)).grid(row=0,column=1)
Label(text='ค่าเงิน',font=('TH Sarabun New',18)).grid(row=1,column=0)
Label(text='1 THB = 0.026 EUR',font=('TH Sarabun New',18)).grid(row=1,column=1)
Label(text='1 THB = 3.486 JPY',font=('TH Sarabun New',18)).grid(row=2,column=1)
Label(text='1 THB = 0.031 USD',font=('TH Sarabun New',18)).grid(row=3,column=1)
Label(text='1 THB = 0.023 GBP',font=('TH Sarabun New',18)).grid(row=4,column=1)
Label(text='ใส่เงินบาท',font=('TH Sarabun New',18,BOLD)).grid(row=5,column=0)
money = IntVar()
et1 = Entry(font=('TH Sarabun New',18),textvariable=money)
et1.grid(row=5,column=1)
Label(text='เลือกสกุลเงิน',font=('TH Sarabun New',18,BOLD)).grid(row=5,column=2)
choice = StringVar(value="เลือกค่าเงิน")
combo = ttk.Combobox(textvariable=choice)
combo.grid(row=5,column=3)
combo["values"]=("EUR","JPY","USD","GBP")
Label(text='ได้เงินมา',font=('TH Sarabun New',18,BOLD)).grid(row=6,column=1)

btn1 = Button(text="คำนวณ",font=('TH Sarabun New',18),fg='white',bg='green',command=exchange).grid(row=7,column=1)
btn2 = Button(text="ล้างข้อมูล",font=('TH Sarabun New',18),fg='white',bg='red',command=delet).grid(row=8,column=1)
root.mainloop()