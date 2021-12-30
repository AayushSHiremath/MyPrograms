import pyttsx3
import speech_recognition as sr
import pywhatkit
import os
import webbrowser
import time
import datetime
import sys
import random

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
#Lists of commands
My_Joke_List = ["can a kangaroo jump higher than a house , of course , a house cant jump at all.", 
            "how does a solar system keep its pants up , with the asteroid belt.",
            "what do you call someone who points out the obvious , someone who points out the obvious.",
            "your nose cannot be 12 inches long , otherwise it would be a foot.",
            "how do robots eat chips , with microchips.",
            "Why couldnt the leopard play hide and seek? Because he was always spotted.",
            "How does the ocean say hello? It waves.",
            "What starts with E, ends with E, and has only 1 letter in it? An Envelope.",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "Why cant you trust an atom? Because they make up everything.",
            "Why did the school kids eat their homework? Because their teacher told them it was a piece of cake.",
            "How do trees access the internet? They log in.",
            "What is the tallest building in the entire world? The library, because it has so many stories.",
            "Why did the painting go to jail? It was framed.",
            "Why are obtuse angles so depressed? Because theyre never right.",
            "Why should you worry about the math teacher holding graph paper? Shes definitely plotting something.",
            "Why was the math book sad? Because it had so many problems.",
            "Im really good at sleeping. I can do it with my eyes closed.",
            "Why cant a bicycle stand on its own? It is two tired.",
            "Can February March? No but April May"]

My_WhoAreYou_List = ["I am Jarvis , Your Personal Assistant , I am here to help , let me know if you need anything", "I am Jarvis your virtual Assistant , I can play music , tell you what the time is , all you need to do is ask"]

My_WhereAreYouFrom_List = ["First I was an Idea , Then someone did a lot of experiments on me , and that's where i came from", "I come from the headquarters of apple company , just kidding I am from A house in Banglore."]

My_WhoMadeYou_List = ["I was created by elon musk , Just kidding I was made by an awesome kid who knows how to code", "I was born by a bright mind who started working to create an Assistant , Just for you"]

My_Hello_List = ["Hello sir , how are you", "Hello Sir , Didnt see you there.", "Hey , Whats up", "Hey there , I was busy planning New year's eve , I am very exicted."]

My_ThankYou_List = ["You are very welcome sir", "I am honoured to serve.", "No worries , I am here to help", "Just doing my job"]

My_WhatCanYouDo_List = ["I can do many things , some of them are Open youtube , what is the time.", "I can do many things , and I'm learning more , You can ask me to do things like open youtube , or show a video on youtube", "Here are some things you can try , open gmail or show me updatess on 8 bitryan."]

My_HowHasYourDayBeen_List = ["I'm splendid , thank you for asking", "Great , Thanks", "Its been good , you are very kind to ask , especially in these times"]

My_TellMeYourSecret_List = ["Here's a secret, I am not actually a person", "Okay but keep it to yourself , Sometimes I just pretend to understand sarcasm"]

My_ILoveYou_List = ["You should know the feelings mutual", "no wonder , If I was you , I would love me too", "I love me too"]

My_YouAreTheBest_List = ["That's so funny , i was just thinking the same thing about you", "Thats nice to hear , I hope you know the fellings mutual"]

My_WhatCanYouNotDo_List = ["I cant give you a Hi-fi , but i still think you are great", "I haven't tested this , But I am pretty sure i can't swim", "I cant really handle any spicy food , or any food", "I am not very good at pull ups"]

My_HowDoYouDoThat_List = ["It was either magic , or good programming", "Magic", "shh , it's a secret", "I am not sure"]

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
                engine.say(random.choice(My_WhoAreYou_List))
                engine.runAndWait()                

            elif 'where are you from' in command:
                engine.say(random.choice(My_WhereAreYouFrom_List))
                engine.runAndWait()

            elif 'who made you' in command:
                engine.say(random.choice(My_WhoMadeYou_List))
                engine.runAndWait()     

            elif ('hello jarvis' in command) or ('good morning' in command) or ('good afternoon' in command) or ('good evening' in command):
                engine.say(random.choice(My_Hello_List))
                engine.runAndWait()

            elif ('thank you' in command) or ('thank you so much' in command):
                engine.say(random.choice(My_ThankYou_List))
                engine.runAndWait()

            elif ('what can you do' in command) or ('what are your features' in command) or ('Can you help me' in command):
                engine.say(random.choice(My_WhatCanYouDo_List))
                engine.runAndWait()

            elif ('how has your day been' in command) or ('how was your day' in command):
                engine.say(random.choice(My_HowHasYourDayBeen_List))
                engine.runAndWait()

            elif ('tell me your secret' in command) or ('tell me a secret' in command):
                engine.say(random.choice(My_TellMeYourSecret_List))
                engine.runAndWait()

            elif ('i hate you' in command) or ('you are the worst' in command):
                engine.say("Well i'm still learning , what do we need to fix")
                engine.runAndWait()

            elif 'i love you' in command:
                engine.say(random.choice(My_ILoveYou_List))
                engine.runAndWait()

            elif 'you are the best' in command:
                engine.say(random.choice(My_YouAreTheBest_List))
                engine.runAndWait()

            elif 'What can you not do' in command:
                engine.say(random.choice(My_WhatCanYouNotDo_List))
                engine.runAndWait()
                
            elif ('how do you do that' in command) or ('how did you do that' in command):
                engine.say(random.choice(My_HowDoYouDoThat_List))
                engine.runAndWait()
            
            elif 'tell me a joke' in command:
                engine.say(random.choice(My_Joke_List))
                engine.runAndWait()

            elif 'who is the most famous youtuber' in command:
                engine.say("the most famous youtuber in the world is Pewdiepie")
                engine.runAndWait()

            elif 'self destruct' in command:
                engine.say("Self destructing in 3, 2, 1         Actually I think I will stick around")
                engine.runAndWait()

             elif 'do you breathe' in command:
                engine.say("I dont , which means I never have to worry about bad breath.")
                engine.runAndWait()
            
             elif 'can you eat' in command:
                engine.say("My device is all charged up , i am ready to help")
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