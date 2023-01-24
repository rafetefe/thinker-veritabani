# -*- coding: utf-8 -*-
"""
@author: Rafet Efe Gazanfer, 190303087
"""

#Offical mongodb python client
from pymongo import MongoClient

#https://docs.python.org/3/library/tkinter.html#tkinter-modules
from tkinter import Tk
from tkinter import Label
from tkinter import Frame
from tkinter import mainloop
from PIL import Image, ImageTk


#Kendi class/kütüphanelerimiz
from loginMenu import LoginMenu
from veritabani_setup import Veritabani


if __name__ == '__main__':
    
    def app():
        
        splash.destroy()
        
        veritabani = Veritabani()
        #Tkinter instantesi/oturumu
        
        canvasWindow = Tk()
            
        loginEkrani = LoginMenu(canvasWindow, veritabani)

    
    splash = Tk()
    splash.title("Splash Screen")
    
    Label(splash, text="Rafet Efe Gazanfer",font=12).grid(row=0,pady=5,padx=5)
    Label(splash, text="190303087", font=10).grid(row=1,pady=5)
    Label(splash, text="BIL303-2023 NoSQL Veri Tabanı Projesi", font=14).grid(row=2,pady=5,padx=5)
    imgErz = Image.open("erz.png")
    imgErz = imgErz.resize((250,250))
    imgTk = ImageTk.PhotoImage(imgErz)
    Label(splash, image=imgTk).grid(row=3,pady=5,padx=5)
    
    splash.after(3000, app)
    
    mainloop()
    
