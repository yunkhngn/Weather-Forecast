#please create a weather app that will take in a city name and display the current weather
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from itertools import count, cycle
from time import strftime 
from requests.api import get

def getWeather():
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=e9185b28e9969fb7a300801eb026de9c"
    response = requests.get(url)
    data = response.json()
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    temp = round(temp - 273.15, 2)
    weatherLabel.config(text=weather.title() + ' with a \ntemperature of ' + str(temp) + '°C')

def getLocation():
    global city
    url = "http://ipinfo.io/"
    response = requests.get(url)
    data = response.json()
    city = data["city"]
    displayCurrentCity.config(text="Your current city is " + city)

def time(): 
    string = strftime('%H:%M') 
    timeDisplay.config(text = string) 
    timeDisplay.after(1000, time) 

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

screen = tk.Tk()
screen.geometry("250x400")
screen.resizable(width=False, height=False)
screen.title(" Weather App")
screen.config(bg="#013368")
screen.iconbitmap("cloud.ico")

displayFrame = tk.Frame(screen, bg="#013368")
displayFrame.grid(columnspan="2", row="0", padx=(0,5), pady=(15,0))

displayCurrentCity = tk.Label(displayFrame, bg="#013368")
displayCurrentCity.grid(columnspan = "2", row = "3", padx=0, pady=(5,0))
displayCurrentCity.config(text = "", font=("Segoe UI",10), fg="white")
getLocation()

weatherDisplay = tk.Label(displayFrame, bg="#013368")
weatherDisplay.grid(columnspan = "2", row = "1", padx=0, pady=(10,0))
weatherDisplay.config(text = "Weather App", font=("Segoe UI Bold",15), fg="white")

timeDisplay = tk.Label(displayFrame, bg="#013368")
timeDisplay.grid(columnspan = "2", row = "2", padx=0, pady=(2,0))
timeDisplay.config(text = "00:00", font=("Segoe UI Bold",25), fg="white")

weatherLabel = tk.Label(displayFrame, bg="#013368")
weatherLabel.grid(columnspan = "2", row = "4", padx=0, pady=(0,4))
weatherLabel.config(text = "", font=("Playfair Display",14), fg="white")

getWeather()

lbl = ImageLabel(screen, width=230, height=200)
lbl.grid(columnspan = "2", row = "4", padx=(0,20), pady=(0,0))
lbl.load('gif.gif')

copyright = tk.Label(screen, bg="#013368")
copyright.grid(columnspan = "2", row = "4", padx=0, pady=(140,0))
copyright.config(text = "Copyright © Khoa Nguyễn", font=("Segoe UI",7), fg="white")

time()
screen.mainloop()

