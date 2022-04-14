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
    root = Tk()
    obj = face_recognition(root)
    root.mainloop() 
