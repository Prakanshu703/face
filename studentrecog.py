from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student import Student
from tkinter import messagebox
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help



class Student_Face_Recognition_System:
   def __init__(self,root):                    
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")
      
                                                                                  
      
      
      #**********************Variables******************************
      
      #self.var_dep= StringVar()
      #self.var_course = StringVar()
      #self.var_year= StringVar()
      #self.var_semester=StringVar()
      #self.va_std_id=StringVar()
      #self.var_std_name=StringVar()
      #self.var_div=StringVar()
      #self.var_roll=StringVar()
      #self.var_gender=StringVar()
      #self.var_dob= StringVar()
      #self.var_email= StringVar()
      #self.var_phone= StringVar()
      #self.var_address=StringVar()
      #self.var_teacher= StringVar()
      
      

      # first imag
      img=Image.open(r"clg images\0_u190t7LKR908teW7.jpg")
      img=img.resize((500,130),Image.LANCZOS)
      self.photoimg=ImageTk.PhotoImage(img)

      f_lbl=Label(self.root,image=self.photoimg)            
      f_lbl.place(x=0,y=0,width=500,height=130)

      # second image

      img1=Image.open(r"clg images\facial_recognition_reuters-759.jpg")
      img1=img1.resize((500,130), Image.LANCZOS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      f_lbl=Label(self.root,image= self.photoimg1)
      f_lbl.place(x=500,y=0,width=500,height=130)

      #third imag
      img2=Image.open(r"clg images\face-recognition-ar-hologram-screen-smart-technology_53876-167350 (1).webp")
      img2=img2.resize((550,130),Image.LANCZOS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      f_lbl=Label(self.root,image=self.photoimg2)
      f_lbl.place(x=1000,y=0,width=550,height=130)

      #bg image
      img3=Image.open(r"clg images\W1M7KR.jpg")
      img3=img3.resize((1530,710),Image.LANCZOS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      bg_img=Label(self.root,image=self.photoimg3)
      bg_img.place(x=0,y=130,width=1530,height=710)

      title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
      title_lbl.place(x=0,y=0,width=1530,height=45)
      
      # ******************time*****************
      def time():
          string=strftime('%H:%M:%S %p')
          lbl.config(text=string)
          lbl.after(1000,time)
      
      lbl=Label(title_lbl,font=('time new roman',14,'bold'),background='white',foreground='blue')
      lbl.place(x=0,y=0,width=110,height=50)
      time()
      
     
      # Detect face button
      img5=Image.open(r"clg images\images (1).jpg")
      img5=img5.resize((220,220),Image.LANCZOS) 
      self.photoimg5=ImageTk.PhotoImage(img5)
        
      b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data) 
      b1.place(x=500,y=100, width=220, height=220)
        
      b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2", font=("times new roman",15,"bold"),bg="blue",fg="white")
      b1_1.place(x=500,y=300,width=220,height=40)


      #************************Functions button************************
      
   def face_data(self): 
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition(self.new_window)   
      


if __name__=="__main__":
    root=Tk()
    obj=Student_Face_Recognition_System(root)
    root.mainloop()