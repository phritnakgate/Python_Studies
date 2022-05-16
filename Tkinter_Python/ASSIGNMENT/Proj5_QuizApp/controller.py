from gui import *
class Controller:
    def __init__(self,data):
        self.question_list = data
        self.question_number = 0
        self.score = 0
    
    def nextQuestion(self):
        current = self.question_list[self.question_number]
        self.question_number+=1
        return f'{self.question_number}){current.text}'
    def hasQuestion(self):
        return self.question_number < len(self.question_list)
    
    def checkAnswer(self,userInput,correct_answer):
        if(userInput == correct_answer):
            #ได้คะแนน
            self.score += 1
            print('คะแนน: ',self.score)
        else:
            print('ตอบผิด เฉลยคือ ',correct_answer)