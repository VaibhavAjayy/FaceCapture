from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from PIL import Image,ImageTk
from click import command
from matplotlib.pyplot import title
import mysql.connector
from cProfile import label
from tkinter import*
from tkinter import ttk
from tkinter import font
import tkinter  #for stylish toolkit
from PIL import Image,ImageTk
from Student import Student
import os
from train import Train
from faceRecognition import Face_Recognition
from Attendance import Attendance
from help import Help
import tkinter
from main import face_recognition

def main():
    win = Tk()
    obj = Login(win)
    win.mainloop()


class Login:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("FACE RECOGNITION BASED ATTENDANCE SYSTEM")

        # background image
        img3 = Image.open(r"Images\1519797201497.jpg")
        img3 = img3.resize((1350,700),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x =0, y = 0, width = 1350, height = 700) 

        title_lbl = Label(bg_img,text="FACE RECOGNITION BASED ATTENDANCE SYSTEM", font = ("Arial Black",25,"bold"),bg = "black",fg="white")
        title_lbl.place(x = 0, y = 0, width= 1290, height= 35)

        main_frame = Frame(self.root,bg="black")
        main_frame.place(x=470,y=120,width=350,height=450)

        img_main = Image.open(r"Images\login-illustration-letter-cubes-forming-word-36025252.jpg")
        img_main  = img_main.resize((250,100),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg_main  = ImageTk.PhotoImage(img_main)

        first_lbl = Label(image = self.photoimg_main,bg='black')
        first_lbl.place(x = 520, y = 124, width=250,height=120)

        getStarted_label = Label(main_frame,text="GET STARTED",font =("Arial",20,"bold"),bg ="black",fg="white")
        getStarted_label.place(x = 75, y = 120)

        userName_label = Label(main_frame,text="USERNAME",font =("Arial",15,"bold"),bg ="black",fg="white")
        userName_label.place(x = 10, y = 160)

        self.userName_Entry = ttk. Entry(main_frame,width=20,font =("Arial",8,"bold"))
        self.userName_Entry.place(x = 140, y = 165,width=200)

        password_label = Label(main_frame,text="PASSWORD",font =("Arial",15,"bold"),bg ="black",fg="white")
        password_label.place(x = 10, y = 210)

        self.password_Entry = ttk. Entry(main_frame,width=20,font =("Arial",8,"bold"))
        self.password_Entry.place(x = 140, y = 215,width=200)

        #login button
        login_button = Button(main_frame,text="LOGIN",command=self.login,width =19,font=("Arial",13,"bold"),bg ="white",fg= "darkgreen",activeforeground="darkgreen",activebackground="white")
        login_button.place(x = 75, y = 255)

        #register button
        register_button = Button(main_frame,command=self.register_window,text="NEW USER REGISTER",width =19,font=("Arial",13,"bold"),bg ="black",fg= "white",activeforeground="white",activebackground="black")
        register_button.place(x = 10, y = 300)

         #forgotPassword button
        forgotPassword_button = Button(main_frame,command=self.forgot_password,text="FORGOT PASSWORD ?",width =19,font=("Arial",13,"bold"),bg ="black",fg= "white",activeforeground="white",activebackground="black")
        forgotPassword_button.place(x = 10, y = 355)
    
    def register_window(self):
        self.newWindow = Toplevel(self.root)
        self.obj = Register(self.newWindow)

    def login(self):
        if self.userName_Entry.get() == "" or self.password_Entry == "":
            messagebox.showerror("Error","All Fields required")
        elif self.userName_Entry.get()== "vasu" and self.password_Entry.get()=="gocorona": 
            messagebox.showinfo("Sucess","WELCOME")
        else:
            conn = mysql.connector.connect(host = "localhost",username = "root",password = "12345",database = "face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password = %s ",(
                                                                                         self.userName_Entry.get(),
                                                                                         self.password_Entry.get()
                                                                                         ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main = messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.newWindow  = Toplevel(self.root)
                    self.obj = face_recognition(self.newWindow)
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()
    #reset password
    def reset_pass(self):
        if self.sques_combo.get()=="Select":
            messagebox.showerror("Error","Select the security question")
        elif self.sans_Entry.get()=="":
            messagebox.showerror("Error","Please enter the answer")
        elif self.NewPassword_Entry.get()=="":
            messagebox.showerror("Error","Please enter the new password")
        else:
            conn = mysql.connector.connect(host = "localhost",username = "root",password = "12345",database = "face_recognition")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and SecurityQuestion=%s and SecurityAns=%s")
            value = (self.userName_Entry.get(),self.sques_combo.get(),self.sans_Entry.get())
            my_cursor.execute(query,value)

            row = my_cursor.fetchone()
            
            if row == None:
                messagebox.showerror("Error","Please enter correct answer")
            else:
                query = ("update register set password = %s where email =%s")
                value = (self.NewPassword_Entry.get(),self.userName_Entry.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Password reset Successfully, Please login again",parent=self.root2)




    #forgot password window
    def forgot_password(self):
        if self.userName_Entry.get() == "":
            messagebox.showerror("Error","Please enter email to reset password")
        else:
            conn = mysql.connector.connect(host = "localhost",username = "root",password = "12345",database = "face_recognition")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.userName_Entry.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            
            if row == None:
                messagebox.showerror("Error","Please enter Valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("350x450+470+120")

                l_lbl = Label(self.root2,text="Forgot Password",font =("Arial",15,"bold"),bg ="white",fg="black")
                l_lbl.place(x = 0, y =10,relwidth=1)

                sques_lbl = Label(self.root2,text="SECURITY Q",font =("Arial",15,"bold"),bg ="white",fg="black")
                sques_lbl.place(x = 80, y =50)

                sques_combo = ttk.Combobox(self.root2,font =("Arial",12,"bold"),state = "read only",width=12)
                sques_combo["values"]=("Select","Your pet name","Your fav fruit")
                sques_combo.current(0)
                sques_combo.place(x = 80, y =80,width=200)

        
                sans_lbl = Label(self.root2,text="SECURITY A",font =("Arial",15,"bold"),bg ="white",fg="black")
                sans_lbl.place(x = 80, y =110)

                sans_Entry = ttk. Entry(self.root2,width=20,font =("Arial",12,"bold"))
                sans_Entry.place(x = 80, y =140,width=200)

                NewPassword_lbl = Label(self.root2,text="New Password",font =("Arial",15,"bold"),bg ="white",fg="black")
                NewPassword_lbl.place(x = 80, y =180)

                NewPassword_Entry = ttk. Entry(self.root2,width=20,font =("Arial",12,"bold"))
                NewPassword_Entry.place(x = 80, y =220,width=200)

                b1_button = Button(self.root2,text="RESET",command=self.reset_pass,width =16,font=("Arial",15,"bold"),bg ="darkgreen",fg= "white")
                b1_button.place(x = 80, y = 280)
                      

class Register:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("REGISTER")

        #text variable
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_sques = StringVar()
        self.var_sans = StringVar()
        self.var_pass = StringVar()
        self.var_conpas = StringVar()    
       

        # background image
        img3 = Image.open(r"Images\360_F_137574978_zQ5OsEYsizBPKE1FT2NWQTjdUoFpCsR1.jpg")
        img3 = img3.resize((1350,700),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x =0, y = 0, width = 1350, height = 700) 

        # left image
        img4 = Image.open(r"Images\assorted-reading-books.jpg")
        img4 = img4.resize((450,500),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img1 = Label(self.root,image = self.photoimg4)
        bg_img1.place(x =50, y = 100, width = 450, height = 500)

        main_frame = Frame(self.root,bg="white")
        main_frame.place(x=500,y=100,width=700,height=500) 

        first_lbl = Label(main_frame,text="REGISTER HERE",font =("Arial",20,"bold"),bg ="black",fg="white")
        first_lbl.place(x = 20, y =20)

        fname_lbl = Label(main_frame,text="FIRST NAME",font =("Arial",15,"bold"),bg ="white",fg="black")
        fname_lbl.place(x = 20, y =90)

        fname_Entry = ttk. Entry(main_frame,textvariable=self.var_fname,width=20,font =("Arial",12,"bold"))
        fname_Entry.place(x = 150, y =90,width=200)

        lname_lbl = Label(main_frame,text="LAST NAME",font =("Arial",15,"bold"),bg ="white",fg="black")
        lname_lbl.place(x = 355, y =90)

        lname_Entry = ttk. Entry(main_frame,textvariable=self.var_lname,width=20,font =("Arial",12,"bold"))
        lname_Entry.place(x = 490, y =90,width=200)

        cont_lbl = Label(main_frame,text="CONTACT NO.",font =("Arial",15,"bold"),bg ="white",fg="black")
        cont_lbl.place(x = 20, y =140)

        cont_Entry = ttk. Entry(main_frame,textvariable=self.var_contact,width=20,font =("Arial",12,"bold"))
        cont_Entry.place(x = 170, y =140,width=200)

        email_lbl = Label(main_frame,text="EMAIL",font =("Arial",15,"bold"),bg ="white",fg="black")
        email_lbl.place(x = 390, y =140)

        email_Entry = ttk. Entry(main_frame,textvariable=self.var_email,width=20,font =("Arial",12,"bold"))
        email_Entry.place(x = 490, y =140,width=200)

        sques_lbl = Label(main_frame,text="SECURITY Q",font =("Arial",15,"bold"),bg ="white",fg="black")
        sques_lbl.place(x = 20, y =200)

        sques_combo = ttk.Combobox(main_frame,textvariable=self.var_sques,font =("Arial",12,"bold"),state = "read only",width=12)
        sques_combo["values"]=("Select","Your pet name","Your fav fruit")
        sques_combo.current(0)
        sques_combo.place(x = 170, y =200,width=200)

 
        sans_lbl = Label(main_frame,text="SECURITY A",font =("Arial",15,"bold"),bg ="white",fg="black")
        sans_lbl.place(x = 375, y =200)

        sans_Entry = ttk. Entry(main_frame,textvariable=self.var_sans,width=20,font =("Arial",12,"bold"))
        sans_Entry.place(x = 500, y =200,width=190)

        newpass_lbl = Label(main_frame,text="PASSWORD",font =("Arial",15,"bold"),bg ="white",fg="black")
        newpass_lbl.place(x = 20, y =260)

        newpass_Entry = ttk. Entry(main_frame,textvariable=self.var_pass,width=20,font =("Arial",12,"bold"))
        newpass_Entry.place(x = 170, y =260,width=200)

        confirmpas_lbl = Label(main_frame,text="CONFIRM",font =("Arial",15,"bold"),bg ="white",fg="black")
        confirmpas_lbl.place(x = 375, y =260)

        confirmpas_Entry = ttk. Entry(main_frame,textvariable=self.var_conpas,width=20,font =("Arial",12,"bold"))
        confirmpas_Entry.place(x = 500, y =260,width=190)
        
        #checkbutton
        self.var_chk = IntVar()
        chk_button = Checkbutton(main_frame,variable=self.var_chk,text="I Agree",width =19,font=("Arial",15,"bold"),bg ="white",fg= "red",activeforeground="red",activebackground="white",onvalue=1,offvalue=0)
        chk_button.place(x = 20, y = 300)

        img5 = Image.open(r"Images\istockphoto-1300307175-612x612.jpg")
        img5 = img5.resize((300,70),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(main_frame,command=self.register_data,image=self.photoimg5,borderwidth=0,cursor="hand2")
        b1.place(x= 30,y=350,width=300)

        img6 = Image.open(r"Images\login-button-square-d-push-sign-177297913.jpg")
        img6 = img6.resize((300,70),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(main_frame,command=self.return_login,image=self.photoimg6,borderwidth=0,cursor="hand2")
        b1.place(x=350,y=350,width=300)

    #register data function
    def register_data(self):
        if self.var_fname.get() =="" or self.var_email.get() =="" or self.var_sques.get() == "Select":
            messagebox.showerror("Error","All Fields Required")
        elif self.var_pass.get()!=self.var_conpas.get():
            messagebox.showerror("Error","confirm not matches to the password you entered")
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error","Please check the I Agree box")
        else:
            conn = mysql.connector.connect(host = "localhost",username = "root",password = "12345",database = "face_recognition")
            my_cursor = conn.cursor()
            query = ("select * from register where email =%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already exist,Change the Email Entered")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                      self.var_fname.get(),
                                                                                      self.var_lname.get(),
                                                                                      self.var_contact.get(),
                                                                                      self.var_email.get(),
                                                                                      self.var_sques.get(),
                                                                                      self.var_sans.get(),
                                                                                      self.var_pass.get()
                                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")
            self.root.destroy()
    def return_login(self):
        self.root.destroy()

class face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("FACE RECOGNITION BASED ATTENDANCE SYSTEM")
        
        # 1st image
        img = Image.open(r"Images\facialrecognition1.png")
        img = img.resize((500,150),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg = ImageTk.PhotoImage(img)

        first_lbl = Label(self.root,image = self.photoimg)
        first_lbl.place(x = 0, y = 0, width=500,height=150)

        # 2nd image
        img1 = Image.open(r"Images\Learn-Facial-Recognition-scaled.jpg")
        img1 = img1.resize((400,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root,image = self.photoimg1)
        first_lbl.place(x = 500, y = 0, width=400,height=150)
         
        # 3rd image
        img2 = Image.open(r"Images\DRL-ICA-91521-scaled.jpeg")
        img2 = img2.resize((379,150),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_lbl = Label(self.root,image = self.photoimg2)
        first_lbl.place(x = 900, y = 0, width=379,height=150)

        # background image
        img3 = Image.open(r"Images\pngtree-modern-double-color-futuristic-neon-background-image_351866.jpg")
        img3 = img3.resize((1350,600),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x =0, y = 150, width = 1350, height = 600)

        title_lbl = Label(bg_img,text="FACE RECOGNITION BASED ATTENDANCE SYSTEM", font = ("Arial Black",25,"bold"),bg = "white",fg="black")
        title_lbl.place(x = 0, y = 0, width= 1290, height= 35)

        # Student button
        img4 = Image.open(r"Images\istockphoto-1171062918-612x612.jpg")
        img4 = img4.resize((150,150),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg4 = ImageTk.PhotoImage(img4)

        #creating button
        b1 = Button(bg_img,image = self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x = 130, y =100, width=120, height=120)

        #creating button
        b1_1 = Button(bg_img,text = "STUDENT DETAILS",command=self.student_details,cursor="hand2",font = ("Arial Black",8,"bold"),bg = "darkblue",fg="white")
        b1_1.place(x = 130, y =200, width=120, height=30)

        # detect face button
        img5 = Image.open(r"Images\fr-1200.png")
        img5 = img5.resize((150,150),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg5 = ImageTk.PhotoImage(img5)

        #creating button
        b1 = Button(bg_img,image = self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x = 400, y =100, width=120, height=120)

        #creating button
        b1_1 = Button(bg_img,text = "FACE DETECTOR",cursor="hand2",command=self.face_data,font = ("Arial Black",8,"bold"),bg = "darkblue",fg="white")
        b1_1.place(x = 400, y =200, width=120, height=30)

        # Attendace button
        img6 = Image.open(r"Images\FR-Facial-Recognition-Web-Responsive-Banner-30-may-2020_1-1320x500-1.jpg")
        img6 = img6.resize((150,150),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg6 = ImageTk.PhotoImage(img6)

        #creating button
        b1 = Button(bg_img,image = self.photoimg6,cursor="hand2",command=self.Attendance_data)
        b1.place(x = 700, y =100, width=120, height=120)

        #creating button
        b1_1 = Button(bg_img,text = "ATTENDANCE",cursor="hand2",command=self.Attendance_data,font = ("Arial Black",8,"bold"),bg = "darkblue",fg="white")
        b1_1.place(x = 700, y =200, width=120, height=30)

        # Help button
        img7 = Image.open(r"Images\Service-Help-Desk.png")
        img7 = img7.resize((150,150),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg7 = ImageTk.PhotoImage(img7)

        #creating button
        b1 = Button(bg_img,image = self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x = 1000, y =100, width=120, height=120)

        #creating button
        b1_1 = Button(bg_img,text = "HELP DESK",cursor="hand2",command=self.help_data,font = ("Arial Black",8,"bold"),bg = "darkblue",fg="white")
        b1_1.place(x = 1000, y =200, width=120, height=30)

        # Train data button
        img8 = Image.open(r"Images\Service-Help-Desk.png")
        img8 = img8.resize((150,150),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg8 = ImageTk.PhotoImage(img8)

        #creating button
        b1 = Button(bg_img,image = self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x = 250, y =300, width=120, height=120)

        #creating button
        b1_1 = Button(bg_img,text = "TRAIN DATA",cursor="hand2",command=self.train_data,font = ("Arial Black",8,"bold"),bg = "darkblue",fg="white")
        b1_1.place(x = 250, y =400, width=120, height=30)

        # Photos data button
        img9 = Image.open(r"Images\about-us-hero-image-t.jpg")
        img9 = img9.resize((150,150),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg9 = ImageTk.PhotoImage(img9)

        #creating button
        b1 = Button(bg_img,image = self.photoimg9,cursor="hand2",command=self.open_image)
        b1.place(x = 550, y =300, width=120, height=120)

        #creating button
        b1_1 = Button(bg_img,text = "PHOTOS",cursor="hand2",command=self.open_image,font = ("Arial Black",8,"bold"),bg = "darkblue",fg="white")
        b1_1.place(x = 550, y =400, width=120, height=30)

        # Exit data button
        img10 = Image.open(r"Images\download (2).jpg")
        img10 = img10.resize((150,150),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg10 = ImageTk.PhotoImage(img10)

        #creating button
        b1 = Button(bg_img,image = self.photoimg10,cursor="hand2",command=self.exit)
        b1.place(x = 850, y =300, width=120, height=120)

        #creating button
        b1_1 = Button(bg_img,text = "EXIT",cursor="hand2",command=self.exit,font = ("Arial Black",8,"bold"),bg = "darkblue",fg="white")
        b1_1.place(x = 850, y =400, width=120, height=30)
    
    def open_image(self):
        os.startfile("Data")

       
    #-------------Functions Button-----------------------------
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.var = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.var = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.var = Face_Recognition(self.new_window)

    def Attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.var = Attendance(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.var = Help(self.new_window)

    def exit(self):
        self.exit = tkinter.messagebox.askyesno("FACE RECOGNITION","YOU SURE YOU WANNA EXIT",parent =self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return






if __name__ == "__main__":
    main()