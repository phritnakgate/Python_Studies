from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
root = Tk()
root.title("MY GUI")
root.geometry('300x300')
lbl = Label(root,text = "Hello World",font=20).pack()
def selectColor():
    color = askcolor()
    lbl2 = Label(root,text = "Hello World",bg=color[1]).pack()
def selectFile():
    fileopen = askopenfilename()
    fileContent = open(fileopen,encoding='utf8')
    lbl3 = Label(text = fileContent.read()).pack()
btn1 = Button(root,text="เลือกสี",fg="white",font=20,bg='green',command=selectColor).pack()
btn2 = Button(root,text="เลือกไฟล์",fg="white",font=20,bg='green',command=selectFile).pack()
root.mainloop()