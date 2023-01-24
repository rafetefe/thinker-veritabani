# -*- coding: utf-8 -*-
"""
@author: Rafet Efe Gazanfer, 190303087
"""

from pymongo import MongoClient

class Veritabani:
    
    def __init__(self):
        
        self.ISIM = 'muzik_demeti_db'
        self.URL  = 'mongodb://localhost'
        
        #MongoDB offical client adaptörü
        self.client = MongoClient(self.URL)
        
        #Veritabanına erişim
        db = self.client[self.ISIM] 
        
        #Collectionlara indeksler
        self.c_kullanici = db['kullanici'] 
        self.c_dinleyici = db['dinleyici']
        self.c_podcaster = db['podcaster']
        self.c_artist    = db['artist']
        
        self.c_playlist  = db['playlist']
        self.c_podcast   = db['podcast']
        self.c_album     = db['album']
        self.c_sarki     = db['sarki']
        self.c_single    = db['single']
        self.c_EP        = db['EP']
        self.c_LP        = db['LP']

        
    def db_temizle(self):
        self.client.drop_database(self.ISIM)
        
    
    def db_ornekVeri(self):
        #Kullanıcılar
        self.c_kullanici.insert_one({"_id":1, "email":"dinleyici@dg.com", "username":"dinleyici","password":"123"})
        self.c_kullanici.insert_one({"_id":2, "email":"podcaster@pg.com", "username":"podcaster","password":"123"})
        self.c_kullanici.insert_one({"_id":3, "email":   "artist@ag.com", "username":"artist"   ,"password":"123"})
        
        #https://www.mongodb.com/docs/manual/tutorial/model-embedded-one-to-one-relationships-between-documents/
        self.c_dinleyici.insert_one({
            "kullanici":1,
            "takip_ettikleri":[
                {"kullanici_id":3}, 
                {"kullanici_id":2}
                ]
            })
        
        #https://www.mongodb.com/docs/manual/tutorial/model-embedded-one-to-many-relationships-between-documents/
        self.c_podcaster.insert_one({
            "kullanici_id":2, 
            "podcastler":[{"podcast_id":1}],
            "adi":"Huberman Lab", 
            "hakkinda":"Hosted by Dr. Andrew Huberman, The Huberman Lab Podcast discusses science and science-based tools for everyday life. New episodes are released every Monday."
            })
        
        self.c_artist.insert_one({
            "kullanici_id":3,
            "adi":"The Weeknd",
            "singlelar":[{"single_id":1}],
            "albumler":[{"album_id":1}],
            "takipci":0, 
            "hakkinda":"The Weeknd took over pop music & culture on his own terms filtering R&B, Pop,& hip-hop through an ambitious widescreen lens. The multi-platinum 3X GRAMMY Award winner has emerged as one of the most successful & significant artists of the modern era."
            })
        
        #İçerikler
        self.c_podcast.insert_one({
            "_id":1,
            "adi":"Science based tools for increasinging happines | #1", 
            "hakkinda":"I explain the science of happiness, including the different types of happiness and how our actions, circumstances and mindset control them.",
            "tarih":"2022-11-07T00:00Z",
            "degerlendirme":5
            })
        
        #Weeknd Album
        self.c_album.insert_one({
            "_id":1,
            "adi":"After Hours",
            "album":[{
                "sarki_id":1},{
                "sarki_id":2}],
            "tarih":"2020-05-20T00:00Z"
            })
        
        #Weeknd Şarkılar
        self.c_sarki.insert_one({
            "_id":1,
            "adi":"Alone Again",
            "dinlenme":133562348})
        
        self.c_sarki.insert_one({
            "_id":2,
            "adi":"Too Late",
            "dinlenme":136872273})
        
        self.c_sarki.insert_one({
            "_id":3,
            "adi":"Stary Eyes - MIKE DEAN Remix",
            "dinlenme":4760989})
        
        #Weeknd Single
        self.c_single.insert_one({
            "_id":1,
            "adi":"Starry Eyes (MIKE DEAN Remix)",
            "sarki_id":3,
            "tarih":"2020-04-20T00:00Z"})
        
        #Weeknd EP
        self.c_EP.insert_one({
            "_id":1,
            "adi":"After Hours (Remixes)",
            "sarkilar":[{
                "sarki_id":4},{
                "sarki_id":5}],
            "tarih":"2020-03-02T00:00Z"})
        
        self.c_sarki.insert_one({
            "_id":4,
            "adi":"Heartless - Remix",
            "dinlenme":608722094
            })
        
        self.c_sarki.insert_one({
            "_id":5,
            "adi":"Blinding Lights - Chromatic Remix",
            "dinlenme":10633123})
        
        
                    
        
        