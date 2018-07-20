# Smart-RPi-Clock
A smart clock for the Raspberry Pi and can be run on Windows. Shows weather, date, time, and news. Runs from Python 2.7 to 3.4.

## Hardware
I recommend using a fairly good screen, HDMI, 10 inches or more, WiFi, and a good power cable for your RPi.

## Weather

You need to get your own API key <a href="www.darksky.net/dev">here</a> and get your longitude and latitude on Google Maps. Also, pip install the forcastio DarkSky wrapper using sudo(linux/RPi) or admin console(windows):

    pip install python-forcastio
    
Use the "Types of weather data.py" to see all the avalible data points. The 12 icons are also included with a license. To display them, you need Pillow (PIL).

    pip install Pillow
    
Or for Python 3:

    pip3 install Pillow

I am planning on adding the forecast for the next day.

## Clock and Date

A very nice display that stands out. Shows the time in 24-hour with seconds. Date is day of week, month, day, year. Uses tkinter and strftime.

## News
Uses feedparser to display it. I get my news from reddit, but you can change the link. All you have to do is find another RSS link and change it. To install feedparser:

    pip install feedparser
    
