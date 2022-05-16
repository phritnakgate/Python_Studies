from tkinter import *
import pyqrcode
import png
from PIL import ImageTk,Image
root = Tk()
root.title("QR CODE GENERATOR")
canvas = Canvas(root,width=400,height=600)
canvas.pack()

#Function
def qrgen():
    lname = et1.get()
    l = et2.get()
    file_name=lname+".png"
    url=pyqrcode.create(l)
    url.png(file_name,scale=5)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image = image
    canvas.create_window(200,300,window=image_label)
def clear():
    et1.delete(0,END)
    et2.delete(0,END)
    
#WIDGET
app_lbl=Label(text='QR Code Generator',font=('Arial',20,'bold'),justify='center')
canvas.create_window(200,50,window=app_lbl)

name_lbl=Label(text='Name',font=('Arial',18),justify='center')
canvas.create_window(200,100,window=name_lbl)
et1 = Entry(font=16)
canvas.create_window(200,130,window=et1)

link_lbl=Label(text='Link/Text',font=('Arial',18),justify='center')
canvas.create_window(200,160,window=link_lbl)
et2 = Entry(font=16)
canvas.create_window(200,190,window=et2)

btn1 = Button(font=('Arial',16),text='แปลง',command=qrgen)
canvas.create_window(200,450,window=btn1)

btn2 = Button(font=('Arial',16),text='Clear',command=clear)
canvas.create_window(200,500,window=btn2)

root.mainloop()