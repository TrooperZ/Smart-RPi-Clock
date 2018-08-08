# Smart-RPi-Clock
A smart clock for the Raspberry Pi and can be run on Windows. Shows weather, date, time, and news. Runs from Python 2.7 to 3.4.

## UPDATE
### v2.1
You have to install the ImageTk package seperatly if you are running it on a Raspberry Pi or Linux

For Raspberry Pi and Linux:

    sudo apt-get install python-imaging python-imaging-tk
   
Python 3:

    sudo apt-get install python3-pil python3-pil.imagetk
    
Windows: It comes with Pillow, so you don't need to worry.

What's New:

- Reformatted Code
- Fixed forecastio glitch
- Fixed ImageTk glitch
- Removed Redundant code

### v2!

Woohoo!

What's new:

- Easy customize variables (fonts, text, background, etc.)
- Removed background from icons
- Added black icons
- Added RSS feed updating

## Hardware
I recommend using a fairly good screen, HDMI, 10 inches or more, WiFi, and a good power cable for your RPi.

## Before you start
Know that to leave is Ctrl+F6.

## Weather

You need to get your own API key <a href="www.darksky.net/dev">here</a> and get your longitude and latitude on Google Maps. Also, pip install the forcastio DarkSky wrapper using sudo(linux/RPi) or admin console(windows):

    pip install python-forecastio
    
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
    
Further changes will be made to this project and hopefully I will make it better.
