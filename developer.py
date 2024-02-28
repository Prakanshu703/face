from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
   def __init__(self,root):                    
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")
      
      title_lbl=Label(self.root,text="DEVELOPER", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
      title_lbl.place(x=0,y=0,width=1530,height=45)
      
      img_top=Image.open(r"clg images\programming-code-abstract-technology-background-of-software-developer-and-computer-ai-generated-photo.jpeg")
      img_top=img_top.resize((1530,720),Image.LANCZOS)
      self.photoimg_top=ImageTk.PhotoImage(img_top)
      
      f_lbl=Label(self.root,image=self.photoimg_top) 
      f_lbl.place(x=0,y=55,width=1530,height=720)
      
      # Frame 
      main_frame=Frame(f_lbl,bd=2,bg="white") 
      main_frame.place(x=1000,y=0,width=500,height=600)
      
      img_top1=Image.open(r"clg images\1_ZSbjnPGWPr2wko0pGH-gQg.png")
      img_top1=img_top1.resize((200,200),Image.LANCZOS)
      self.photoimg_top1=ImageTk.PhotoImage(img_top1)
      
      f_lbl=Label(main_frame,image=self.photoimg_top1) 
      f_lbl.place(x=300,y=0,width=200,height=200)
      
      # Developer info
      dev_label=Label(main_frame,text="Name : Rahul", font=("Arial",20,""),fg="blue",bg="white")
      dev_label.place(x=0,y=5)
      
      dev_label=Label(main_frame,text="Full Stack Developer", font=("Arial",20,""),fg="black",bg="white")
      dev_label.place(x=0,y=50)
      
      dev_label=Label(main_frame,text="Role:Lead Developer", font=("Arial",20,""),fg="blue",bg="white")
      dev_label.place(x=0,y=100)
      
      dev_label=Label(main_frame,text="Expertise:Python", font=("Arial",20,""),fg="black",bg="white")
      dev_label.place(x=0,y=150)
      
      img2=Image.open(r"clg images\Full-Stack-Developer.webp")
      img2=img2.resize((500,390),Image.LANCZOS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      f_lbl=Label(main_frame,image=self.photoimg2)
      f_lbl.place(x=0,y=210,width=500,height=390)
     
      
      

if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()