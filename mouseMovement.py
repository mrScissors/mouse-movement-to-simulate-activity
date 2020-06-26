import time
from random import randint
import pyautogui

while True:
    r = randint(5, 100)
    c = -randint(5, 100)
    pyautogui.move(r, c, duration=0.2)
    pyautogui.move(-r, -c, duration=0.2)
    pyautogui.click(clicks=2, interval = 1)
    time.sleep(randint(5, 8))
