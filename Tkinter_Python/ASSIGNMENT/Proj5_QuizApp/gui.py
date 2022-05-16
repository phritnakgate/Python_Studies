#UI
from tkinter import *
from controller import Controller
from problems import *

THEME_APP = '#375362'

class UserInterface:
    def __init__(self,controller:Controller):
        self.controller = controller
        #หน้าต่างโปรแกรม
        self.window = Tk()
        self.window.title('Quiz Application')
        self.window.config(padx=20,pady=20,bg=THEME_APP)
        
        #พื้นที่แสดงคะแนน
        self.scoreLabel = Label(text='คะแนน: 0',fg='white',bg=THEME_APP)
        self.scoreLabel.grid(row=0,column=2)
        
        #พื้นที่แสดงโจทย์ปัญหา
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='EIEI',
            font=('Bai jamjuree',18,'bold'),
            fill= THEME_APP
        )
        self.canvas.grid(row=1,column=1,columnspan=2,pady=50)
        
        #ตอบ
        self.txtbox = Entry(font=('Bai jamjuree',18,'bold'))
        self.txtbox.grid(row=2,column=2)


        #ปุ่ม
        self.true_button = Button(text='ตรวจคำตอบ',font=('Bai jamjuree',18,'bold'),command=self.true_pressed)
        self.true_button.grid(row=3,column=2)
        self.get_next_question()
        
        self.window.mainloop()
    def get_next_question(self):
        if self.controller.hasQuestion():
            q_text = self.controller.nextQuestion()
            self.canvas.itemconfig(self.question_text,text=q_text)
            self.scoreLabel.config(text=f'คะแนน: {self.controller.score}')
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text='จบเกม')
            self.scoreLabel.config(text=f'คะแนน: {self.controller.score}')
            self.true_button.config(state='disabled')
    def true_pressed(self): 
            self.controller.checkAnswer(self.txtbox.get())
            self.waitNextQuestion()
    def waitNextQuestion(self):
        self.window.after(1000,self.get_next_question)