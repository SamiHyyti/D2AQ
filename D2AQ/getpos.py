from python_imagesearch.imagesearch import *
from pyautogui import*
import pyautogui
import keyboard
import time

while not keyboard.is_pressed('esc'):
    if keyboard.is_pressed('alt'):
        print(pyautogui.position())
