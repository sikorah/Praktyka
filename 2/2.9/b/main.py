from peripherals import LedSet, LedClr
from my_peri import LedPoint
import time

i = 0
while(i < 4):
    LedPoint(i)
    time.sleep(1)
    i += 1
LedPoint(None)