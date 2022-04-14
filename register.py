from cProfile import label
from email import message
from tkinter import*
from tkinter import ttk
from tkinter import font
import tkinter
from tkinter import messagebox
from turtle import width  #for stylish toolkit
from PIL import Image,ImageTk
from Student import Student
import os
from train import Train
from faceRecognition import Face_Recognition
from Attendance import Attendance
from help import Help
import tkinter
import mysql.connector


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
        b1 = Button(main_frame,image=self.photoimg6,borderwidth=0,cursor="hand2")
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






        
if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop() 