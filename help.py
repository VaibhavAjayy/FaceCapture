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


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("FACE RECOGNITION BASED ATTENDANCE SYSTEM")

        title_lbl = Label(self.root,text="HELP DESK", font = ("Arial Black",26,"bold"),bg = "darkred",fg="white")
        title_lbl.place(x = 0, y = 0, width= 1290, height= 40)

        img_top = Image.open(r"Images\Service-Help-Desk.png")
        img_top  = img_top .resize((1280,600),Image.ANTIALIAS) #Antialias -> high to low level img
        self.photoimg_top  = ImageTk.PhotoImage(img_top)

        first_lbl = Label(self.root,image = self.photoimg_top)
        first_lbl.place(x = 0, y = 40,width=1280,height=640)

        email_lbl = Label(self.root,text="EMAIL:vaibhav_it20b11_40@dtu.ac.in", font = ("Arial Black",25,"bold"),bg = "red",fg="white")
        email_lbl.place(x = 300, y =330)


if __name__ == "__main__":
  root = Tk()
  obj = Help(root) 
  root.mainloop() 