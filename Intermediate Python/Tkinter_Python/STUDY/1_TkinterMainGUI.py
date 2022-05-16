from tkinter import *
#1. สร้างหน้าจอด้วย Tk
root = Tk()
root.title("MY GUI") #ชื่อโปรแกรม

#2. กำหนดขนาดและตำแหน่ง
'''
.geometry('widthxheight+pos x+pos y')
'''
root.geometry('640x480+0+0')

#3. แสดงข้อความด้วย label => แบบพิกัด/แบบ grid
#myLabel1 = Label(root,text = "Hello World",fg="red",font=20,bg='yellow').place(x=100,y=0)
myLabel1 = Label(root,text = "Hello World",fg="red",font=20,bg='yellow').grid(row=0,column=0)
#myLabel2 = Label(root,text = "Buikemkungz",fg='green',font=18).place(x=50,y=200)
myLabel2 = Label(root,text = "Buikemkungz",fg='green',font=18).grid(row=1,column=0)



#4. ปุ่ม
btn1 = Button(root,text="บันทึก",fg="white",font=18,bg='green').grid(row=3,column=2)
btn2 = Button(root,text="เปิดข้อมูล",fg="white",font=18,bg='red').grid(row=4,column=2)

#5. textbox
txt = StringVar()
ent1 = Entry(root,textvariable=txt).grid(row=2,column=0)

#6.หน้าจอที่ 2
newwin = Tk()
newwin.title("NEWWIN")
newwin.geometry('300x300')
newwin.mainloop()

root.mainloop() 
'''
ใส่ไว้ท้ายสุดเสมอ
ลูปที่รันวนไปเรื่อยๆ ตลอดเวลาที่เราเปิดหน้าต่างของโปรแกรมนั้นไว้ โปรแกรมจะออกจากลูปเมื่อเราปิดหน้าต่าง 
event loop จะคอยดูว่าเรา คลิกหรือพิมพ์อะไรบ้าง โปรแกรมจะได้คอยตอบสนองคำสั่งของผู้ใช้
'''