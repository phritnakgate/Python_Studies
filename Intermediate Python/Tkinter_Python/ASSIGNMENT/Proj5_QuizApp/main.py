from question import *
from problems import *
from controller import *
from gui import *

all_question = []
UserInterface()
#โจทย์
for item in question_data:
    problem = item['problem']
    answer = item['answer']
    question = Question(problem,answer)
    all_question.append(question)

#แผงควบคุม
controller = Controller(all_question)
userinterface = UserInterface(controller)
