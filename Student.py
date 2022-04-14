from cProfile import label
from distutils.debug import DEBUG
from logging import exception
from operator import ge
from optparse import Values
import string
from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import width  #for stylish toolkit
from PIL import Image,ImageTk
from cv2 import COLOR_BGR2GRAY, COLOR_GRAY2BGR
from flask import g
from matplotlib.pyplot import connect, fill, get
from tkinter import messagebox
import mysql.connector
from numpy import delete, var 
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("FACE RECOGNITION BASED ATTENDANCE SYSTEM")


        #------------------variables--------------------------
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_session = StringVar()
        self.var_Semester = StringVar()
        self.var_Id= StringVar()
        self.var_Name = StringVar()
        self.var_Batch = StringVar()
        self.var_RollNo = StringVar()
        self.var_Email = StringVar()
        self.var_Teacher = StringVar()

        # 1st image
        img = Image.open(r"Images\our-students.jpg")
        img = img.resize((500,150),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg = ImageTk.PhotoImage(img)

        first_lbl = Label(self.root,image = self.photoimg)
        first_lbl.place(x = 0, y = 0, width=500,height=150)

        # 2nd image
        img1 = Image.open(r"Images\Student-Well-Being_1410x820-705x410.jpg")
        img1 = img1.resize((400,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root,image = self.photoimg1)
        first_lbl.place(x = 500, y = 0, width=400,height=150)
         
        # 3rd image
        img2 = Image.open(r"Images\cartoon-students-vector-25730419.jpg")
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

        title_lbl = Label(bg_img,text="STUDENT DETAILS", font = ("Arial Black",25,"bold"),bg = "white",fg="red")
        title_lbl.place(x = 0, y = 0, width= 1290, height= 35)

        main_frame = Frame(bg_img,bd=2,bg="lightgreen")
        main_frame.place(x=5,y=37,width=1280,height=500)

        # left label frame
        left_frame = LabelFrame(main_frame,bd=5,bg="lightyellow",relief=RIDGE,text="STUDENT DETAILS",font =("Arial",12,"bold"))
        left_frame.place(x = 20,y=10,width=590,height=450)

        img_left = Image.open(r"Images\depositphotos_26419797-stock-photo-children-reading-books.jpg")
        img_left  = img_left .resize((570,100),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg_left  = ImageTk.PhotoImage(img_left)

        first_lbl = Label(left_frame,image = self.photoimg_left)
        first_lbl.place(x = 5, y = 0, width=570,height=100)

        #current course
        current_course_frame = LabelFrame(left_frame,bd=5,bg="lightyellow",relief=RIDGE,text="CURRENT COURSE INFO",font =("Arial",12,"bold"))
        current_course_frame.place(x = 5,y=110,width=570,height=100)
         
        #department
        department_label = Label(current_course_frame,text="DEPARTMENT",font =("Arial",8,"bold"),bg ="lightyellow")
        department_label.grid(row=0,column=0,padx= 5,sticky=W)

        department_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font =("Arial",8,"bold"),state = "read only",width=20)
        department_combo["values"]=("Select Department","COE","IT","SE","ECE")
        department_combo.current(0)
        department_combo.grid(row=0,column=1,padx= 2, pady= 5)

        #Course
        Course_label = Label(current_course_frame,text="YEAR",font =("Arial",8,"bold"),bg ="lightyellow")
        Course_label.grid(row=0,column=2,padx= 5,sticky=W)

        Course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font =("Arial",8,"bold"),state = "read only",width=20)
        Course_combo["values"]=("Select Year","First Year","Second Year","Third Year","Fourth Year")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx= 2, pady= 5,sticky=W)

        #Year
        Year_label = Label(current_course_frame,text="SESSION",font =("Arial",8,"bold"),bg ="lightyellow")
        Year_label.grid(row=1,column=0,padx= 5,sticky=W)

        Year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_session,font =("Arial",8,"bold"),state = "read only",width=20)
        Year_combo["values"]=("Select Session","2020-21","2021-22","2022-23","2023-24")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx= 2, pady= 5,sticky=W)

        #Semester
        Semester_label = Label(current_course_frame,text="SEMESTER",font =("Arial",8,"bold"),bg ="lightyellow")
        Semester_label.grid(row=1,column=2,padx= 5,sticky=W)

        Semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Semester,font =("Arial",8,"bold"),state = "read only",width=20)
        Semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx= 2, pady= 5,sticky=W)

      
        #Student info
        Student_info_frame = LabelFrame(left_frame,bd=5,bg="lightyellow",relief=RIDGE,text="STUDENT INFO",font =("Arial",12,"bold"))
        Student_info_frame.place(x = 5,y=210,width=570,height=210)
        
        #Student_ID
        Student_ID_label = Label(Student_info_frame,text="STUDENT_ID:",font =("Arial",8,"bold"),bg ="lightyellow")
        Student_ID_label.grid(row=0,column=0,padx= 5,sticky=W)

        Student_ID_Entry = ttk. Entry(Student_info_frame,textvariable=self.var_Id,width=15,font =("Arial",8,"bold"))
        Student_ID_Entry.grid(row=0,column=1,padx= 5,sticky=W)

        #Student_Name
        Student_Name_label = Label(Student_info_frame,text="STUDENT_NAME:",font =("Arial",8,"bold"),bg ="lightyellow")
        Student_Name_label.grid(row=0,column=2,padx= 5,pady=5,sticky=W)

        Student_Name_Entry = ttk. Entry(Student_info_frame,textvariable=self.var_Name,width=15,font =("Arial",8,"bold"))
        Student_Name_Entry.grid(row=0,column=3,padx= 5,pady=5,sticky=W)

        #Batch
        Batch_label = Label(Student_info_frame,text="BATCH",font =("Arial",8,"bold"),bg ="lightyellow")
        Batch_label.grid(row=1,column=0,padx= 5,pady=10,sticky=W)

        Batch_combo = ttk.Combobox(Student_info_frame,textvariable=self.var_Batch,font =("Arial",8,"bold"),state = "read only",width=12)
        Batch_combo["values"]=("Select Batch","A","B")
        Batch_combo.current(0)
        Batch_combo.grid(row=1,column=1,padx= 5, pady= 10,sticky=W)

        #Student_RollNo
        Student_RollNo_label = Label(Student_info_frame,text="STUDENT_ROLLNO:",font =("Arial",8,"bold"),bg ="lightyellow")
        Student_RollNo_label.grid(row=1,column=2,padx= 5,pady=5,sticky=W)

        Student_RollNo_Entry = ttk. Entry(Student_info_frame,textvariable=self.var_RollNo,width=15,font =("Arial",8,"bold"))
        Student_RollNo_Entry.grid(row=1,column=3,padx= 5,pady=5,sticky=W)

        #Student_Email
        Student_Email_label = Label(Student_info_frame,text="EMAIL:",font =("Arial",8,"bold"),bg ="lightyellow")
        Student_Email_label.grid(row=2,column=0,padx= 5,pady=5,sticky=W)

        Student_Email_Entry = ttk. Entry(Student_info_frame,textvariable=self.var_Email,width=15,font =("Arial",8,"bold"))
        Student_Email_Entry.grid(row=2,column=1,padx= 5,pady=5,sticky=W)

        #Teacher_Name
        Teacher_Name_label = Label(Student_info_frame,text="TEACHER_NAME:",font =("Arial",8,"bold"),bg ="lightyellow")
        Teacher_Name_label.grid(row=2,column=2,padx= 5,pady=5,sticky=W)

        Teacher_Name_Entry = ttk. Entry(Student_info_frame,textvariable=self.var_Teacher,width=15,font =("Arial",8,"bold"))
        Teacher_Name_Entry.grid(row=2,column=3,padx= 5,pady=5,sticky=W)

        #radio button
        self.var_radio1 = StringVar()
        radio_button1 = ttk.Radiobutton(Student_info_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio_button1.grid(row=3,column=0)
        
        radio_button2 = ttk.Radiobutton(Student_info_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio_button2.grid(row=3,column=2)

        #button frame
        button_frame = Frame(Student_info_frame,bd=2,relief=RIDGE)
        button_frame.place(x = 0,y=125,width=560,height=29)

        save_button = Button(button_frame,text="SAVE",command=self.add_data,width =19,font=("Arial",8,"bold"),bg ="blue",fg= "white")
        save_button.grid(row=0,column=1)

        update_button = Button(button_frame,text="UPDATE",command=self.update_data,width =19,font=("Arial",8,"bold"),bg ="blue",fg= "white")
        update_button.grid(row=0,column=2)
        
        delete_button = Button(button_frame,text="DELETE",command=self.delete_data,width =19,font=("Arial",8,"bold"),bg ="blue",fg= "white")
        delete_button.grid(row=0,column=3)

        reset_button = Button(button_frame,text="RESET",command=self.reset_data,width =19,font=("Arial",8,"bold"),bg ="blue",fg= "white")
        reset_button.grid(row=0,column=4)

        #button frame
        button_frame1 = Frame(Student_info_frame,bd=2,relief=RIDGE)
        button_frame1.place(x = 0,y=153,width=560,height=29)

        take_photo_button = Button(button_frame1,text="TAKE PHOTO SAMPLE",command=self.generate_dataset,width =39,font=("Arial",8,"bold"),bg ="blue",fg= "white")
        take_photo_button.grid(row=0,column=0)

        update_photo_button = Button(button_frame1,text="UPDATE PHOTO SAMPLE",width =38,font=("Arial",8,"bold"),bg ="blue",fg= "white")
        update_photo_button.grid(row=0,column=1)

        # Right label frame
        Right_frame = LabelFrame(main_frame,bd=5,bg="lightyellow",relief=RIDGE,text="STUDENT DETAILS",font =("Arial",12,"bold"))
        Right_frame.place(x = 650,y=10,width=595,height=450)

        img_right = Image.open(r"Images\1519797201497.jpg")
        img_right  = img_right .resize((570,100),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg_right  = ImageTk.PhotoImage(img_right)

        first_lbl = Label(Right_frame,image = self.photoimg_right)
        first_lbl.place(x = 5, y = 0, width=570,height=100)
   
        #------------TABLE FRAME---------------------------------------------
        Table_frame = Frame(Right_frame,bd=5,bg="lightyellow",relief=RIDGE)
        Table_frame.place(x = 5,y=110,width=570,height=310)

        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.Student_Table=ttk.Treeview(Table_frame,column=("Dep","Year","Session","Semester","Id","Name","Batch","RollNo","Email","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)

        self.Student_Table.heading("Dep",text="DEPARTMENT")
        self.Student_Table.heading("Year",text="YEAR")
        self.Student_Table.heading("Session",text="SESSION")
        self.Student_Table.heading("Semester",text="SEMESTER")
        self.Student_Table.heading("Id",text="ID")
        self.Student_Table.heading("Name",text="NAME")
        self.Student_Table.heading("Batch",text="BATCH")
        self.Student_Table.heading("RollNo",text="ROLL_NO")
        self.Student_Table.heading("Email",text="EMAIL")
        self.Student_Table.heading("Teacher",text="TEACHER")
        self.Student_Table.heading("Photo",text="PHOTO_SAMPLE_STATUS")
        self.Student_Table["show"]="headings"

        self.Student_Table.column("Dep",width=100)
        self.Student_Table.column("Year",width=100)
        self.Student_Table.column("Session",width=100)
        self.Student_Table.column("Semester",width=100)
        self.Student_Table.column("Id",width=100)
        self.Student_Table.column("Name",width=100)
        self.Student_Table.column("Batch",width=100)
        self.Student_Table.column("RollNo",width=100)
        self.Student_Table.column("Email",width=100)
        self.Student_Table.column("Teacher",width=100)
        self.Student_Table.column("Photo",width=150)

        self.Student_Table.pack(fill=BOTH,expand=1)
        self.Student_Table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

     
     #------------------Function Declaration----------------
    
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_Name.get()== "" or self.var_Id.get() =="":
            messagebox.showerror("Error","All Fields are required",parent= self.root)
        else:
            try: 
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "12345",database = "face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                   self.var_dep.get(),self.var_year.get(),self.var_session.get(),self.var_Semester.get(),self.var_Id.get(),
                   self.var_Name.get(),self.var_Batch.get(),self.var_RollNo.get(), self.var_Email.get(),self.var_Teacher.get(),
                   self.var_radio1.get() ))                                                                                                                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","STUDENT DETAILS ADDED SUCCESSFULLY",parent = self.root)
            except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)} ",parent = self.root)

    #-----------------------------Fetching Data------------------------      
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost",username = "root",password = "12345",database = "face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        my_data = my_cursor.fetchall()


        if len(my_data)!=0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for i in my_data:
                self.Student_Table.insert("",END,values = i)
            conn.commit()
        conn.close()
    #---------------------get cursor function------------------------------------
    def get_cursor(self,event = ""):
        cursor_focus = self.Student_Table.focus()
        content = self.Student_Table.item(cursor_focus)
        data = content["values"] 

        self.var_dep.set(data[0]) 
        self.var_year.set(data[1])
        self.var_session.set(data[2]),
        self.var_Semester.set(data[3]),
        self.var_Id.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Batch.set(data[6]),
        self.var_RollNo.set(data[7]),
        self.var_Email.set(data[8]),
        self.var_Teacher.set(data[9]),
        self.var_radio1.set(data[10])
    
    #---------------Update function---------------------------
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_Name.get()== "" or self.var_Id.get() =="":
            messagebox.showerror("Error","All Fields are required",parent= self.root)
        else:
            try:
                Update = messagebox.askyesno("UPDATE","Do you want to update any info of this student",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password = "12345",database = "face_recognition")
                    my_cursor = conn.cursor()
                    sql = "update student set name=%s,photo_sample=%s where ID = %s"
                    my_cursor.execute(sql,(self.var_Name.get(),self.var_radio1.get(),self.var_Id.get()))                                                                                                                                                                                                               
                                                                                                                                                                                          
                else: 
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Info Updated Successfully",parent=self.root)           
                conn.commit()
                self.fetch_data()
                conn.close()            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    #-----------------delete function-----------------------------
    def delete_data(self):
        if self.var_Id.get() == "":
            messagebox.showerror("Error","Student ID Required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password = "12345",database = "face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where ID = %s"
                    val = (self.var_Id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Info deleted",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    #------------------reset function--------------------------------
    def reset_data(self):
        self.var_dep.set("Select Department") 
        self.var_year.set("Select Year")
        self.var_session.set("Select Session"),
        self.var_Semester.set("Select Semester"),
        self.var_Id.set(""),
        self.var_Name.set(""),
        self.var_Batch.set("Select Batch"),
        self.var_RollNo.set(""),
        self.var_Email.set(""),
        self.var_Teacher.set(""),
        self.var_radio1.set("")

    #----------------------generate data set or photosample--------------------
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_Name.get()== "" or self.var_Id.get() =="":
            messagebox.showerror("Error","All Fields are required",parent= self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "12345",database = "face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id+=1
                sql = "update student set photo_sample=%s where ID = %s"
                my_cursor.execute(sql,(self.var_radio1.get(),self.var_Id.get() == id +1))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #---------dataset from opencv--------------------
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                #---------image cropping function--------------
                def face_crop(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3 by default
                    #minimum neighbor = 5

                    for(x,y,w,h) in faces:
                        face_crop = img[y:y+h,x:x+w]
                        return face_crop 

                capture = cv2.VideoCapture(0) #0->webcam, 1->other cam
                img_id = 0
                while True:
                    ret,my_frame = capture.read()
                    if face_crop(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_crop(my_frame),(450,450))
                        face = cv2.cvtColor(face,COLOR_BGR2GRAY)
                        file_path  = "Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_DUPLEX,3,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("RESULT","Data set generated Successfully !!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)


if __name__ == "__main__":
  root = Tk()
  obj = Student(root) 
  root.mainloop() 