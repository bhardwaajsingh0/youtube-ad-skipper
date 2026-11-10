import pyautogui
import time

print("Bot starting in 5 seconds... switch to YouTube")
time.sleep(5)

while True:
    try:
        # Look for the skip button on screen using the reference image
        button = pyautogui.locateOnScreen('skip2.png', confidence=0.5)
        if button is not None:
            print("Skip button found!")
            x, y = pyautogui.center(button)
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.click()
            time.sleep(2)
    except Exception as e:
        print("Error:", e)
    time.sleep(1)
