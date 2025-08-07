from my_peri import LedPoint, ReadKeyboard
import time


but_prev = None
counter = 0
while(True):
    but_current = ReadKeyboard()
    if (but_current != None) & (but_prev == None):
        counter += 1 
        print('but:', but_current)
        print('counter:', counter)
    but_prev = but_current
    time.sleep(0.1)