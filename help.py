from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
   def __init__(self,root):                    
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")
      
      title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="DodgerBlue",fg="white")
      title_lbl.place(x=0,y=0,width=1530,height=60)
      
      img_top=Image.open(r"clg images/help_bg.jpg")
      img_top=img_top.resize((1530,720),Image.LANCZOS)
      self.photoimg_top=ImageTk.PhotoImage(img_top)
      
      f_lbl=Label(self.root,image=self.photoimg_top) 
      f_lbl.place(x=0,y=55,width=1530,height=720)

      dev_label=Label(f_lbl,text="How can we help you?", font=("times new roman",30,"bold"),fg="black",bg="white")
      dev_label.place(x=100,y=150,width=450,height=60)
      
      
      dev_label2=Label(f_lbl,text="Need a hand?We're here to help!""\n Whether you have a question,encounter a hiccup ,our dedicated ""\nteam is at your service. Maintaining accuracy is our top prioprity!!", font=("times new roman",12,"bold"),fg="black",bg="white")
      dev_label2.place(x=100,y=210,width=450,height=60)
      
      dev_label3=Label(f_lbl,text="\nEmail:prakanshu35@gmail.com", font=("times new roman",12,"bold"),fg="black",bg="white")
      dev_label3.place(x=100,y=270,width=450,height=40)
      
   
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()