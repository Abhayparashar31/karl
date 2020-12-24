import os
from pynput.keyboard import Key,Listener
import pyttsx3
import os
import webbrowser
keys=[]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Activating Karl..... Sir!")
def on_press(key):
    global keys
    #keys.append(str(key).replace("'",""))
    string = str(key).replace("'","")
    keys.append(string)
    main_string = "".join(keys)
    print(main_string)
    if "[0--0]" in main_string:
        speak("Running karl...")
        os.startfile("C:\\Users\\abhay\\Desktop\\ChatBot\\karl.bat")
        keys = []
    elif "[0000]" in main_string:
        os.startfile("C:\\Users\\abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        webbrowser.open("https://www.youtube.com/")
        keys = []
    elif "[0photoshop0]" in main_string:
        speak("Opening photoshop...")
        os.startfile("F:\\softwares\\photoshop\\PhotoshopPortable.exe")
        keys = []
def on_release(key):
    if key == Key.esc:
        speak("Shutting Down karl sir...!")
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()