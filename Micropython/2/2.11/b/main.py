from my_peri import LedPoint
import time

i = 0

while(True):
    if i == 0:
        step = 1
    elif i == 3:
        step = -1
    
    i += step
    LedPoint(i)
    time.sleep(0.5)