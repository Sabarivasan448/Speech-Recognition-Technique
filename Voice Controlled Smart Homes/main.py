import speech_recognition as sr
import pyttsx3

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Smart Home device state
devices = {
    "light": False,
    "fan": False,
    "ac": False
}

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was a problem with the speech recognition service.")
        return ""

def turn_on_device(command):
    for device in devices:
        if device in command:
            devices[device] = True
            speak(f"{device.capitalize()} turned on.")
            return
    speak("Device not recognized.")

def turn_off_device(command):
    for device in devices:
        if device in command:
            devices[device] = False
            speak(f"{device.capitalize()} turned off.")
            return
    speak("Device not recognized.")

def device_status():
    status = []
    for device, state in devices.items():
        status.append(f"{device}: {'on' if state else 'off'}")
    speak("Device status: " + ", ".join(status))

if __name__ == "__main__":
    speak("Voice-controlled smart home activated. How can I help you?")
    while True:
        command = listen_command()
        if not command:
            continue

        if "turn on" in command:
            turn_on_device(command)
        elif "turn off" in command:
            turn_off_device(command)
        elif "status" in command:
            device_status()
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I can't handle that command yet.")
