from peripherals import LedSet, LedClr
from my_peri import LedPoint
import time


for i in [0, 1, 2, 3]:
    LedPoint(i)
    time.sleep(1)
LedPoint(None)