import pyttsx3
import os

pyttsx3.speak(" hello..sir i am your tech assistance")
pyttsx3.speak("how can i help you")

while(1):
    print("please enter your requirement:")
    p = input()
    
    if(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("explorer"in p)or("this pc" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening window explorer")
       os.system("start explorer")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("cmd"in p)or("command prompt" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening command prompt")
       os.system("start cmd")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("control panel"in p)or("control" in p)or("panel" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening control panel")
       os.system("start control")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("chrome"in p)or("browser" in p)or("chrome browser" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening chrome browser")
       os.system("chrome")    
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("internet"in p)or("explorer" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening internet explorer")
       os.system("start iexplorer")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("notepad"in p)or("text editor" in p)or("editor" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening notepad")
       os.system("notetpad")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("media"in p)or("player" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening window media player")
       os.system("wmplayer")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("camera"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening camera")
       os.system("start microsoft.windows.camera:")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("calc"in p)or("calculator" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening calculator")
       os.system("start calc")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("calender"in p)or("planer" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening calender")
       os.system("start outlookcal:")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("clock"in p)or("time" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening clock")
       os.system("start ms-clock:")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("security"in p)or("defender" in p)or("windows defender" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening windows defender")
       os.system("start windowsdefender:")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("excel"in p)or("microsoft excel" in p)or("ms excel" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening microsoft excel")
       os.system("start excel")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("publisher"in p)or("microsoft publisher" in p)or("ms publisher" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening microsoft publisher")
       os.system("start mspub")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("outlook"in p)or("microsoft outlook" in p)or("ms outlook" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening microsoft outlook")
       os.system("start outlook")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("powerpoint"in p)or("microsoft powerpoint" in p)or("mspowerpoint" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening microsoft powerpoint")
       os.system("start powerpnt")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("word"in p)or("microsoft word" in p)or("msword" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening microsoft word")
       os.system("start winword")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("vlc" in p)or("vlc player" in p)or("video player" in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening VLC midea player")
       os.system("start vlc")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("python"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening python interpreter")
       os.system("start python")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("google"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening google")
       os.system("start chrome google.com")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("facebook"in p)or("fb"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening facebook")
       os.system("start chrome facebook.com")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("youtube"in p)or("you tube"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening youtube")
       os.system("start chrome youtube.com")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("linkedin"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening linkedin")
       os.system("start chrome linkedin.com")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("instagram"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening instagram")
       os.system("start chrome instagram.com")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("amazon"in p)or("amazon shopping"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening amazon")
       os.system("start chrome amazon.com")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("flipkart"in p)or("flipkart shopping"))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening flipkart")
       os.system("start chrome flipkart.com")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("myntra"in p)or("myntra shopping"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening myntra")
       os.system("start chrome myntra.com")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("twitter"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening twitter")
       os.system("start chrome twitter.com")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("photos"in p)or("galary"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening photos")
       os.system("start ms-photos:")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("setting"in p)or("settings"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening pc setting")
       os.system("start ms-settings:")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("gmail"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening gmail")
       os.system("start chrome gmail.com")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("map"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening microsoft map")
       os.system("start ms-derive-to:")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("pdf reader"in p)or("adobe pdf"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening Adobe pdf reader")
       os.system("start acrord32")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("skype"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening skype")
       os.system("start skype:")
    elif(("run" in p)or("execute"in p)or("start"in p)or("open"in p))and(("bin"in p)or("recycle"in p))and(("do not" not in p)and("not"not in p)):
       pyttsx3.speak("opening recycle bin folder")
       os.system("start explorer.exe shell:RecycleBinFolder")
    elif(("shutdown"in p))and (("pc"in p)or("this"in p)or("machine"in p)or("computer"in p))and(("dont"not in p)or("not"in p)):
         pyttsx3.speak("shutting down your pc")
         os.system("shutdown /s")
    elif(("restart"in p))and (("pc"in p)or("this"in p)or("machine"in p)or("computer"in p))and(("dont"not in p)or("not"in p)):
         pyttsx3.speak("restarting  your pc")
         os.system("shutdown /r")
    elif("exit"in p)or("quite"in  p)or("close"in p):
         pyttsx3.speak("thanks for using this service")
         break
    else:
         pyttsx3.speak("please try again")
         print("please try again")