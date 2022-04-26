import speech_recognition as sr
# need to install pyaudio through whl file
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query


if __name__ == "__main__":
    speak("I am Vision, how may I help you?")
    print()

    flag=True
    while flag:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who is' in query:
            query = query.replace('who is ', '')
            info = wikipedia.summary(query, sentences=2)
            print(info)
            speak(info)

        elif 'created you' in query:
            speak("I was created by Somil Doshi, Preet Desai, Ronak Dhakad.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'search' in query:
            query = query.replace("search ","")
            webbrowser.open("https://google.com/search?q="+query)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Somil Doshi, Preet Desai, Ronak Dhakad.")

        elif "thank you vision" in query:
            flag = False
            speak("Thank you for using me.")
            speak("This is vision signing off.")

        else:
            speak('Please repeat the command')
