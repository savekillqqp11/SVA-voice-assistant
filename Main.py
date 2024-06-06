from unittest import result
import pyttsx3 # C:/Users/trist/AppData/Local/Microsoft/WindowsApps/python3.10.exe -m pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime  # pip install DateTime
import os  # pip install os-sys
import subprocess  # pip install subprocess.run
import webbrowser as wb  # pip install pycopy-webbrowser
import pyautogui  # pip install PyAutoGUI
import wikipedia  # pip install wikipedia
import pyjokes  # pip install pyjokes
from time import sleep
import pydub #pip install pydub
from pydub import AudioSegment
from pydub.playback import play
import elevate
import subprocess
from googletrans import Translator
from translate import Translator as OfflineTranslator

# Request elevated privileges
elevate.elevate()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Set the voice to a female voice
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Set the voice speed
voicespeed = 150  # setting speed
engine.setProperty('volume', 1.0)
engine.setProperty('rate', voicespeed)

# Translator object
translator = Translator()

# Load the audio file
def speak():
    song = AudioSegment.from_mp3("path/to/file.mp3")
    play(song)
    
chrome_path = r'C:/Program Files/Google/Chrome/Application/chrome.exe %s'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='de-DE')
        print("You said:", query)
        
        # Offline translation
        translator = OfflineTranslator(to_lang="en", from_lang="de")
        english_query = None
        while english_query is None:  # Wait until translation is finished
            english_query = translator.translate(query)
        print("Translated to English:", english_query)
        return english_query.lower()
    except Exception as e:
        print(e)
        return "---"



def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("das momentane datum ist, ")
    speak(day)
    speak(month)
    speak(year)


def wishme():
    speak("wilkommen zurück sir")

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Guten morgen")
    elif hour >= 12 and hour <= 18:
        speak("Guten mittag")
    elif hour >= 18 and hour <= 24:
        speak("Guten abend")
    else:
        speak("Gute nacht")

    speak("wie kann ich ihnen helfen?")


# Open chrome/Website
def open_chrome():
    # url u want to open
    url = 'http://www.google.com/'
    # Windows
    wb.get(chrome_path).open(url)


if __name__ == "__main__":

    # wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()

        if "date" in query:
            date()

        # Open chrome/Website
        if "open chrome" in query:
            open_chrome()

        # Wikipedia search
        elif "wikipedia" in query:
            speak("suchen...")
            query = query.replace("wikipedia", "")
            url = 'https://www.wikipedia.de/'
            # Windows
            wb.get(chrome_path).open(url)
            speak(result)
            print(result)
            
        #chrome search
        elif "search" in query:
            speak("Was soll ich für sie suchen?")
            search_query = takeCommand().lower()
            url = f"https://www.google.com/search?q={search_query}"
            wb.get(chrome_path).open(url)

        # Launch applications
        elif "open notepad" in query:  # if open notepad in statement
            speak("öffne notepad")  # speak
            location = r"C:/WINDOWS/system32/notepad.exe"  # location
            notepad = subprocess.Popen(location)  # location of a software you want tot opem

        elif "close notepad" in query:
            speak("schließe notepad")
            notepad.terminate()  # terminate


        # Random jokes
        elif "joke" in query:
            speak(pyjokes.get_jokes())

        # Logout / Shutdown / Restart
        elif "log out" in query:
            speak('du wirst in 5 sekunden ausgeloggt')
            sleep(5)
            os.system("shutdown - l")

        elif "shut down" in query:
            speak('Computer schaltet in 5 sekunden aus')
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak('Neustart in 5 sekunden')
            sleep(5)
            os.system("shutdown /r /t 1")

            # <-------------------------Pyautogui  Features--------------------->

        elif "hidden menu" in query:
            # Win+X: Open the hidden menu
            pyautogui.hotkey('winleft', 'x')

        elif "task manager" in query:
            # Ctrl+Shift+Esc: Open the Task Manager
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif "task view" in query:
            # Win+Tab: Open the Task view
            pyautogui.hotkey('winleft', 'tab')

        elif "take screenshot" in query:
            # win+perscr
            pyautogui.hotkey('winleft', 'prtscr')
            speak("done")

            # Take screenshot save in Given location
            '''        
        elif "take screenshot" in query:
            img = pyautogui.screenshot()
            img.save("C:/screenshot_1.png")  # file mane and location
            speak("Done")
            '''

        elif "snip" in query:
            pyautogui.hotkey('winleft', 'shift', 's')

        elif "close app" in query:
            # alt + f4: close this app
            pyautogui.hotkey('alt', 'f4')

        elif "setting" in query:
            # win+i = open setting
            pyautogui.hotkey('winleft', 'i')

        elif "new virtual desktop" in query:
            # Win+Ctrl+D: Add a new virtual desktop
            pyautogui.hotkey('winleft', 'ctrl', 'd')

        elif "hello" in query:
            speak('Hallo sir wie kann ich ihnen helfen?')
            print(result)

        elif "anime" in query:
            speak("okay")
            query = query.replace("h*****", "")
            url = 'https://www.hammerporno.xxx/hentai-xxx/'
            # Windows
            wb.get(chrome_path).open(url)
            speak(result)
            print(result)

        elif "hoyolab" in query:
            speak('öffne hoyolab')
            url = 'https://www.hoyolab.com'
            wb.get(chrome_path).open(url)
            speak(result)
            print(result)

        elif "youtube" in query:
            speak('öffne youtube')
            url = 'https://www.youtube.com'
            wb.get(chrome_path).open(url)
            speak(result)
            print(result)
            
            
        elif "open impact" in query:
            speak("öffne genshin impact")
            location = r"D:\\Games\\genshin\\Genshin Impact game\\GenshinImpact.exe"
            if os.path.exists(location):
                speak("Genshin Impact wird geöffnet!")
                genshin = subprocess.Popen(location)
            else:
                speak("Fehler 404. .exe datei wurde nicht gefunden!")
                
            
        elif "favourite playlist" in query:
            speak('öffne deine absolute favourite playlist!')
            url = 'https://www.youtube.com/watch?v=lp0J_Sv_Q3o&list=PL9pAJgYABeiGh0pw3_Hzs29pebg4j1O1c&pp=gAQBiAQB'
            wb.get(chrome_path).open(url)
            speak(result)
            print(result)
            
        elif "thank you" in query:
            speak("Kein Problem sir")
            print(result)
            
        elif "how are you" in query:
            speak('mir geht es gut und ihnen?')
            print(result)
            
        elif "how old are you" in query:
            speak('ich wurde zuletzt geupdatet am 06.06.2024')
            print(result)
            
        elif "discord" in query:
            speak("Öffne Discord")
            print(result)
            location = r"C:\Users\trist\AppData\Local\Discord\app-1.0.9148\Discord.exe" #in case of path not found please change trist to your user folder name :D
            if os.path.exists(location):
                speak("Genshin Impact wird geöffnet!")
                genshin = subprocess.Popen(location)
            else:
                speak("Fehler 404. .exe datei wurde nicht gefunden!")