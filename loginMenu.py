# -*- coding: utf-8 -*-
"""
@author: Rafet Efe Gazanfer, 190303087
"""

from tkinter import *
from tkinter import ttk
from tkinter import Label

from dinleyici import DinleyiciMenu

class LoginMenu:

    def __init__(self, canvasW, veritabani):
        
        self.veritabani = veritabani
        
        #self.client = db_client
        self.canvasW = canvasW
        self.canvasW.title('Login Menu')
        
        self.anaFrame = Frame(self.canvasW)
        self.anaFrame.grid(row=0, column=0, columnspan=3, pady=50, padx=50)
        Label(self.anaFrame, text="Kullanici Adi/Email ").grid(row=1,column=0)
        Label(self.anaFrame, text="Sifre ").grid(row=2,column=0)
        
        self.name_entry = Entry(self.anaFrame)
        self.name_entry.grid(row=1,column=1)
        self.name_entry.focus()
        self.pass_entry = Entry(self.anaFrame)
        self.pass_entry.grid(row=2,column=1)
        
        self.giris_button = Button(self.anaFrame, text="Giriş", command=self.btnGiris, width=16)
        self.giris_button.grid(row=3,column=0,columnspan=5,pady=10)
        
        self.bildiri_label = Label(self.anaFrame, text="")
        self.bildiri_label.grid(row=4,columnspan=5,pady=10)
        
    def btnGiris(self):
        kAd = self.name_entry.get()
        kPass = self.pass_entry.get()
        
        #aranan kullanici var ise 
        sorgu = self.veritabani.c_kullanici.find_one({"username":kAd})
        #ve kullanicinin sifresi, input ile aynı ise
        if(sorgu and kPass == sorgu['password']):
            #dinleyiciEkranının şu anda tek olmasının sebebi, debug yapmamıza müsade ediyor.
            dinleyiciEkranı = DinleyiciMenu(self.canvasW, self.veritabani, self.name_entry.get())
            self.anaFrame.destroy()
        elif(not(kAd and kPass)):
            self.bildiri_label['text'] = "Kullanıcı Adı/Şifre boş olamaz."
        else:
            self.bildiri_label['text'] = "Kullanıcı Adı/Şifre yanlış."
        