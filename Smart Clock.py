#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Smart Clock v.2.0.1


This program uses Python 2.7 to 3.4 because of feedparser. For 3.4, change
Tkinter to tkinter.

Please customize the variables for postion, fonts, and size below
to your liking.




NEW:
Fixed forecastio glitch
Fixed Pillow issue for Linux/Raspberry Pi (see README.md)
Removed redundant code
Reformatted code

'''

#WARNING!!! Use Ctrl + F6 to leave

import Tkinter as tk
from time import strftime
import datetime
import feedparser #pip install feedparser  (sudo for Linux, Admin CMD for Windows)
from itertools import cycle
import forecastio #pip install python-forcastio  (sudo for Linux, Admin CMD for Windows)
from PIL import Image, ImageTk #pip or pip3 install Pillow (sudo for Linux, Admin CMD for Windows)


##########Positioning, fonts, sizing##########

#Weather API
Set_API = "Your API Key"
Set_lat = Your Latitude
Set_long = Your Longitude
units = "F" #use "C" if latitude and longitude is not in the US

#General 
screen_bg = 'black' #Background
screen_fg = 'white' #Text and icon only. Use white or black
icon_setup = None

#White Icons
icon_setup_A = {
        'clear-day': "Weather Icons/White/Sun.png",  # clear sky day
        'wind': "Weather Icons/White/Wind.png",   #wind
        'cloudy': "Weather Icons/White/Cloud.png",  # cloudy day
        'partly-cloudy-day': "Weather Icons/White/PartlySunny.png",  # partly cloudy day
        'rain': "Weather Icons/White/Rain.png",  # rain day
        'snow': "Weather Icons/White/Snow.png",  # snow day
        'snow-thin': "Weather Icons/White/Snow.png",  # sleet day
        'fog': "Weather Icons/White/Haze.png",  # fog day
        'clear-night': "Weather Icons/White/Moon.png",  # clear sky night
        'partly-cloudy-night': "Weather Icons/White/PartlyMoon.png",  # scattered clouds night
        'thunderstorm': "Weather Icons/White/Storm.png",  # thunderstorm
        'tornado': "Weather Icons/White/Tornado.png",    # tornado
        'hail': "Weather Icons/White/Hail.png"  # hail
        }
#Black Icons
icon_setup_B = {
        'clear-day': "Weather Icons/Black/Sun.png",  # clear sky day
        'wind': "Weather Icons/Black/Wind.png",   #wind
        'cloudy': "Weather Icons/Black/Cloud.png",  # cloudy day
        'partly-cloudy-day': "Weather Icons/Black/PartlySunny.png",  # partly cloudy day
        'rain': "Weather Icons/Black/Rain.png",  # rain day
        'snow': "Weather Icons/Black/Snow.png",  # snow day
        'snow-thin': "Weather Icons/Black/Snow.png",  # sleet day
        'fog': "Weather Icons/Black/Haze.png",  # fog day
        'clear-night': "Weather Icons/Black/Moon.png",  # clear sky night
        'partly-cloudy-night': "Weather Icons/Black/PartlyMoon.png",  # scattered clouds night
        'thunderstorm': "Weather Icons/Black/Storm.png",  # thunderstorm
        'tornado': "Weather Icons/Black/Tornado.png",    # tornado
        'hail': "Weather Icons/Black/Hail.png"  # hail
        }

#Icon setup
if screen_fg == 'white':
    icon_setup = icon_setup_A
elif screen_fg == 'black':
    icon_setup = icon_setup_B

News_Link = 'https://www.reddit.com/r/news/.rss' #The RSS feed for your news

#This is for a 1920x1080 resolution. Change it for your style

#Clock
clock_x = 480
clock_y = 400
clock_font = ('calibri light', 180)#font type, size, bold/italic/underlined (put comma between each bold/italic/underlined to make multi style)
                                   #Examples: ('Arial', 28, 'bold', 'italic'), ('Cambria', 36), ('Sans Serif', 12, 'bold')

#Weather Icon
icn_x = 0
icn_y = 0

#Temperature Label
t_x = 120
t_y = 10
t_font = ('Calibri light', 50)

#Weather Summary
weatherSummary_x = 10
weatherSummary_y = 120
weatherSummary_font = ('calibri light', 20)
weatherSummary_textLimit = 400 #amount of pixels the text can go before making a new line

#Temperature that feels like
feel_x = 10
feel_y = 190
feel_font = ('calibri light', 20)
feel_textLimit = 200

#Precipitation Probability
precprob_x = 10
precprob_y = 260
precprob_font = ('calibri light', 20)
precprob_textLimit = 200

#Date
date_x = 610
date_y = 10
date_font = ('calibri light', 35)

#News
#Note: there is no positioning for news. By default in the .pack(), it is at the bottom. DO NOT CHANGE
news_font = ('calibri', 28, 'bold')
news_textLimit = 750

##########Positioning, fonts, sizing##########


class SmartClock(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.iconLbl = tk.Label(self, bg=screen_bg)
        self.iconLbl.pack()
        self.iconLbl.place(x=icn_x, y=icn_y)
        self.clock = tk.Label(self, font=clock_font, bg=screen_bg, fg=screen_fg)
        self.clock.pack()
        self.clock.place(x=clock_x, y=clock_y)
        self.templbl = tk.Label(self, font=t_font, fg=screen_fg, bg=screen_bg)
        self.templbl.pack()
        self.templbl.place(x=t_x, y=t_y)
        self.summlbl = tk.Label(self, font=weatherSummary_font, bg=screen_bg, fg=screen_fg, wraplength=weatherSummary_textLimit)
        self.summlbl.pack()
        self.summlbl.place(x=weatherSummary_x, y=weatherSummary_y)
        self.feel = tk.Label(self, font=feel_font, bg=screen_bg, fg=screen_fg, wraplength=feel_textLimit)
        self.feel.pack()
        self.feel.place(x=feel_x, y=feel_y)
        self.precipprob = tk.Label(self, wraplength=precprob_textLimit, font=precprob_font, fg=screen_fg, bg=screen_bg)
        self.precipprob.pack()
        self.precipprob.place(x=precprob_x, y=precprob_y)
        self.date = tk.Label(self, font=date_font, bg=screen_bg, fg=screen_fg)
        self.date.pack()
        self.date.place(x=date_x, y=date_y)
        self.label_rss = tk.Label(self, font=news_font, wraplength=news_textLimit, bg=screen_bg, fg=screen_fg)
        self.label_rss.pack(side=tk.BOTTOM)
        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        self.configure(background=screen_bg)
        self.focus_set()
        self.tick()
        self.GetRSS()
        self.date_tick()
        self.rssfeeds()
        self.weather()
        
    def GetRSS(self):
        global post_list
        news = feedparser.parse(News_Link)
        post_list = cycle(news.entries)
        self.after(300000, self.GetRSS) #every 5 minutes


    def rssfeeds(self):
        post = next(post_list)
        RSSFEED = post.title
        modTXT = 'News:  ' + RSSFEED
        self.label_rss.config(text=modTXT)
        self.after(10000, self.rssfeeds)


    def tick(self):
     time2 = strftime("%H:%M:%S")
     self.clock.config(text=time2)
     self.clock.after(1000, self.tick)

    def date_tick(self):
     date2 = strftime('''%A,
%B %d, %Y''')
     self.date.config(text=date2)
     self.date.after(1000, self.date_tick)
    
    def weather(self):
     degree_sign= u'\N{DEGREE SIGN}' 
     forecast = forecastio.load_forecast(Set_API, Set_lat, Set_long)
     current_f = forecast.currently()
     icon_id = current_f.icon
     icon2 = None
     icon = ''
     if icon_id in icon_setup:
         icon2 = icon_setup[icon_id]
         if icon2 is not None:
                if icon != icon2:
                    icon = icon2
                    image = Image.open(icon2)
                    image = image.resize((100, 100),  Image.ANTIALIAS)
                    image = image.convert('RGBA')
                    photo = ImageTk.PhotoImage(image)
                    self.iconLbl.config(image=photo)
                    self.iconLbl.image = photo
         else:
                    self.iconLbl.config(image='')
     temp = str(int(round(current_f.temperature))) + units + degree_sign
     self.templbl.config(text=temp)
     sumr = current_f.summary
     self.summlbl.config(text=sumr)
     feeltemp = "Feels Like: " + str(int(round(current_f.apparentTemperature))) + units + degree_sign
     self.feel.config(text=feeltemp)
     precipprb = "Chances of rain: " + str(current_f.precipProbability) + "%"
     self.precipprob.config(text=precipprb)
     self.after(300000, self.weather) #every 5 minutes

app = SmartClock()
app.mainloop()
