
from gtts import gTTS #text to speech
import os as o
from googlesearch import search #google search
import webbrowser 
from selenium import webdriver #clicking
import sys
import time
import speech_recognition as sr #speech recognition
from googletrans import Translator
import wikipedia

text='s'
def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Time Over, Thanks")
        try:
            text = r.recognize_google(audio)
            return format(text)
            
        except:
            print("Sorry could not recognize what you said")
            return "none"
            

def tts(mytext):
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("tts.mp3")
    o.system("tts.mp3")

def search(query):
    try: 
        from googlesearch import search 
    except ImportError: 
        print("No module named 'google' found") 
    for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
        return j      

def player(link):
    driver = webdriver.Firefox()
    driver.get(link)
    driver.find_element_by_tag_name('ytd-player').click()

#song search
def song():
    tts("Which song do you want to play?")
    print("Which song do you want to play?")
    text=speech()
    print(format(text))
    if format(text).lower()=="stop" or format(text).lower()=="exit":
        sys.exit()
    text1=str(text) + " youtube"   
    link=search(text1)
    link1= "Okay, playing "+ str(text)
    tts(link1)
    player(link)
    sys.exit()

def trans():
    tts("Speak what you want to translate")
    print("Speak what you want to translate")
    text = speech()
    destination_languages = {
        'Spanish': 'es',
        'Simplified Chinese': 'zh-CN',
        'Italian': 'it',
        'English': 'en',
        'Hindi': 'hi',
        'Mongolian': 'mn',
        'Russian': 'ru',
        'Ukrainian': 'uk',
        'French': 'fr',
        'Indonesian': 'id',
        'Japanese': 'ja',
        'Slovak': 'sk'
    }
    print(destination_languages)
    time.sleep(2)
    tts("Enter the Destination Language")
    print("Enter the Destination Language")
    dest=speech().capitalize()

    translator = Translator()
    print()
    print("Translated Output:",end = " ")
    out = translator.translate(text,destination_languages[dest]).text
    print(out)
    tts(out)

def wiki():
    tts("What do you wanna search about?:")
    var=input("What do you wanna search about?: ")
    print()
    print(wikipedia.summary(var,sentences=2))
    tts(wikipedia.summary(var,sentences=1))    

tts("What do you want to do?")
print("What do you want to do")
print("1. Play Songs")
print("2. Translate")
choice = speech()

print(choice)
if choice.lower() == "play songs":
    song()
elif choice.lower() == "translate":
    trans()
elif choice.lower() == "search on wikipedia":
    wiki()
