import speech_recognition as sr
import webbrowser
import pyttsx3
import websiteLibrary
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "<API Key Here>"

def speak(text):
    engine.say(text)
    engine.runAndWait()

'''
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")
'''

def aiProcess(command):
    client = OpenAI(
        api_key="<API Key Here>",
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named wiseman skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return(completion.choices[0].message.content)

def processCommand(c):
    if c.lower().startswith("open"):
        site = c.lower().split(" ")[1]
        if site in websiteLibrary.website:
            weblink = websiteLibrary.website[site]
            webbrowser.open(weblink)
            speak(f"Opening {site}")
        else:
            speak(f"Sorry, I couldn't find the website {site} in my library.")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak(f"Sorry, I couldn't find the song {song}.")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Wiseman...")

    while True:
        # Listen for the wake word "Wiseman"
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print("recognizing...") 
            if(word.lower() == "wise man"):
                speak("Yes sir")
                # Listen for command
                with sr.Microphone() as source:
                    print("Wiseman Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)

        except sr.UnknownValueError:
            print("Google could not understand audio")
        except Exception as e:
            print("Google error; {0}".format(e))