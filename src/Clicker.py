# To simulate clicks
import pyautogui

# To use time intervals
from src.interval import getInterval
import time

# To toggle the clicker
import keyboard


pyautogui.FAILSAFE = True
HOTKEY = 'f6'


class Clicker():
    def __init__(self):
        self.interval = 0.1
        self.active = False

    def listen(self, buttonText, entries):
        print("Listening")
        keyboard.wait('f6')

        print("Hotkey pressed")
        self.interval = getInterval(entries)
        self.toggle(buttonText)
        self.listen(buttonText, entries)

    def click(self):
        while True:
            if self.active:
                print("Clicking")
                time.sleep(self.interval)
                pyautogui.leftClick()

    def activate(self):
        print("Activated")
        self.active = True

    def deactivate(self):
        print("Deactivated")
        self.active = False

    def toggle(self, buttonText):
        if self.active:
            buttonText.set('Start (F6)')
            self.deactivate()
        else:
            buttonText.set('Stop (F6)')
            self.activate()
