from tkinter import Tk

from pynput.mouse import Controller
import keyboard

root = Tk()

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

del root

mouse = Controller()

AUS_X = SCREEN_WIDTH - SCREEN_WIDTH / 8
AUS_Y = SCREEN_HEIGHT / 20

while True:
    x, y = mouse.position
    if (x > AUS_X) and (y < AUS_Y):
        for i in range(0, 2, 1):
            keyboard.press_and_release('win+down')