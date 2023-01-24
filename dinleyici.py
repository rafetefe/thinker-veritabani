# -*- coding: utf-8 -*-
"""
@author: Rafet Efe Gazanfer, 190303087
"""

from tkinter import *
from tkinter import ttk
from tkinter import Label

class DinleyiciMenu:

    def __init__(self, window, veritabani, kullanici_adi):
        
# =============================================================================
#         Dinleyici:
#         	Müzik arama
#         	Playlist oluşturma
#         	Podcast + Podcast değerlendirme
# =============================================================================
        
        self.veritabani = veritabani

        #self.client = db_client
        self.window = window
        self.window.title('Merhaba {}'.format(kullanici_adi))
        
        aramaFrame = Frame(self.window)
        aramaFrame.grid(row=0, column=0, columnspan=5, padx=50, pady=50)
        
        self.arama_entry = Entry(aramaFrame)
        self.arama_entry.grid(row=0,column=0,padx=25, pady=25)
        self.arama_button = Button(aramaFrame, width=5, text="Ara", command=self.btnAra)
        self.arama_button.grid(row=0,column=1,padx=25)
        
        # Table
        self.tablo = ttk.Treeview(aramaFrame, height=10)
        self.tablo.grid(row=1, column=0, padx=25, columnspan=6)
        self.tablo.heading('#0', text='Arama Sonuçları', anchor=CENTER)
        
        menuFrame = Frame(self.window)
        menuFrame.grid(row=1, column=0, columnspan=5, pady=50, padx=50)
        
        self.playlist_button = Button(menuFrame, height=2, width=10, text="Playlist")
        self.playlist_button.grid(row=0, column=0, padx=10)
        
        self.podcast_button = Button(menuFrame, height=2, width=10, text="Podcast")
        self.podcast_button.grid(row=0,column=1)
        
        self.rapor_button = Button(menuFrame, height=2, width=10, text="Rapor", command=self.btnRapor)
        self.rapor_button.grid(row=0,column=2, padx=10)
        
    def btnAra(self):
        if(self.arama_entry.get() == ""):
            pass #Bir girdi girilmediğine göre arama yapılmasına gerek yok.
        else:
            #tabloyu temizle
            satirlar = self.tablo.get_children()
            for satir in satirlar:
                self.tablo.delete(satir)
            #tabloyu yeni değerle doldur
            arama_sonuclari = self.veritabani.c_sarki.find({'adi': { "$regex": self.arama_entry.get()}})
            # filling data
            for sonuc in arama_sonuclari:
                self.tablo.insert('', 0, text=sonuc['adi'])
                
    def btnRapor(self):
        
        satirlar = self.tablo.get_children()
        if(satirlar):
            f = open("sonuclar.txt", 'w')
            f.write("Arama sonuclari\n")
            for satir in satirlar:
                f.write(self.tablo.item(satir)['text'] + "\n")
                #print(self.tablo.item(satir)['text'])
            f.close()
            
            f = open("sonuclar.txt","r") #f = open("sonuclar.txt", 'wr') must have exactly one of create/read/write/append mode
            popUp = Toplevel()
            popUp.title("İşlem Tamamlandı")
            Label(popUp, text="Raporlama islemi tamamlandi.\n",).grid(row=0,column=0,padx=5,pady=5)
            Label(popUp, text=f.read()).grid(row=1,column=0)
            btnExit = Button(popUp, text="Tamam", command=popUp.destroy)
            btnExit.grid(row=2,columnspan=2,padx=5)
            f.close()
            