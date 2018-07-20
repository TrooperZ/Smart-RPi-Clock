#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Smart Clock v.1.0
Created By: Amin Karic

This program uses Python 2.7 to 3.4 because of feedparser. For 3.4, change
Tkinter to tkinter.

Please align the .place() x and y coordinates to your liking.

Before you run this code:
- Know that currently there is no exit function, so you have to do Ctrl + f6 to exit

'''

try:
    import Tkinter as tk
except:
    import tkinter as tk
from time import sleep, strftime
import datetime
import feedparser #pip install feedparser  (sudo for Linux, Admin CMD for Windows)
import time
from itertools import cycle
import forecastio #pip install python-forcastio  (sudo for Linux, Admin CMD for Windows)
from PIL import Image, ImageTk #pip or pip3 install Pillow (sudo for Linux, Admin CMD for Windows)

class SmartClock(tk.Tk):
    
    def __init__(self, master=None):
        self.master = master
        tk.Tk.__init__(self)
        self. d = feedparser.parse('https://www.reddit.com/r/news/.rss')
        self.post_list = cycle(self.d.entries)
        self.icon_lookup = {
        'clear-day': "assets/Sun.png",  # clear sky day
        'wind': "assets/Wind.png",   #wind
        'cloudy': "assets/Cloud.png",  # cloudy day
        'partly-cloudy-day': "assets/PartlySunny.png",  # partly cloudy day
        'rain': "assets/Rain.png",  # rain day
        'snow': "assets/Snow.png",  # snow day
        'snow-thin': "assets/Snow.png",  # sleet day
        'fog': "assets/Haze.png",  # fog day
        'clear-night': "assets/Moon.png",  # clear sky night
        'partly-cloudy-night': "assets/PartlyMoon.png",  # scattered clouds night
        'thunderstorm': "assets/Storm.png",  # thunderstorm
        'tornado': "assests/Tornado.png",    # tornado
        'hail': "assests/Hail.png"  # hail
        }
        self.halfw_clock = self.winfo_screenwidth()/2-350
        self.halfh_clock = self.winfo_screenheight()/2-100
        self.time1 = ''
        self.date1 = ''
        self.iconLbl = tk.Label(self, bg="black")
        self.iconLbl.pack()
        self.iconLbl.place(x=0, y=0)
        self.clock = tk.Label(self, font=('calibri light', 140), bg='black', fg='white')
        self.clock.pack()
        self.clock.place(x=self.halfw_clock, y=self.halfh_clock)
        self.templbl = tk.Label(self, font=('calibri light', 40), fg='white', bg='black')
        self.templbl.pack()
        self.templbl.place(x=120, y=10)
        self.summlbl = tk.Label(self, font=('calibri light', 20), bg='black', fg='white', wraplength=200)
        self.summlbl.pack()
        self.summlbl.place(x=10, y=120)
        self.feel = tk.Label(self, font=('calibri light', 20), bg='black', fg='white', wraplength=200)
        self.feel.pack()
        self.feel.place(x=10, y=190)
        self.precipprob = tk.Label(self, wraplength=200, font=('calibri light', 20), fg='white', bg='black')
        self.precipprob.pack()
        self.precipprob.place(x=10, y=260)
        self.date = tk.Label(self, font=('calibri light', 35), bg='black', fg='white')
        self.date.pack()
        self.date.place(x=610, y=10)
        self.label_rss = tk.Label(self, font=('calibri', 18, 'bold'), wraplength=750, bg='black', fg='white')
        self.label_rss.pack(side=tk.BOTTOM)
        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        self.configure(background='black')
        self.focus_set()
        self.tick()
        self.date_tick()
        self.rssfeeds()
        self.weather()

    def rssfeeds(self):
        self.post = next(self.post_list)
        self.RSSFEED = self.post.title
        self.modTXT = 'News:  ' + self.RSSFEED
        self.label_rss.config(text=self.modTXT)
        self.after(8000, self.rssfeeds)


    def tick(self):
     global time1
     self.time2 = strftime("%H:%M:%S")
     if self.time2 != self.time1:
      self. time1 = self.time2
      self.clock.config(text=self.time2)
     self.clock.after(1000, self.tick)

    def date_tick(self):
     global date1
     self.date2 = strftime('''%A,
%B %d, %Y''')
     if self.date2 != self.date1:
      self.date1 = self.date2
      self.date.config(text=self.date2)
     self.date.after(1000, self.date_tick)
    
    def weather(self):
     self.api_key = "Your API key"
     self.lat = Your latitude
     self.lng = Your longitude
     self.degree_sign= u'\N{DEGREE SIGN}' 
     self.forecast = forecastio.load_forecast(self.api_key, self.lat, self.lng)
     self.r = self.forecast.currently()
     self.icon_id = self.r.icon
     self.icon2 = None
     self.icon = ''
     if self.icon_id in self.icon_lookup:
         self.icon2 = self.icon_lookup[self.icon_id]
         if self.icon2 is not None:
                if self.icon != self.icon2:
                    self.icon = self.icon2
                    self.image = Image.open(self.icon2)
                    self.image = self.image.resize((100, 100),  Image.ANTIALIAS)
                    self.image = self.image.convert('RGB')
                    self.photo = ImageTk.PhotoImage(self.image)
                    self.iconLbl.config(image=self.photo)
                    self.iconLbl.image = self.photo
         else:
                    self.iconLbl.config(image='')
     self.temp = str(int(round(self.r.temperature))) + "F" + self.degree_sign
     self.templbl.config(text=self.temp)
     self.sumr = self.r.summary
     self.summlbl.config(text=self.sumr)
     self.feeltemp = "Feels Like: " + str(int(round(self.r.apparentTemperature))) + "F" + self.degree_sign
     self.feel.config(text=self.feeltemp)
     self.precipprb = "Chances of rain: " + str(self.r.precipProbability) + "%"
     self.precipprob.config(text=self.precipprb)
     self.after(300000, self.weather) #every 5 minutes

app = SmartClock()
app.mainloop()
