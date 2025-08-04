from peripherals import LedSet, LedClr
from my_peri import LedPoint
import time


iterations = [0, 1, 2, 3, 4]

for i in iterations:
    LedPoint(i) # 4 poza zakresem, ale gaśnie
    time.sleep(1)