{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "please enter your requirement:\n",
      "open youtube\n",
      "please enter your requirement:\n"
     ]
    }
   ],
   "source": [
    "import pyttsx3\n",
    "import os\n",
    "\n",
    "pyttsx3.speak(\" hello..sir i am your tech assistance\")\n",
    "pyttsx3.speak(\"how can i help you\")\n",
    "\n",
    "while(1):\n",
    "    print(\"please enter your requirement:\")\n",
    "    p = input()\n",
    "    \n",
    "    if((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"explorer\"in p)or(\"this pc\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening window explorer\")\n",
    "       os.system(\"start explorer\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"cmd\"in p)or(\"command prompt\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening command prompt\")\n",
    "       os.system(\"start cmd\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"control panel\"in p)or(\"control\" in p)or(\"panel\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening control panel\")\n",
    "       os.system(\"start control\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"chrome\"in p)or(\"browser\" in p)or(\"chrome browser\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening chrome browser\")\n",
    "       os.system(\"chrome\")    \n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"internet\"in p)or(\"explorer\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening internet explorer\")\n",
    "       os.system(\"start iexplorer\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"notepad\"in p)or(\"text editor\" in p)or(\"editor\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening notepad\")\n",
    "       os.system(\"notetpad\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"media\"in p)or(\"player\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening window media player\")\n",
    "       os.system(\"wmplayer\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"camera\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening camera\")\n",
    "       os.system(\"start microsoft.windows.camera:\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"calc\"in p)or(\"calculator\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening calculator\")\n",
    "       os.system(\"start calc\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"calender\"in p)or(\"planer\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening calender\")\n",
    "       os.system(\"start outlookcal:\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"clock\"in p)or(\"time\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening clock\")\n",
    "       os.system(\"start ms-clock:\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"security\"in p)or(\"defender\" in p)or(\"windows defender\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening windows defender\")\n",
    "       os.system(\"start windowsdefender:\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"excel\"in p)or(\"microsoft excel\" in p)or(\"ms excel\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening microsoft excel\")\n",
    "       os.system(\"start excel\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"publisher\"in p)or(\"microsoft publisher\" in p)or(\"ms publisher\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening microsoft publisher\")\n",
    "       os.system(\"start mspub\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"outlook\"in p)or(\"microsoft outlook\" in p)or(\"ms outlook\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening microsoft outlook\")\n",
    "       os.system(\"start outlook\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"powerpoint\"in p)or(\"microsoft powerpoint\" in p)or(\"mspowerpoint\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening microsoft powerpoint\")\n",
    "       os.system(\"start powerpnt\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"word\"in p)or(\"microsoft word\" in p)or(\"msword\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening microsoft word\")\n",
    "       os.system(\"start winword\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"vlc\" in p)or(\"vlc player\" in p)or(\"video player\" in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening VLC midea player\")\n",
    "       os.system(\"start vlc\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"python\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening python interpreter\")\n",
    "       os.system(\"start python\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"google\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening google\")\n",
    "       os.system(\"start chrome google.com\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"facebook\"in p)or(\"fb\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening facebook\")\n",
    "       os.system(\"start chrome facebook.com\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"youtube\"in p)or(\"you tube\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening youtube\")\n",
    "       os.system(\"start chrome youtube.com\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"linkedin\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening linkedin\")\n",
    "       os.system(\"start chrome linkedin.com\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"instagram\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening instagram\")\n",
    "       os.system(\"start chrome instagram.com\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"amazon\"in p)or(\"amazon shopping\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening amazon\")\n",
    "       os.system(\"start chrome amazon.com\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"flipkart\"in p)or(\"flipkart shopping\"))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening flipkart\")\n",
    "       os.system(\"start chrome flipkart.com\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"myntra\"in p)or(\"myntra shopping\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening myntra\")\n",
    "       os.system(\"start chrome myntra.com\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"twitter\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening twitter\")\n",
    "       os.system(\"start chrome twitter.com\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"photos\"in p)or(\"galary\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening photos\")\n",
    "       os.system(\"start ms-photos:\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"setting\"in p)or(\"settings\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening pc setting\")\n",
    "       os.system(\"start ms-settings:\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"gmail\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening gmail\")\n",
    "       os.system(\"start chrome gmail.com\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"map\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening microsoft map\")\n",
    "       os.system(\"start ms-derive-to:\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"pdf reader\"in p)or(\"adobe pdf\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening Adobe pdf reader\")\n",
    "       os.system(\"start acrord32\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"skype\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening skype\")\n",
    "       os.system(\"start skype:\")\n",
    "    elif((\"run\" in p)or(\"execute\"in p)or(\"start\"in p)or(\"open\"in p))and((\"bin\"in p)or(\"recycle\"in p))and((\"do not\" not in p)and(\"not\"not in p)):\n",
    "       pyttsx3.speak(\"opening recycle bin folder\")\n",
    "       os.system(\"start explorer.exe shell:RecycleBinFolder\")\n",
    "    elif((\"shutdown\"in p))and ((\"pc\"in p)or(\"this\"in p)or(\"machine\"in p)or(\"computer\"in p))and((\"dont\"not in p)or(\"not\"in p)):\n",
    "         pyttsx3.speak(\"shutting down your pc\")\n",
    "         os.system(\"shutdown /s\")\n",
    "    elif((\"restart\"in p))and ((\"pc\"in p)or(\"this\"in p)or(\"machine\"in p)or(\"computer\"in p))and((\"dont\"not in p)or(\"not\"in p)):\n",
    "         pyttsx3.speak(\"restarting  your pc\")\n",
    "         os.system(\"shutdown /r\")\n",
    "    elif(\"exit\"in p)or(\"quite\"in  p)or(\"close\"in p):\n",
    "         pyttsx3.speak(\"thanks for using this service\")\n",
    "         break\n",
    "    else:\n",
    "         pyttsx3.speak(\"please try again\")\n",
    "         print(\"please try again\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
