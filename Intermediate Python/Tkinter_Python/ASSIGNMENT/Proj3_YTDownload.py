from tkinter import *
from pytube import YouTube
from moviepy.editor import *
from tkinter import messagebox

root = Tk()
root.title("Youtube Downloader")
canvas = Canvas(root,width=600,height=300)
canvas.pack()

#Function
def downloader():
    try:
        video_path=et1.get()
        mp4 = YouTube(video_path).streams.get_highest_resolution().download()
        video_clip = VideoFileClip(mp4)
        video_clip.close()
    except Exception:
        messagebox.ERROR('ERROR','ใส่ URL ผิด')
def clearentry():
    et1.delete(0,END)

#WIDGET
app_lbl=Label(text='Youtube Downloader',font=('Arial',20,'bold'),justify='center')
canvas.create_window(300,50,window=app_lbl)
name_lbl=Label(text='Link',font=('Arial',18),justify='center')
canvas.create_window(300,100,window=name_lbl)
et1 = Entry(font=16,width=50)
canvas.create_window(300,130,window=et1)
btn1 = Button(font=('Arial',16),text='Download',command=downloader)
canvas.create_window(300,160,window=btn1)
btn2 = Button(font=('Arial',16),text='Download',command=clearentry)
canvas.create_window(300,190,window=btn1)
root.mainloop()