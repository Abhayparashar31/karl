import pyttsx3
from bs4 import BeautifulSoup 
import requests
from googlesearch import search
import webbrowser
import speech_recognition as sr
from tkinter import *
from tkinter.messagebox import showinfo, showerror
import csv
import time
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# name = 'how to remove background from an image in figma'
data = ""
# for i in search(name, num=1, stop=3, pause=2): 
#     link = i
#     print(i)
#     #webbrowser.open(f"{link}")
#     res = requests.get(link,headers=headers)
#     soup = BeautifulSoup(res.text,"html.parser")
#     content = soup.findAll("p")
#     #print(link)
#     for texts in content :
#         data +=texts.text
# print(data)
    

res = requests.get('https://stackoverflow.com/questions/15802554/how-to-make-a-timer-program-in-python',headers=headers)
soup = BeautifulSoup(res.text,"html.parser")
print(soup)
content = soup.select('.prettyprinted')     
print(content)
for texts in content :
    data +=texts.text
print(data)