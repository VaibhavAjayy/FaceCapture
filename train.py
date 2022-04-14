from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
from PIL import Image,ImageTk
import cv2

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("FACE RECOGNITION BASED ATTENDANCE SYSTEM")

        title_lbl = Label(self.root,text="TRAIN DATA SET", font = ("Arial Black",25,"bold"),bg = "darkgreen",fg="white")
        title_lbl.place(x = 0, y = 0, width= 1290, height= 35)

        img_top = Image.open(r"Images\PEOPLE.jpg")
        img_top  = img_top .resize((1279,280),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg_top  = ImageTk.PhotoImage(img_top)

        first_lbl = Label(self.root,image = self.photoimg_top)
        first_lbl.place(x = 0, y = 36,width=1279,height=280)
        
        #button
        b1_button = Button(self.root,text="TRAIN DATA",command=self.train_classifier,width =19,font=("Arial",24,"bold"),bg ="darkred",fg= "white")
        b1_button.place(x = 0, y = 290,width=1279,height=56)

        img_bottom = Image.open(r"Images\Personal-Crowd-Silhouettes-Human-Group-Of-People-2045498.jpg")
        img_bottom  = img_bottom .resize((1279,305),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        first_lbl = Label(self.root,image = self.photoimg_bottom)
        first_lbl.place(x = 0, y = 350,width=1279,height=305)
    
    
    def train_classifier(self):
        data_dir = ("Data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)] #list comprehension

        faces=[]
        ids = []

        for image in path:
            img = Image.open(image).convert('L')   #to convert bgr to gray
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("TRAINING",imageNp)
            cv2.waitKey(1) == 13 
        ids = np.array(ids)  

        #----------train classifier and save--------------
        classifier_1 = cv2.face.LBPHFaceRecognizer_create()
        classifier_1.train(faces,ids)
        classifier_1.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed !!")

        


if __name__ == "__main__":
  root = Tk()
  obj = Train(root) 
  root.mainloop()         