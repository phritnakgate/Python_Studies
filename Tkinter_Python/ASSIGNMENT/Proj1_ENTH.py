from tkinter import *
import tkinter
from googletrans import Translator
from tkinter import messagebox
root = Tk()
root.title("Google Translate EN-TH")
root.geometry('530x300')
root.maxsize(530,300)
root.minsize(530,300)
lbl=Label(text='Google Translate EN-TH',font=('Arial',20,'bold'),justify='center').pack()
txteng = Text(root,width=30,height=10)
txteng.place(x=10,y=70)
txtthai = Text(root,width=30,height=10)
txtthai.place(x=260,y=70)
def trans():
    translator = Translator()
    eng = txteng.get('1.0','end-1c')
    try:
        th = translator.translate(text=eng,src='en',dest='th')
        txtthai.insert('end',th.text)
    except Exception:
        messagebox.ERROR('ERROR','ใส่ภาษาผิด')
btntrans = Button(font=('Arial',18),text='Translate',command=trans)
btntrans.place(x=150,y=250)
def clear():
    txteng.delete(1.0,'end')
    txtthai.delete(1.0,'end')
btnclear = Button(font=('Arial',18),text='Clear',command=clear)
btnclear.place(x=280,y=250)
root.mainloop()