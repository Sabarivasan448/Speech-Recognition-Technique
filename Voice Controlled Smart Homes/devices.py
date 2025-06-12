from smart_speaker import speak

class SmartHome:
    def __init__(self):
        self.devices = {
            "light": False,
            "fan": False,
            "ac": False
        }

    def turn_on_device(self, command):
        for device in self.devices:
            if device in command:
                self.devices[device] = True
                speak(f"{device.capitalize()} turned on.")
                return
        speak("Device not recognized.")

    def turn_off_device(self, command):
        for device in self.devices:
            if device in command:
                self.devices[device] = False
                speak(f"{device.capitalize()} turned off.")
                return
        speak("Device not recognized.")

    def device_status(self):
        status = []
        for device, state in self.devices.items():
            state_str = "on" if state else "off"
            status.append(f"{device}: {state_str}")
        speak("Device status: " + ", ".join(status))
