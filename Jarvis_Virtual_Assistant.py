import pyttsx3
import speech_recognition as sr
import pywhatkit
import os
import webbrowser
import time
import datetime
import sys

time = time.strftime("%I %M")

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def speak(audio):
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

wishMe()

speak("How may i help you?") 
engine.runAndWait()

def Listen():

    kill = False

    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
            print(command)

            #Basic commands

            if 'what is the time' in command:
                engine.say("The time is" + time)
                engine.runAndWait()  

            elif 'who are you' in command:
                engine.say("I am Jarvis , Your Personal Assistant , I am here to help , let me know if ")
                engine.runAndWait()

            elif 'where are you from' in command:
                engine.say("I come from the headquarters of apple company , just kidding I am from confidential area")
                engine.runAndWait()

            elif 'who made you' in command:
                engine.say("I was created by elon musk , Just kidding I was made by an awesome kid who knows how to code")
                engine.runAndWait()

            elif ('hello jarvis' in command) or ('good morning' in command) or ('good afternoon' in command) or ('good evening' in command):
                engine.say("Hello sir , how are you")
                engine.runAndWait()

            elif ('thank you' in command) or ('thank you so much' in command):
                engine.say("You are very welcome sir")
                engine.runAndWait()

            elif ('what can you do' in command) or ('what are your features' in command) or ('Can you help me' in command):
                engine.say("I can do many things , some of them are Open youtube , what is the time , what is the weather , etc.")
                engine.runAndWait()

            elif 'how has your day been' in command:
                engine.say('Its been good , you are very kind to ask , especially in these times')
                engine.runAndWait()

            elif 'tell me your secret' in command:
                engine.say("Okay but keep it to yourself , Sometimes I just pretend to understand sarcasm")
                engine.runAndWait()

            elif 'i hate you' in command:
                engine.say("Well i'm still learning , what do we need to fix")
                engine.runAndWait()

            elif 'i love you' in command:
                engine.say("I love me too")
                engine.runAndWait()

            elif 'you are the best' in command:
                engine.say("That's so funny , i was just thinking the same thing about you")
                engine.runAndWait()

            elif 'What can you not do' in command:
                engine.say("I cant give you a Hi-fi , but i still think you are great")
                engine.runAndWait()
                
            elif ('how do you do that' in command) or ('how did you do that' in command):
                engine.say("It was either magic , or good programming")
                engine.runAndWait()

            elif 'tell me a joke' in command:
                engine.say("This is an aquired taste , did you hear about the anti-gravity book , it seems that you cant put it down")
                engine.runAndWait() 

            elif 'who is the most famous youtuber' in command:
                engine.say("the most famous youtber in the world is Pewdiepie")
                engine.runAndWait()

            #Opening Apps

            elif ('open youtube' in command) or ('startup youtube' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("youtube.com")
                
            elif ('open gmail' in command) or ('startup gmail' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("gmail.com")

            #Videos

            elif 'secret command' in command:
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

            elif 'show me the new spider-man movie trailer' in command:
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/watch?v=JfVOs4VSpmA")

            #Pictures 

            elif ('show me pictures of cat' in command) or ('cat images' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://in.images.search.yahoo.com/search/images;_ylt=Awrx264_7rFh7UIAzwG7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=pictures+of+cats&fr2=piv-web&type=E211IN714G0&fr=mcafee")

            elif ('show me pictures of dogs' in command) or ('dog images' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://in.images.search.yahoo.com/search/images;_ylt=AwrxxP7o7rFhUncADgC7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=pictures+of+dogs&fr2=piv-web&type=E211IN714G0&fr=mcafee")

            #Music section

            elif 'play run it' in command:
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/watch?v=iCt-F8tD2BU")

            elif 'play butterfly effect' in command:
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/watch?v=iNw1fsUYzNM")

            elif 'play frequency 75' in command:
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/watch?v=8SASn5dTaxg")

            elif 'play get low' in command:
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/watch?v=l8RPFYq7mCo")

            elif 'play meet your right' in command:
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/watch?v=kuHr34QhzvE")

            #Youtubers

            elif ('search 8 bitryan on youtube' in command) or ('update on 8 bitryan' in command) or ('show me the latest video of 8 bitryan' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query=8+bitryan")

            elif ('search thinknoodles on youtube' in command) or ('update on thinknoodles' in command) or ('show me the latest video of thinknoodles' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query=thinknoodles")

            elif ('search minecraft curios on youtube' in command) or ('update on minecraft curios' in command) or ('show me the latest video of minecraft curios' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query=minecraft+curios")

            elif ('search the mythical sausage on youtube' in command) or ('update on the mythical sausage' in command) or ('show me the latest video of the mythical sausage' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query=the+mythical+sausage")

            elif ('search s u e v on youtube' in command) or ('update on s u e v' in command) or ('show me the latest video of s u e v' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query=suev")

            elif ('search cam and 18 on youtube' in command) or ('update on cam and 18' in command) or ('show me the latest video of cam and 18' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query=camman18")

            elif ('search trixy blocks on youtube' in command) or ('update on trixy blocks' in command) or ('show me the latest video of trixy blocks' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query=trixyblox")

            elif ('search canadian lad on youtube' in command) or ('update on canadian lad' in command) or ('show me the latest video of canadian lad' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query=canadian+lad")

            elif ('search benny productions on youtube' in command) or ('update on benny productions' in command) or ('show me the latest video of benny productions' in command):
                engine.say("Just a minute")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query=benny+productions")

            #Killing the command

            elif ('shutdown' in command) or ('go to sleep' in command) or ('do not talk' in command) or ('be quiet' in command) or ('shut up' in command):
                engine.say("Okay Sir")
                engine.runAndWait()
                kill = True
                sys.exit(1)

    except:
        print("")
        if kill:
            sys.exit(1)
        
while True:
    Listen()