from tkinter import *
from gtts import gTTS
root = Tk()
root.title("Text to Speech")
canvas = Canvas(root,width=600,height=300)
canvas.pack()

#Function
def ttsp():
    word=et.get()
    language = 'th'
    output=gTTS(text=word,lang=language,slow=False)
    output.save('%s.mp3'%word)

#WIDGET
app_lbl=Label(text='Text to Speech',font=('Arial',20,'bold'),justify='center')
canvas.create_window(300,50,window=app_lbl)
et=Entry(font=('Bai jamjuree',16))
canvas.create_window(300,100,window=et)
btnspeech=Button(text='Speech',font=16,command=ttsp)
canvas.create_window(300,150,window=btnspeech)
root.mainloop()