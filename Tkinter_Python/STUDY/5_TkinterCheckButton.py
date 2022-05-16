from tkinter import *
root = Tk()
root.title("MY GUI")
root.geometry('300x300')

def showChoice():
    choice1 = lang1.get()
    choice2 = lang2.get()
    choice3 = lang3.get()
    choice4 = lang4.get()
    if choice1 == 1:
        Label(text = "P y t h o N").pack(anchor=W)
    if choice2 == 1:
        Label(text = "J a v a").pack(anchor=W)
    if choice3 == 1:
        Label(text = "P H P").pack(anchor=W)
    if choice4 == 1:
        Label(text = "C Shaftttttttt").pack(anchor=W)
#เก็บค่า 0 = ไม่เลือก 1 = เลือก
lang1 = IntVar()
Checkbutton(text="Python",variable=lang1).pack(anchor=W)
lang2 = IntVar()
Checkbutton(text="Java",variable=lang2).pack(anchor=W)
lang3 = IntVar()
Checkbutton(text="PHP",variable=lang3).pack(anchor=W)
lang4 = IntVar()
Checkbutton(text="C#",variable=lang4).pack(anchor=W)

Button(text="แสดงตัวเลือก",command=showChoice).pack(anchor=W)
root.mainloop()