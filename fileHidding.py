import os
import keyboard
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

file_path = input("Enter the file address:")
clear()

privacy_status = False
last_keypress_time = 0
wait_time = 5  

def update_privacy_status():
    global privacy_status
    try:
        if not privacy_status:
            os.system(f"attrib +h +s +r {file_path} /s /d")
            privacy_status = True
        else:
            os.system(f"attrib -h -s -r {file_path} /s /d")
            privacy_status = False
    except Exception as e:
        print(f"Error occurred: {e}")

while True:
    if (keyboard.is_pressed("shift") or keyboard.is_pressed("ctrl")) and time.time() - last_keypress_time >= wait_time:
        update_privacy_status()
        clear()  # Konsolu temizle
        print("File Confidentiality:", privacy_status)
        last_keypress_time = time.time()
