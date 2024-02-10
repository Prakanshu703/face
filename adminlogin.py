from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk    #pip install pillow
from student import Student
from tkinter import messagebox
import mysql.connector
from pwinput import pwinput
from main import Face_Recognition_System


def main():
  win=Tk()
  app=AdminLogin_window(win)
  win.mainloop()
  
def check_password(password):
    if len(password) >= 8:
        print("Password accepted!")
        return True
    else:
        print("Password should be at least 8 characters long. Please try again.")
        return False
   
  
class AdminLogin_window:
      
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\PRAKANSHU\Desktop\Face recognition system\clg images\—Pngtree—captivating acrylic art mesmerizing ocean_15222733 (1).jpg") 
        lbl_bg=Label(self.root,bg="black",image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)
        
 
        
        get_str=Label(frame,text="Welcome",font=("times new roman",25,"bold"),fg="black",bg="white")
        get_str.place(x=100,y=20)

        get_str1=Label(frame,text="Enter your credentials to access your account",font=("times new roman",12,"bold"),fg="#B3B3B3",bg="white")
        get_str1.place(x=17,y=65)   
        
        # label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=30,y=115)  
        
        self.txtuser=ttk.Entry(frame,font=("time new roman",10,))
        self.txtuser.place(x=30,y=140,width=270) 
        
        
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=30,y=200)  
        
        
        self.txtpass = ttk.Entry(frame, font=("times new roman", 12), show="*")
        self.txtpass.place(x=30, y=225, width=270)
 
         
        # LoginButton
        loginbtn=Button(frame,command=self.login,text="Sign in",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#57a1f8",border=0,activeforeground="white",activebackground="red")
        loginbtn.place(x=30,y=300,width=280,height=35)
        label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('times new roman',9))
        label.place(x=30, y=350)
        # RegisterButton
        registerbtn=Button(frame,width=6,text="Sign Up",border=0,command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="#57a1f8",activeforeground="white",activebackground="black")
        registerbtn.place(x=175,y=350)

        label2=Label(frame,text="Forgot your password?",fg='black',bg='white',font=('times new roman',9))
        label2.place(x=30, y=385)
        #forgetpasswordButton
        passwordbtn=Button(frame,width=15,text="Reset Password",border=0,command=self.forget_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="#57a1f8",activeforeground="white",activebackground="black")
        passwordbtn.place(x=170,y=385)

       
        
        
      
    def register_window(self):
      self.new_window=Toplevel(self.root)
      self.app=Register(self.new_window)
        
    def login(self):
        if self.txtuser.get()==""or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif not check_password(self.txtpass.get()):
            messagebox.showerror("Error", "Password should be at least 8 characters long. Please try again.")    
        elif self.txtuser.get()=="Rahul" and self.txtpass.get()=="12345678":
            messagebox.showinfo("success","Welcome to facial attendance recognition")
        else:
          conn=mysql.connector.connect(host="localhost",user="rahul",password="1234",database="mydata")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from admin where username=%s and password=%s",(
                                                                                   self.txtuser.get(),
                                                                                   self.txtpass.get()                                                                                                    
                                                                              ))
          
          row=my_cursor.fetchone()
          # print(row)
          if row==None:
            messagebox.showerror("Error","Invalid Username & Password")
          else:
            open_main=messagebox.askyesno("YesNo","Access only admin")
            if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
            else:  
                if not open_main:
                    return 
          conn.commit()
          conn.close()
        
    ########################################Reset Password##############################################
    
    def reset_pass(self):
      if self.txtuser.get()=="":
        messagebox.showerror("Error","Please enter your email",parent=self.root2)
      elif self.txt_newpass.get()=="":
        messagebox.showerror("Error","Please enter the new password",parent=self.root2)
      else:
         conn=mysql.connector.connect(host="localhost",user="rahul",password="1234",database="mydata")
         my_cursor=conn.cursor()
         query=("select * from admin where email=%s")
         value=(self.txtuser.get(),)
         my_cursor.execute(query,value) 
         row=my_cursor.fetchone()
         if row==None:
           messagebox.showerror("Error","Email not found",parent=self.root2)
         else:
           query=("update admin set password=%s where email=%s")
           value=(self.txt_newpass.get(),self.txtuser.get())
           my_cursor.execute(query,value)
           
           conn.commit()
           conn.close()
           messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)
           self.root2.destroy()
   
    
        
        
    ######################################Forget Password Window#######################################    
    def forget_password_window(self):
          if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the username to reset password")
          else:
           conn=mysql.connector.connect(host="localhost",user="rahul",password="1234",database="mydata")
           my_cursor=conn.cursor()
           query=("select * from admin where username=%s")
           value=(self.txtuser.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           #print(row)
           
           if row is None:
             messagebox.showerror("My Error","Please enter the valid username")
           else:
             conn.close()
             self.root2=Toplevel()
             self.root2.title("Forget Password")
             self.root2.geometry("340x450+610+170")
             
             l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
             l.place(x=0,y=10,relwidth=1)
             
             email=Label(self.root2,text="Enter your Email",font=("times new roman",15,"bold"),bg="white",fg="black")
             email.place(x=50,y=80)
             
             self.txt_email=ttk.Entry(self.root2,font=("times new roman",15))
             self.txt_email.place(x=50,y=120,width=250)
             
             new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
             new_password.place(x=50,y=210)
             
             self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
             self.txt_newpass.place(x=50,y=250,width=250)
             
             btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
             btn.place(x=120,y=290)
             
            
          
          
        
class Register:
          
    def __init__(self,root):
      
        
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
      
        
        #*******************variable******************
        self.var_username=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
      # ************bg image**************
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\PRAKANSHU\Desktop\Face recognition system\clg images\—Pngtree—captivating acrylic art mesmerizing ocean_15222733 (1).jpg")
        
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
         #***************main frame*****************
        frame=Frame(self.root,bg="white")
        frame.place(x=450,y=100,width=680,height=550)
        
        register_lbl=Label(frame,text="Join us today!",font=("times new roman",25,"bold"),fg="black",bg="white")
        register_lbl.place(x=250,y=20)
        
         #*******************label and entry*********************
        label = Label(frame,text="Sign up now to become a member",fg='#B3B3B3',bg='white',font=('times new roman',15,"bold"))
        label.place(x=200,y=60)
        #*******************row1
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="white")
        username.place(x=220,y=100)
        
        self.username_entry=ttk.Entry(frame,textvariable=self.var_username,font=("times new roman",15))
        self.username_entry.place(x=220,y=130,width=250)
        
         #***********************row2
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=220,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=220,y=200,width=250)
        
        #******************************row3
        
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=220,y=240)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=220,y=270,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=220,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=220,y=340,width=250)
        
        #***********************CheckButton*****************************
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to the Terms and Condition",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        self.checkbtn.place(x=70,y=390)
         
         #*********************Button******************************

        b1=Button(frame,command=self.register_data,text="Registeration",font=("times new roman",15,"bold"),fg="white",bd=3,relief=RIDGE,bg="#57a1f8",border=0,activeforeground="white",activebackground="red")
        b1.place(x=50,y=450,width=575,height=35)
        

        label = Label(frame,text="Have already an account?",fg='black',bg='white',font=('times new roman',9))
        label.place(x=50, y = 500)
        # RegisterButton
        
        b1=Button(frame,width=6,command=self.return_login,text="Login",borderwidth=0,font=("times new roman",10,"bold"),fg="#57a1f8",bd=3,relief=RIDGE,bg="white",border=0,activeforeground="white",activebackground="red")
        b1.place(x=200,y=500)
        
      
      #************************ Function declaration **********************
          
    def register_data(self):
        if self.var_username.get()=="" or self.var_email.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
          messagebox.showerror("Error","Password & confirm password must be same",parent=self.root)
        elif not check_password(self.var_pass.get()):
          messagebox.showerror("Error", "Password should be at least 8 characters long. Please try again.")
        elif self.var_check.get()==0:
          messagebox.showerror("Error","please agree our terms and condition",parent=self.root)
        else:
          conn=mysql.connector.connect(host="localhost",user="rahul",password="1234",database="mydata")
          my_cursor=conn.cursor()
          query=("select * from admin where email=%s")
          value=(self.var_email.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()
          if row is not None:
            messagebox.showerror("Error","User already exist , please try another email",parent=self.root)
          else:
            my_cursor.execute("insert into admin values(%s,%s,%s)",(
                                                                                    self.var_username.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_pass.get()    
                                                                                ))
        
            
          conn.commit()
          conn.close()
          messagebox.showinfo("Success","Register Successfully",parent=self.root)
          
    def return_login(self):
        self.root.destroy()    
        
                         
      
                                             
         
      
                                             
        

if __name__=="__main__":
 main()