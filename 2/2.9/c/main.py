from peripherals import LedSet, LedClr
from my_peri import LedPoint
import time


iterations = [0, 1, 2, 3]

for i in iterations:
    LedPoint(i)
    time.sleep(1)
    i += 1
LedPoint(None)