from peripherals import LedSet, LedClr
from my_peri import LedPoint
import time


leds = [0, 1, 2, 3]

for i in leds:
    LedPoint(i)
    time.sleep(1)
    
for i in reversed(leds):
    LedPoint(i)
    time.sleep(1)
    
LedPoint(None)