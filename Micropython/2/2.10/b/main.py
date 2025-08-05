from peripherals import LedSet, LedClr
from my_peri import LedPoint
import time

i = 0
while(j < 8):
    if i < 4:
        j = i
    else:
        j = 3 - i
        
    LedPoint(j)
    time.sleep(1)
    i += 1
    