from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from matplotlib.pyplot import gray
import mysql.connector
import os
import numpy as np
from PIL import Image,ImageTk
import cv2
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("FACE RECOGNITION BASED ATTENDANCE SYSTEM")
 
        title_lbl = Label(self.root,text="FACE RECOGNITION", font = ("Arial Black",26,"bold"),bg = "darkred",fg="white")
        title_lbl.place(x = 0, y = 0, width= 1290, height= 40)

        img_top = Image.open(r"Images\facialscanningaish1151270_1523604-860x645.jpg")
        img_top  = img_top .resize((670,600),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg_top  = ImageTk.PhotoImage(img_top)

        first_lbl = Label(self.root,image = self.photoimg_top)
        first_lbl.place(x = 0, y = 40,width=670,height=630)

        img_bottom = Image.open(r"Images\whyfacebanner.png")
        img_bottom  = img_bottom .resize((650,600),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg_bottom  = ImageTk.PhotoImage(img_bottom)

        first_1_lbl = Label(self.root,image = self.photoimg_bottom)
        first_1_lbl.place(x = 670, y = 40,width=650,height=630)

        #button
        b1_button = Button(self.root,text="FACE RECOGNIZER",command=self.recognition,width =19,font=("Arial",23,"bold"),bg ="yellow",fg= "black")
        b1_button.place(x = 500, y = 550,width=300,height=45)
    

    #------------Attendance-------------------------------------------
    def mark_attendance(self,i,r,n,d):
        with open("Attendance_today.csv","r+",newline="\n") as f:
            my_data_list = f.readlines()
            name_list = []
            for line in my_data_list:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list)and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dt=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dt},{d1},Present")

            

    #------------------face recognition-------------------------------
    def recognition(self):
        def draw_Boundary(img,classifier,scaleFactor,minNeighbor,color,text,classifier_1):
             gray_image =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
             features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbor)

             coord=[]

             for(x,y,w,h) in features:
                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
                 id,predict = classifier_1.predict(gray_image[y:y+h,x:x+w])
                 confidence = int((100*(1-predict/300)))

                 conn = mysql.connector.connect(host = "localhost",username = "root",password = "12345",database = "face_recognition")
                 my_cursor = conn.cursor()

                 my_cursor.execute("select Name from student where ID ="+str(id))
                 n = my_cursor.fetchone() 
                 n = "+".join(n)

                 my_cursor.execute("select rollno from student where ID ="+str(id))
                 r = my_cursor.fetchone()
                 r = "+".join(r)

                 my_cursor.execute("select Department from student where ID ="+str(id))
                 d = my_cursor.fetchone()
                 d = "+".join(d)

                 my_cursor.execute("select ID from student where ID ="+str(id))
                 i = my_cursor.fetchone() 
                 i = "+".join(i)


                 if confidence>77:
                     cv2.putText(img,f"ID: {i}",(x,y-100),cv2.FONT_HERSHEY_COMPLEX,1,(0,204,204),3)
                     cv2.putText(img,f"ROLL NO: {r}",(x,y-70),cv2.FONT_HERSHEY_COMPLEX,1,(0,204,204),3)
                     cv2.putText(img,f"NAME: {n}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,1,(0,204,204),3)
                     cv2.putText(img,f"DEPARTMENT: {d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,204,204),3)
                     self.mark_attendance(i,r,n,d)
                 else:
                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                     cv2.putText(img,"UNKNOWN FACE",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)

                 coord=[x,y,w,h]

             return coord 
        def recognize(img,classifier_1,faceCascade):
            coord =draw_Boundary(img,faceCascade,1.1,10,(255,255,255),"Face",classifier_1)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        classifer_1 = cv2.face.LBPHFaceRecognizer_create()
        classifer_1.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img=recognize(img,classifer_1,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1) == 13:
             break
            
        video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
  root = Tk()
  obj = Face_Recognition(root) 
  root.mainloop()         