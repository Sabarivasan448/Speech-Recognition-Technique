import pyautogui

# Mapping commands to keypresses
command_map = {
    "move forward": "w",
    "move back": "s",
    "move left": "a",
    "move right": "d",
    "jump": "space",
    "shoot": "ctrl",
    "crouch": "c",
    "reload": "r"
}

def execute_command(command):
    for phrase, key in command_map.items():
        if phrase in command:
            pyautogui.press(key)
            return True
    return False
