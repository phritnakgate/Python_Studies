from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("MY GUI")
root.geometry('300x300')
def showChoice():
    choice = language.get()
    if choice==1:
        tkinter.messagebox.showinfo("eiei","WOW PYTHON")
    elif choice==2:
        tkinter.messagebox.showinfo("eiei","WOW Java")
    elif choice ==3:
        tkinter.messagebox.showinfo("eiei","WOW PHP")
    else:
        tkinter.messagebox.showinfo("eiei","WOW C#")
language = IntVar()
Radiobutton(text="Python",variable=language,value=1,command=showChoice).grid(row=0,column=0)
Radiobutton(text="Java",variable=language,value=2,command=showChoice).grid(row=0,column=1)
Radiobutton(text="PHP",variable=language,value=3,command=showChoice).grid(row=0,column=2)
Radiobutton(text="C#",variable=language,value=4,command=showChoice).grid(row=0,column=3)
root.mainloop()