from tkinter import *
import os
import fnmatch
from PIL import ImageTk,Image
from pygame import mixer
root=Tk()
root.geometry("600x500")
root.minsize(400,300)
root.maxsize(600,500)
root.title("Mi MUsic PLayer")
root.config(bg="black")
def start():
    global rain,previous,startnow,pause,next,newimage,newimage1
    path ="C:\\Users\Jyoti\OneDrive\Desktop\Mi MUsic PLayer\playlist"
    pattern ="*mp3"
    mixer.init()
    def play():
        mixer.music.load(path + "\\" + lbx.get("anchor"))
        mixer.music.play()
    def stop_bar():
        mixer.music.stop()
        lbx.select_clear("active")
    def  next_bar():
        new_song = lbx.curselection()
        new_song = new_song[0] + 1
        new_song_name=lbx.get(new_song)
        mixer.music.load(path + "\\" +new_song_name )
        mixer.music.play()
        lbx.select_clear(0,"end")
        lbx.activate(new_song)
        lbx.select_set(new_song)
    def pre_bar():
        new_song = lbx.curselection()
        new_song = new_song[0] -1
        new_song_name=lbx.get(new_song)
        mixer.music.load(path + "\\" +new_song_name )
        mixer.music.play()
        lbx.select_clear(0,"end")
        lbx.activate(new_song)
        lbx.select_set(new_song)
    f1=Frame(bg="black")
    f1.place(x=0,y=0,width=600,height=500) 
    lbx=Listbox(f1,bg="black",fg="white",font="DS-Digital 12 bold",width=25,height=45)
    lbx.pack(side= LEFT,padx=10,pady=10)
    f2=Frame(f1,bg="white",width=900,height=70)
    f2.pack(anchor=CENTER)
    f3=Frame(f1,bg="white",width=500,height=50)
    f3.pack(side=BOTTOM)
    rain=ImageTk.PhotoImage(Image.open("plant.jpg").resize((900,200)))
    imagelabel=Label(f1,image=rain)
    imagelabel.pack()
    previous=PhotoImage(file="previous.png")
    img1btn=Button(f1,image=previous,command=pre_bar)
    img1btn.pack(side=LEFT,pady=3,padx=3)
    startnow=PhotoImage(file="start.png")
    img2btn=Button(f1,image=startnow,command=play)
    img2btn.pack(side=LEFT,pady=3,padx=3)
    pause=PhotoImage(file="pause.png")
    img3btn=Button(f1,image=pause,command=stop_bar)
    img3btn.pack(side=LEFT,pady=3,padx=3)
    next=PhotoImage(file="next.png")
    img4btn=Button(f1,image=next,command= next_bar)
    img4btn.pack(side=LEFT,pady=3,padx=3)
    newimage=ImageTk.PhotoImage(Image.open("rain.png").resize((400,90)))
    image5=Label(f2,image=newimage)
    image5.pack(side=BOTTOM)
    newimage1=ImageTk.PhotoImage(Image.open("path.jpg").resize((400,90)))
    image6=Label(f3,image=newimage1)
    image6.pack(side=BOTTOM)
    for root,dir,files in os.walk(path):
        for filename in fnmatch.filter(files,pattern):
            lbx.insert("end",filename)   
image1 = PhotoImage(file="moon.png")
pic1=Label(image=image1 )
t1=Label(text="Mi MUsic PLayer",font= "Broadway 40 bold"  ,fg="Blue",bg ="black" )
Button(root,text="WELCOME TO Mi WORLD!!\n CLICK!!",font="Times 10 bold",bg="#9BABB8",fg="black",height = 3, width=40,command=start).pack(side=BOTTOM)
t1.pack(side=BOTTOM)
pic1.pack(side=TOP)
root.mainloop()
