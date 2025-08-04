from peripherals import LedSet, LedClr
from my_peri import LedPoint
import time
    
i = 0
while(i<4):
    LedPoint(i)
    i += 1
    time.sleep(1)
LedPoint(None)