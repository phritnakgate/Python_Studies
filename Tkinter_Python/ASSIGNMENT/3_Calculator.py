from tkinter import * 
root = Tk()
root.title("Calculator_Basic")

content = ""
txt_input = StringVar(value='0')

#FUNCTION
#รับ input ผ่านปุ่ม
def btn(number):
    global content
    content = content + str(number)
    txt_input.set(content)
#ปุ่ม C
def clearButton():
    display.delete(0,END)
#ปุ่ม =
def equal():
    global content
    try:
        calc = float(eval(content))
        txt_input.set(calc)
        content=""
    except Exception:
        txt_input.set('ERROR')

#WIDGET
#input
display = Entry(font=('Arial',45),bg='white',textvariable=txt_input,justify='right')
display.grid(columnspan=4)

#menu
myMenu = Menu()
root.config(menu = myMenu)
myMenu.add_cascade(label="Mode")

#row1
btnc=Button(font=('Arial',30,'bold'),fg='white',bg='blue',text='C',command=clearButton,padx=30,pady=15).grid(row=1,column=0,sticky='nsew')
btndiv=Button(font=('Arial',30,'bold'),bg='orange',text='÷',command=lambda:btn('/'),padx=30,pady=15).grid(row=1,column=3,sticky='nsew')
btnbl=Button(font=('Arial',30,'bold'),bg='orange',text='(',command=lambda:btn('('),padx=30,pady=15).grid(row=1,column=1,sticky='nsew')
btnbr=Button(font=('Arial',30,'bold'),bg='orange',text=')',command=lambda:btn(')'),padx=30,pady=15).grid(row=1,column=2,sticky='nsew')
#row2
btn7=Button(font=('Arial',30,'bold'),fg='black',text='7',command=lambda:btn(7),padx=30,pady=15).grid(row=2,column=0,sticky='nsew')
btn8=Button(font=('Arial',30,'bold'),fg='black',text='8',command=lambda:btn(8),padx=30,pady=15).grid(row=2,column=1,sticky='nsew')
btn9=Button(font=('Arial',30,'bold'),fg='black',text='9',command=lambda:btn(9),padx=30,pady=15).grid(row=2,column=2,sticky='nsew')
btnmul=Button(font=('Arial',30,'bold'),bg='orange',text='×',command=lambda:btn('*'),padx=30,pady=15).grid(row=2,column=3,sticky='nsew')

#row3
btn4=Button(font=('Arial',30,'bold'),fg='black',text='4',command=lambda:btn(4),padx=30,pady=15).grid(row=3,column=0,sticky='nsew')
btn5=Button(font=('Arial',30,'bold'),fg='black',text='5',command=lambda:btn(5),padx=30,pady=15).grid(row=3,column=1,sticky='nsew')
btn6=Button(font=('Arial',30,'bold'),fg='black',text='6',command=lambda:btn(6),padx=30,pady=15).grid(row=3,column=2,sticky='nsew')
btnminus=Button(font=('Arial',30,'bold'),bg='orange',text='-',command=lambda:btn('-'),padx=30,pady=15).grid(row=3,column=3,sticky='nsew')

#row4
btn1=Button(font=('Arial',30,'bold'),fg='black',text='1',command=lambda:btn(1),padx=30,pady=15).grid(row=4,column=0,sticky='nsew')
btn2=Button(font=('Arial',30,'bold'),fg='black',text='2',command=lambda:btn(2),padx=30,pady=15).grid(row=4,column=1,sticky='nsew')
btn3=Button(font=('Arial',30,'bold'),fg='black',text='3',command=lambda:btn(3),padx=30,pady=15).grid(row=4,column=2,sticky='nsew')
btnplus=Button(font=('Arial',30,'bold'),bg='orange',text='+',command=lambda:btn('+'),padx=30,pady=15).grid(row=4,column=3,sticky='nsew')

#row5
btn0=Button(font=('Arial',30,'bold'),fg='black',text='0',command=lambda:btn(0),padx=30,pady=15).grid(row=5,column=1,sticky='nsew')
btneq=Button(font=('Arial',30,'bold'),fg='white',bg='blue',command=equal,text='=',padx=30,pady=15).grid(row=5,column=3,sticky='nsew')
btndot=Button(font=('Arial',30,'bold'),fg='black',text='.',command=lambda:btn('.'),padx=30,pady=15).grid(row=5,column=2,sticky='nsew')

root.mainloop()