from peripherals import LedSet, LedClr
from my_peri import LedPoint
import time
    
for i in range(4):
    LedPoint(i)
    time.sleep(1)
    i += 1
    LedPoint(None)