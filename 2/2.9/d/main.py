from peripherals import LedSet, LedClr
from my_peri import LedPoint
import time

for i in [0, 1, 2, 3, None]:
    LedPoint(i) 
    time.sleep(1)