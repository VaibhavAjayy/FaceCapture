from cProfile import label
from distutils.debug import DEBUG
from logging import exception
from operator import ge
from optparse import Values
import string
from tkinter import*
from tkinter import ttk
from tkinter import font
import tkinter
from turtle import width  #for stylish toolkit
from PIL import Image,ImageTk
from cv2 import COLOR_BGR2GRAY, COLOR_GRAY2BGR
from flask import g
from matplotlib.pyplot import connect, fill, get
from tkinter import messagebox
import mysql.connector
from numpy import delete, var 
import cv2
from pyparsing import restOfLine
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("FACE RECOGNITION BASED ATTENDANCE SYSTEM")

        #------------------variables--------------------------
        self.var_attend_id = StringVar()
        self.var_attend_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time= StringVar()
        self.var_date = StringVar()
        self.var_attend_status = StringVar()
 
        # 1st image
        img = Image.open(r"Images\whyfacebanner.png")
        img = img.resize((650,150),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg = ImageTk.PhotoImage(img)

        first_lbl = Label(self.root,image = self.photoimg)
        first_lbl.place(x = 0, y = 0, width=650,height=150)

       
        # 2nd image
        img1 = Image.open(r"Images\1519797201497.jpg")
        img1 = img1.resize((640,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root,image = self.photoimg1)
        first_lbl.place(x = 650, y = 0, width=640,height=150)

        title_lbl = Label(self.root,text="ATTENDANCE MANGAMENT SYSTEM", font = ("Arial Black",25,"bold"),bg = "green",fg="white")
        title_lbl.place(x = 0, y = 150, width= 1290, height= 35)

        main_frame = Frame(self.root,bd=2,bg="white")
        main_frame.place(x=5,y=187,width=1280,height=500)
        
        #left frame
        left_frame = LabelFrame(main_frame,bd=5,bg="lightblue",relief=RIDGE,text="STUDENT ATTENDANCE DETAILS",font =("Arial",12,"bold"))
        left_frame.place(x = 20,y=10,width=590,height=450)

        img_left = Image.open(r"Images\depositphotos_26419797-stock-photo-children-reading-books.jpg")
        img_left  = img_left .resize((570,100),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg_left  = ImageTk.PhotoImage(img_left)

        first_lbl = Label(left_frame,image = self.photoimg_left)
        first_lbl.place(x = 5, y = 0, width=570,height=100)

        #left_inside_frame
        left_inside_frame = LabelFrame(left_frame,bd=5,bg="lightyellow",relief=RIDGE,font =("Arial",12,"bold"))
        left_inside_frame.place(x = 5,y=110,width=570,height=300)


        # label and entry
        #Attendance_ID
        Attendance_ID_label = Label(left_inside_frame,text="ATTENDACE_ID:",font =("Arial",10,"bold"),bg ="lightyellow")
        Attendance_ID_label.grid(row=0,column=0,padx= 5,sticky=W)

        Attendance_ID_Entry = ttk. Entry(left_inside_frame,width=15,textvariable=self.var_attend_id,font =("Arial",10,"bold"))
        Attendance_ID_Entry.grid(row=0,column=1,padx= 5,pady = 5,sticky=W)

        #Name
        Name_label = Label(left_inside_frame,text="NAME:",font =("Arial",10,"bold"),bg ="lightyellow")
        Name_label.grid(row=0,column=2,padx= 5,sticky=W)

        Name_Entry = ttk. Entry(left_inside_frame,width=15,textvariable=self.var_name,font =("Arial",10,"bold"))
        Name_Entry.grid(row=0,column=3,padx= 5,pady = 5,sticky=W)

        #RollNo
        RollNo_label = Label(left_inside_frame,text="ROLL NO:",font =("Arial",10,"bold"),bg ="lightyellow")
        RollNo_label.grid(row=1,column=0,padx= 5,sticky=W)

        RollNo_Entry = ttk. Entry(left_inside_frame,width=15,textvariable=self.var_attend_roll,font =("Arial",10,"bold"))
        RollNo_Entry.grid(row=1,column=1,padx= 5,pady = 5,sticky=W)

        #Department
        Department_label = Label(left_inside_frame,text="DEPARTMENT:",font =("Arial",10,"bold"),bg ="lightyellow")
        Department_label.grid(row=1,column=2,padx= 5,sticky=W)

        Department_Entry = ttk. Entry(left_inside_frame,width=15,textvariable=self.var_dep,font =("Arial",10,"bold"))
        Department_Entry.grid(row=1,column=3,padx= 5,pady = 5,sticky =W)

        #Time
        Time_label = Label(left_inside_frame,text="TIME:",font =("Arial",10,"bold"),bg ="lightyellow")
        Time_label.grid(row=2,column=0,padx= 5,sticky=W)

        Time_Entry = ttk. Entry(left_inside_frame,width=15,textvariable=self.var_time,font =("Arial",10,"bold"))
        Time_Entry.grid(row=2,column=1,padx= 5,pady = 5,sticky=W)

        #Date
        Date_label = Label(left_inside_frame,text="DATE:",font =("Arial",10,"bold"),bg ="lightyellow")
        Date_label.grid(row=2,column=2,padx= 5,sticky=W)

        Date_Entry = ttk. Entry(left_inside_frame,width=15,textvariable=self.var_date,font =("Arial",10,"bold"))
        Date_Entry.grid(row=2,column=3,padx= 5,pady = 5,sticky =W)

        #Attendance_Status
        Attendance_Status_label = Label(left_inside_frame,text="ATTENDACE_STATUS:",font =("Arial",10,"bold"),bg ="lightyellow")
        Attendance_Status_label.grid(row=3,column=0,padx= 5,sticky=W)

        Attendance_Status_combo = ttk.Combobox(left_inside_frame,textvariable=self.var_attend_status,font =("Arial",8,"bold"),state = "read only",width=15)
        Attendance_Status_combo["values"]=("Select Status","Present","Absent")
        Attendance_Status_combo.current(0)
        Attendance_Status_combo.grid(row=3,column=1,padx= 2, pady= 5,sticky=W)

        #button frame
        button_frame = Frame(left_inside_frame,bd=2,relief=RIDGE)
        button_frame.place(x = 0,y=200,width=560,height=29)

        save_button = Button(button_frame,text="IMPORT CSV",command=self.importCsv,width =19,font=("Arial",8,"bold"),bg ="blue",fg= "white")
        save_button.grid(row=0,column=1)

        update_button = Button(button_frame,text="EXPORT CSV",command=self.exportCsv,width =19,font=("Arial",8,"bold"),bg ="blue",fg= "white")
        update_button.grid(row=0,column=2)
        
        delete_button = Button(button_frame,text="UPDATE",command=self.update_data,width =19,font=("Arial",8,"bold"),bg ="blue",fg= "white")
        delete_button.grid(row=0,column=3)

        reset_button = Button(button_frame,text="RESET",width =19,command=self.reset_data,font=("Arial",8,"bold"),bg ="blue",fg= "white")
        reset_button.grid(row=0,column=4)

        # Right label frame
        Right_frame = LabelFrame(main_frame,bd=5,bg="lightyellow",relief=RIDGE,text="ATTENDANCE  DETAILS",font =("Arial",12,"bold"))
        Right_frame.place(x = 650,y=10,width=595,height=450)

        Right_inside_frame = LabelFrame(Right_frame,bd=5,bg="lightyellow",relief=RIDGE,font =("Arial",12,"bold"))
        Right_inside_frame.place(x =5,y=5,width=570,height=410)

        #----------scroll bar---------------
        scroll_x = ttk.Scrollbar(Right_inside_frame ,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Right_inside_frame ,orient=VERTICAL)

        self.Attendance_Report_Table=ttk.Treeview(Right_inside_frame ,column=("Id","RollNo","Name","Department","Time","Date","Attendance_Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Attendance_Report_Table.xview)
        scroll_y.config(command=self.Attendance_Report_Table.yview)

        self.Attendance_Report_Table.heading("Id",text="ATTENDANCE ID")
        self.Attendance_Report_Table.heading("RollNo",text="ROLLNO")
        self.Attendance_Report_Table.heading("Name",text="NAME")
        self.Attendance_Report_Table.heading("Department",text="DEPARTMENT")
        self.Attendance_Report_Table.heading("Time",text="TIME")
        self.Attendance_Report_Table.heading("Date",text="DATE")
        self.Attendance_Report_Table.heading("Attendance_Status",text="ATTENDANCE_STATUS")
        self.Attendance_Report_Table["show"]="headings"

        self.Attendance_Report_Table.column("Id",width=100)
        self.Attendance_Report_Table.column("RollNo",width=100)
        self.Attendance_Report_Table.column("Name",width=100)
        self.Attendance_Report_Table.column("Department",width=100)
        self.Attendance_Report_Table.column("Time",width=100)
        self.Attendance_Report_Table.column("Date",width=100)
        self.Attendance_Report_Table.column("Attendance_Status",width=150)

        self.Attendance_Report_Table.pack(fill=BOTH,expand=1)
        self.Attendance_Report_Table.bind("<ButtonRelease>",self.get_cursor)
        

    #---------fetch data---------------------
    def fetchData(self,rows):
        self.Attendance_Report_Table.delete(*self.Attendance_Report_Table.get_children())
        for i in rows:
            self.Attendance_Report_Table.insert("",END,values=i)
    

    # importCSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir = os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent =self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
                 
    #exportCSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("N0 DATA","NO DATA FOUND TO EXPORT",parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent =self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter = ",")
                for i in mydata:
                    exp_write.writerow(i)
                    messagebox.showinfo("DATA EXPORT","YOUR DATA EXPORTED SUCCESSFULLY")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)} ",parent = self.root)
    
    #---------------------get cursor function------------------------------------
    def get_cursor(self,event = ""):
        cursor_row = self.Attendance_Report_Table.focus()
        content = self.Attendance_Report_Table.item(cursor_row)
        data = content["values"] 

        self.var_attend_id.set(data[0])
        self.var_attend_roll.set(data[1]) 
        self.var_name.set(data[2])
        self.var_dep.set(data[3])
        self.var_time.set(data[4])
        self.var_date.set(data[5]) 
        self.var_attend_status.set(data[6])

    #------------------reset function--------------------------------
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("") 
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("") 
        self.var_attend_status.set("Select Status")

    def update_data(self):
        self.update_data = tkinter.messagebox.showinfo("UPDATE","Check Csv file for Updation",parent =self.root)
        if self.update_data >0:
            self.root.destroy()
        else:
            return

         

if __name__ == "__main__":
  root = Tk()
  obj = Attendance(root) 
  root.mainloop() 