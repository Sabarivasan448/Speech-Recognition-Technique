import speech_recognition as sr
import pyttsx3
from devices import SmartHome

# Initialize engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was a problem with the speech service.")
        return ""

# Initialize Smart Home
home = SmartHome()

# Main loop
if __name__ == "__main__":
    speak("Smart Home Assistant activated. How can I help?")
    while True:
        command = listen_command()
        if not command:
            continue

        if "turn on" in command:
            home.turn_on_device(command)
        elif "turn off" in command:
            home.turn_off_device(command)
        elif "status" in command:
            home.device_status()
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I can't handle that command yet.")
