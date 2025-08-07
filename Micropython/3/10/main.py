from my_peri import LedPoint, ReadKeyboard
import time

leds = [0, 1, 2, 3, None]

while(True):
    button = ReadKeyboard()
    if button != None:
        LedPoint(button)