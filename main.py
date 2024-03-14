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




class Face_Recognition_System:
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
      img=Image.open(r"clg images\face attendance_banner.png")
      img=img.resize((1530,250),Image.LANCZOS)
      self.photoimg=ImageTk.PhotoImage(img)

      f_lbl=Label(self.root,image=self.photoimg)            
      f_lbl.place(x=0,y=0,width=1530,height=150) 


      #bg image
      img3=Image.open(r"clg images\backgroung_img.png")
      img3=img3.resize((1530,710),Image.LANCZOS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      bg_img=Label(self.root,image=self.photoimg3)
      bg_img.place(x=0,y=130,width=1530,height=710)

      title_lbl=Label(bg_img, font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
      title_lbl.place(x=0,y=0,width=1530,height=35)
      
      # ******************time*****************
      def time():
          string=strftime('%H:%M:%S %p')
          lbl.config(text=string)
          lbl.after(1000,time)
      
      lbl=Label(title_lbl,font=('time new roman',14,'bold'),background='white',foreground='blue')
      lbl.place(x=0,y=0,width=110,height=50)
      time()
      
      # student button
      img4=Image.open(r"clg images\Attendance-Monitoring.jpg")
      img4=img4.resize((220,220), Image.LANCZOS) 
      self.photoimg4=ImageTk.PhotoImage(img4)

      b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
      b1.place(x=200,y=100, width=220,height=220)

      b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
      b1_1.place(x=200,y=300,width=220,height=40)
     
      # Detect face button
      img5=Image.open(r"clg images\images (1).jpg")
      img5=img5.resize((220,220),Image.LANCZOS) 
      self.photoimg5=ImageTk.PhotoImage(img5)
        
      b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data) 
      b1.place(x=500,y=100, width=220, height=220)
        
      b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2", font=("times new roman",15,"bold"),bg="blue",fg="white")
      b1_1.place(x=500,y=300,width=220,height=40)

      # Attendace face button
      img6=Image.open(r"clg images\images.png")
      img6=img6.resize((220,220), Image.LANCZOS) 
      self.photoimg6=ImageTk.PhotoImage(img6)
    
      b1=Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.attendance_data)
      b1.place(x=800,y=100,width=220,height=220)
    
      b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15, "bold"),bg="blue",fg="white")
      b1_1.place(x=800,y=300,width=220,height=40)
    
      # Help face button
      img7 = Image.open(r"clg images\OIP.jpg")
      img7 = img7.resize((220, 220), Image.LANCZOS)  # Use Image.LANCZOS directly on resize
      self.photoimg7 = ImageTk.PhotoImage(img7)

      b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
      b1.place(x=1100, y=100, width=220, height=220)

      b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data,font=("times new roman", 15, "bold"), bg="blue", fg="white")
      b1_1.place(x=1100, y=300, width=220, height=40)

      
      #Train data
      img8=Image.open(r"clg images\images (2).jpg") 
      img8=img8.resize((220,220), Image.LANCZOS) 
      self.photoimg8=ImageTk.PhotoImage(img8)
    
      b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
      b1.place(x=200,y=380,width=220, height=220)

      b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2", font=("times new roman",15, "bold"),bg="blue",fg="white")
      b1_1.place(x=200,y=580, width=220,height=40)

      # Photos face button
      img9=Image.open(r"clg images\download.jpg")
      img9=img9.resize((220,220), Image.LANCZOS)
      self.photoimg9=ImageTk.PhotoImage(img9)

      b1=Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.open_img) 
      b1.place(x=500,y=380,width=220,height=220)

      b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15, "bold"),bg="blue",fg="white")
      b1_1.place(x=500,y=580,width=220,height=40)
      
      # developer face button
      img10=Image.open(r"clg images\images.jpg")
      img10=img10.resize((220,220), Image.LANCZOS) 
      self.photoimg10=ImageTk.PhotoImage(img10)

      b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data) 
      b1.place(x=800,y=380,width=220, height=220)

      b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman", 15, "bold"),bg="blue",fg="white")
      b1_1.place(x=800,y=580,width=220,height=40)

      # Exit face button
      img11=Image.open(r"clg images\c67cce0a22.jpg")
      img11=img11.resize((220,220), Image.LANCZOS)
      self.photoimg11=ImageTk.PhotoImage(img11)

      b1=Button(bg_img, image=self.photoimg11,cursor="hand2",command=self.iExit)
      b1.place(x=1100,y=380,width=220,height=220)

      b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman", 15, "bold"),bg="blue",fg="white")
      bg= b1_1.place(x=1100,y=580,width=220,height=40)
      
   def open_img(self):
       os.startfile("data")
       
   def iExit(self):
      self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project",parent=self.root)
      if self.iExit>0:
         self.root.destroy()

      #************************Functions button************************
      
   def student_details(self): 
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)
       
   def train_data(self): 
       self.new_window=Toplevel(self.root)
       self.app=Train(self.new_window)    
       
   def face_data(self): 
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition(self.new_window)   
      
   def attendance_data(self): 
      self.new_window=Toplevel(self.root)
      self.app=Attendance(self.new_window)  
      
   def developer_data(self): 
      self.new_window=Toplevel(self.root)
      self.app=Developer(self.new_window)       
   
   def help_data(self): 
      self.new_window=Toplevel(self.root)
      self.app=Help(self.new_window)  


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()