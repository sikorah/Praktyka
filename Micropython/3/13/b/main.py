from my_peri import LedPoint, ReadKeyboard, LedBar
import time


but_prev = None
counter = 0
while(True):
    but_current = ReadKeyboard()
    if (but_current != None) & (but_prev == None):
        counter = (counter + 1) % 5
        LedBar(counter)
    but_prev = but_current
    time.sleep(0.1)