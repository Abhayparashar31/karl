import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import datetime
import wikipedia #pip install wikipedia
from googlesearch import search #pip install google
import webbrowser
import os
import random
import smtplib
from email.message import EmailMessage #pip install email
from time import sleep
import time
from win10toast import ToastNotifier #pip install win10toast
from bs4 import BeautifulSoup #pip install bs4
import requests #pip install requests
from playsound import playsound  #pip install playsound
from subprocess import call,Popen
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 
     
    print("I am Karl Sir. your personal assistant. Please tell me how may I help you")
    speak("I am Karl Sir. your personal assistant. Please tell me how may I help you")       



def takeCommand():
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        t_end = time.time() + 5
        while time.time() < t_end:
            print("karl: Listening...")
            audio=r.listen(source)
            audio = audio
    try:    
        query = r.recognize_google(audio)
        print(f"user:{query}")
    except:
        print("karl: Please Type..")
        query=input() 
        return query
    return query 
    ''' 
    query=input("Type...")
    return query



def history():
    print("karl: Looking for history...")
    res = requests.get('https://www.onthisday.com/today/indian-history.php')
    soup = BeautifulSoup(res.text,'html.parser')
    history = soup.select('.event')
    for i in range(0,len(history)):
        history = soup.select('.event')[i].getText()
        history = str(history)
        print("In "+history)
        speak("In"+history)
def jobs():
    name = input("Job name:\n").replace(" ","-")
    city = input("City name:\n")
    state = input("State name:\n")
    speak(f"Searching jobs for {name} in {city}{state} be patient..")
    res = requests.get(f'https://www.indeed.co.in/{name}-jobs-in-{city},-{state}')
    soup = BeautifulSoup(res.text,'html.parser')
    job_name = soup.select('.jobtitle')
    for i in range(len(job_name)):
        job_name = soup.select('.jobtitle')[i].getText()
        job_n = soup.select('.company')[i].getText()
        job_b = soup.select('.location')[i].getText()
        try :
            job_money = soup.select(".salaryText")[i].getText()
        except :
            job_money = ""
        print(job_name)
        print(job_n)
        print(job_b)
        print(job_money)
        speak(job_name)
        speak(job_n)
        speak(job_b)
        speak(job_money)
def commands():
    print("\n\nActions\t\t\t\t\tCommands")
    print("____________________________________________________________________")
    print('''
1.search wikipedia \t\t\twikipedia _query_
2.search google \t\t\tgoogle _query_
3.Open youtube, stackoverflow\t\topen _query_
4.Ask query to Karl\t\t\t i have a query
5.play music\t\t\t\t play music
6.Open vs code \t\t\t\t open vs code
7.Send email \t\t\t\tsend email
8.Calculations \t\t\t\tdo calculation
9.Set reminder\t\t\t\t set a reminder
10.Tell Horoscope\t\t\t Tell about my horoscope
11.History of today\t\t\ttell me the history of today
12.Tell jokes \t\t\t\ttell me a joke
13.Tell Riddle \t\t\t\t tell me a riddle
14.Tells the current time\t\twhat's the time
15.Send SMS\t\t\t\tsend a sms
16.Toss a coin\t\t\t\tToss a coin
17.Current weather\t\t\tTell me the current weather
18.Open Karl pad\t\t\t Open karlpad
19.Open calculator \t\t\t Open calculator
20.Trending news \t\t\t tell me the trending news 
21.Set alarm\t\t\t\t set an alarm
22.Search jobs\t\t\t\t search jobs''')
    print("____________________________________________________________________\n\n")


if __name__ == "__main__":
    wishMe()
    commands()
    
    while True:
        
        query = takeCommand().lower()

        # Query based result
        if 'wikipedia' in query:
            speak('karl: Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia\n")
                print(results)
                speak(results)
            except:
                print("Can't find the data you are looking for..\n")
                print(f"Try: google {query}")
        elif 'google' in query:
            query  = query.replace("google","")
            for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
                link = j
                webbrowser.open(f"{link}")
        elif 'query' in query:
            def google(name):
                name2 = name.replace(" ","+")
                res = requests.get(f'https://www.google.com/search?q={name2}&oq={name2}&aqs=chrome..69i57j46j69i59j35i39j0j46j0l2.4948j0j7&sourceid=chrome&ie=UTF-8',headers=headers)
                print("Searching for answers......\n")
                speak("Searching for answers...!")
                soup = BeautifulSoup(res.text,'html.parser')
                try:
                    try:
                        ans = soup.select('.RqBzHd')[0].getText().strip().upper()
                        print(ans)
                        speak(ans)
                    except:
                        try:
                            ans=soup.select('.e24Kjd')[0].getText().strip().upper()
                            print("Google says:")
                            print(ans)
                            speak(ans)
                        except:
                            ans=soup.select('.kno-rdesc span')[0].getText().strip().upper()
                            print("Google says:")
                            print(ans)
                            speak(ans)
                except:
                    print("Couldn't find the answer you are looking for....")
                    speak("Couldn't find what you are looking for....")
                    for j in search(name, tld="co.in", num=1, stop=1, pause=2): 
                        link = j
                        speak("Try visit the below url")
                        print("Visit: ",link)
                        speak("or")
                        print("Or")
                        print(f"Use command : google {name}")
                        speak(f"Use command : google {name}")

            print("what is your query?")
            speak("what is your query?\n")
            google(input())

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            song = random.randint(0,len(songs)-1)
            print(songs[song])  
            speak(f"playing{songs[song]}")
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M") 
            t_12 = time.strptime(strTime, "%H:%M")
            time_12_hour = time.strftime( "%I:%M %p", t_12 )
            print(f"Karl: The current time is {time_12_hour} sir")
            speak(f"The current time is {time_12_hour} sir")
        elif 'code' in query:
            print("Karl: Opening vs code sir")
            speak("Opening vs code sir")
            codePath = "C:\\Users\\abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)
        elif 'email' in query:
            try:
                print("tell me the subject sir")
                speak("tell me the subject sir")
                subject = takeCommand()
                print(subject)
                print("What should I say sir?")
                speak("What should I say sir?")
                content = takeCommand()
                print(content)
                print("To whom you want to send sir")
                speak("To whom you want to send sir")
                to = takeCommand()
                print(to)
                '''
                print("is the subject is correct sir?")
                speak("is the subject is correct sir?")
                reply = takeCommand()
                if reply=='no':
                    print("please Type the subject of email sir\n")
                    speak("please Type the subject of email sir")
                    subject= input()
               
                print("is it what you want to say sir")
                speak("is it what you want to say sir")
                reply = takeCommand()
                if reply=='no':
                    print("please Type your content sir\n")
                    speak("Please enter the ccontent sir")
                    content= input()

                print("is it the mail id  of that person to whom you want to send sir")
                speak("is it the mail id  of that person to whom you want to send sir")
                reply = takeCommand()
                if reply =='no':
                    print("please Type the email address of the person sir!\n")
                    speak("please Type the email address of the person sir!")
                    to = input() 
                '''     
                email = EmailMessage()
                email['from'] = 'ABhay Parashar'
                email['to'] = f'{to}'
                email['subject'] = f'{subject}'

                email.set_content(f'{content}')

                with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login('YOUR_EMAIL_ADDRESS','YOUR_PASSWORD')
                    smtp.send_message(email)
                    print("Email has been sent! sir")
                    speak("Email has been sent! sir")
                sleep(1)
            except Exception as e:
                print(e)
                speak("Some error occur. I am not able to send this email") 
                sleep(1)        
        elif 'reminder' in query:
            toaster = ToastNotifier()
            try:
                print("Title of reminder")
                speak("Title of reminder\n")
                header = takeCommand()
                print("Message of reminder")
                speak("Message of reminder\n")
                text = takeCommand()
                print("In how many minutes?")
                speak("In how many minutes?\n")
                time_min = takeCommand()
                time_min=float(time_min)
            except:
                header = input("Title of reminder\n")
                text = input("Message of remindar\n")
                time_min=float(input("In how many minutes?\n"))
            time_min = time_min * 60
            print("Setting up reminder..")
            time.sleep(2)
            print("all set!")
            time.sleep(time_min)
            toaster.show_toast(f"{header}",
            f"{text}",
            icon_path="C:\\Users\\abhay\\Desktop\\ChatBot\\profile.ico",
            duration=10,
            threaded=True)
            while toaster.notification_active(): time.sleep(0.005)      
        elif 'calculation' in query:
            def add(x, y):
                return x + y
            def subtract(x, y):
                return x - y
            def multiply(x, y):
                return x * y
            def divide(x, y):
                return x / y
            while True:
                print("Select operation.")
                speak("Select Operation:")
                print("\n1.Add\t2.Subtract\t3.Multiply\t4.Divide\te for exit")
                speak("\n1.Add\t2.Subtract\t3.Multiply\t4.Divide\te for exit")
                try:
                    speak("Choose one:")
                    choice=takeCommand()
                except:
                    choice = input("Enter choice(1/2/3/4): ")
                if choice in ('1', '2', '3', '4'):
                    speak("Your first number")
                    num1=takeCommand()
                    num1=float(num1)
                    speak("Your second number")
                    num2=takeCommand()
                    num2=float(num2)
                    if choice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))

                    elif choice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))

                    elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))

                    elif choice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))
                else:
                    print("Thanks for using!")
                    break
        elif 'history' in query:
            history()
        elif 'jobs' in query:
            jobs()
        elif 'alarm' in query:
            alarm_time = input("Enter the time of alarm to be set:HH:MM:SS AM/PM\n")
            alarm_hour=alarm_time[0:2]
            alarm_minute=alarm_time[3:5]
            alarm_seconds=alarm_time[6:8]
            alarm_period = alarm_time[9:11].upper()
            print("Setting up alarm..")
            sleep(1)
            print("alarm set....")
            while True:
                now = datetime.datetime.now()
                current_hour = now.strftime("%I")
                current_minute = now.strftime("%M")
                current_seconds = now.strftime("%S")
                current_period = now.strftime("%p")
                if(alarm_period==current_period):
                    if(alarm_hour==current_hour):
                        if(alarm_minute==current_minute):
                            if(alarm_seconds==current_seconds):
                                print("Wake Up!")
                                playsound('C:\\Users\\abhay\\Desktop\\ChatBot\\alarm.wav')
                                break
        elif 'horoscope' in query:
            def horoscope(name):
                name2=name
                res = requests.get(f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={name2}',headers=headers)
                print("Searching For Horoscope")
                soup = BeautifulSoup(res.text,'html.parser')
                try:
                    ans = soup.select('.main-horoscope p')[0].getText().strip().upper()
                    sign = soup.select('h1')[0].getText().strip().upper()
                    print(f"\n{sign} for Today..\n")
                    print(ans)
                    speak(ans)
                    
                except:
                    print("Sorry can't find")
    
            print("Enter your Sign\n")
            sign = input().lower()
            signs= {
                    'aries':1,
                    'taurus':2,
                    'gemini':3,
                    'cancer':4,
                    'leo':5,
                    'virgo':6,
                    'libra':7,
                    'scorpio':8,
                    'sagittarius':9,
                    'capricorn':10,
                    'aquarius':11,
                    'pisces':12
            }

            horoscope(signs.get(sign))
        elif 'joke' in query:
            def jokes():
                res = requests.get(f'https://fungenerators.com/random/joke',headers=headers)
                print("Looking for a joke\n")
                soup = BeautifulSoup(res.text,'html.parser')
                title=soup.select('h3.text-muted')[0].getText().strip()
                joke=soup.select('p')[0].getText().strip()
                print(title)
                speak(title)
                print(joke)
                speak(joke)
            jokes()
        elif 'riddle' in query:
            def riddle():
                res = requests.get(f'https://www.riddles.nu/random',headers=headers)
                print("Looking for a riddle\n")
                soup = BeautifulSoup(res.text,'html.parser')
                riddle=soup.select('blockquote p')[0].getText().strip()
                answer=soup.select('.well-small ')[0].getText().strip()
                print(riddle)
                speak(riddle)
                print("Think....")
                time.sleep(4)
                print(answer)
                speak(answer)
            riddle() 
        elif 'coin' in query:
            playsound('C:\\Users\\abhay\\Desktop\\ChatBot\\coin.wav')
            num = random.randint(0,1)
            if num==0:
                print("heads")
                speak("heads")
            else:
                print("tails")
                speak("tails")
        elif 'weather' in query:
            def weather():
                res = requests.get(f'https://www.google.com/search?q=weather&oq=weather&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
                print("Searching For Weather......\n")
                soup = BeautifulSoup(res.text,'html.parser')   
                location = soup.select('#wob_loc')[0].getText().strip()  
                time = soup.select('#wob_dts')[0].getText().strip()       
                info = soup.select('#wob_dc')[0].getText().strip() 
                weather = soup.select('#wob_tm')[0].getText().strip()
                print(location)
                print(time)
                print(info)
                print(weather+"°C") 
                speak(f"It's {weather}°C in {location} feels like {info} ")
            weather()
        elif 'creator' in query:
            print("I am created by Abhay parashar")
            speak("I am created by Abhay parashar")
        elif "what can you do" in query:
            commands()
        elif 'sms' in query:
            speak("Taking you to the app.....")
            sleep(1)
            os.system('python C:\\Users\\abhay\\Desktop\\ChatBot\\message\\message.py')
            speak("Thanks for using out service")
        elif 'karlpad' in query:
            speak("Opening karl pad....")
            sleep(1)
            os.system('python C:\\Users\\abhay\\Desktop\\ChatBot\\karlpad\\karlpad.py')
            speak("Thanks for using out service")
        elif 'calculator' in query:
            speak("Opening Calculator")
            sleep(1)
            os.system('python C:\\Users\\abhay\\Desktop\\ChatBot\\calculator\\calculator.py')
            speak("Thanks for using out service")
        elif 'news' in query:
            def trndnews(): 
                    url = " http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
                    page = requests.get(url).json() 
                    article = page["articles"] 
                    results = [] 
                    for ar in article: 
                        results.append(ar["title"]) 
                    for i in range(len(results)): 
                        print(i + 1, results[i]) 
                    speak("here are the top trending news....!!")
                    speak("Do yo want me to read!!!")
                    reply = takeCommand().lower()
                    reply = str(reply)
                    if reply == "yes":
                        speak(results)
                    else:
                        speak('ok!!!!')
                        pass
            trndnews() 


        elif 'bye' in query:    
            speak("have a nice day sir")
            break
        else :
            speak("Sorry i can't help in this")
