from tkinter import * 
from tkinter import ttk
root = Tk()
root.title("GUI")
root.geometry('500x500')
Label(root,text = "จังหวัด",font=('TH sarabun New',20)).grid(row=0,column=0)
choice = StringVar(value="เลือกจังหวัดของคุณ")
combo = ttk.Combobox(textvariable=choice)
combo.grid(row=0,column=1)
combo["values"]=("กทม.","หาดใหญ่")
def selectCity():
    Label(text = "คุณเลือก"+choice.get(),font=('TH sarabun New',20)).grid(row=2,column=1)
Button(text="บันทึก",font=('TH Sarabun New',18),fg='white',bg='green',command=selectCity).grid(row=1,column=1)
root.mainloop()