this is a open source project originally by savekillqqp and i do not make any money with this i made it for fun.
this is a virtual assistant without any paid subscriptions like openai or anything like that all it uses are python and some python packages which will all install when you click on install dependencies. its currently available in the ENGLISH and German language as can be seen by the EN and DE files (EN = english and DE = deutsch/German)

windows defender can cause issues with the assistant for some reason so you should disable it

please install the VoiceAssistant.zip file

to properly get it to work please use the installDepends in your language for english press the installDependsEN.bat for german InstallDependsDE.bat it will then install python if you do not yet have it and all of the python packages and libraries. the libraries include:

unittest
pyttsx3
speech_recognition
datetime 
os
subprocess
webbrowser
pyautogui
wikipedia
pyjokes
time
pydub
elevate
subprocess
googletrans
translate


commands:
open chrome = opening google in the chrome browser
search      = will ask you what to search and whatever you say after it asked you will be googled.
youtube     = opens youtube.com in chrome
time        = tells you the current time
date        = tells you the current date
wikipedia   = opens wikipedia
open notepad= opens microsoft build in notepad
close notepad= closes the notepad
joke        = currently not working properly, supposed to tell you a random joke from the pyjoke library. instead tells you every single joke in py library.
log out     = will log you out of windows in 5 seconds
shut down   = will shut down your windows pc in 5 seconds
restart     = restarts your pc in 5 seconds
hidden menu = opens hidden menu accessable by pressing hotkey winleft + x
task manager= opens task manager
task view   = opens task view
take screenshot= takes screenshot and saves it under "C:/screenshot_1.png
snip        = winleft, shift, s
close app   = closes current application
settings    = opens windows settings by pressing hotkeys winleft+i
new virtual desktop= opens new virtual desktop
hello       = smalltalk. gives you the response: Hello sir how may i help you? in case youre bored
anime       = .... opens... a hentai website.... dont mind this command...
hoyolab     = since the creator (me) and his friends play hoyoverse games like genshin this is a shortcut for hoyolab.com
youtube     = takes you to youtube.com
open impact = opens genshin impact, needs to be changed for your genshin impact.exe directory. also its not open genshin cuz the speech recog doesnt like the word genshin
favourite playlist= will open my absolute favourite playlist (music playlist on youtube) you can change it to the directory of your playlists tho
thank you   = smalltalk will give you the response: no problem sir
how are you = smalltalk will give you the response: im fine, how about you sir?
how old are you?= will give you the date of her last update
discord     = needs to be changed, rn its the directory it normally gets send to just with my username. if you want it to work change C:\User\trist. change the trist to your name and keep the rest the same it should work.





in case you wish to add more features or delete some you can always do so since the MainEN.py and Main.py are both the full codes used in the assistant. the bat file only installs the base dependencies like pyttsx3 and speechrecog and so on to make it work. you can install more yourself if you so wish.

to add a website you can use this empty code:


elif "enter name for site here" in query: #enter the command. basically what you have to say to open the website.
	speak("enter what you want her to say here") #enter what you want the voice assistant to say here
	url = 'https://yourURLHere' #add your url for the website here
	wb.get(chrome_path).open(url) #gets chrome
	speak(results) #speaks the results
	print(results) #prints the results


