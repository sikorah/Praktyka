from my_peri import LedPoint, ReadKeyboard
import time


but_prev = None
while(True):
    but_current = ReadKeyboard()
    if (but_current != None) & (but_prev == None):
        print('but', but_current)
    but_prev = but_current
    time.sleep(0.1)