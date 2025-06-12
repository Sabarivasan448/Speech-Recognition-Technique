import speech_recognition as sr
import pyttsx3
from commands import execute_command

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎮 Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

if __name__ == "__main__":
    speak("Voice-controlled gaming started. Say your command.")
    while True:
        command = listen_for_command()

        if "exit" in command or "quit" in command:
            speak("Exiting game control.")
            break
        elif command:
            executed = execute_command(command)
            if executed:
                speak(f"Executing {command}")
            else:
                speak("Command not recognized.")
