from my_peri import LedPoint, LedBar
import time

while(True):
    for i in [0, 1, 2, 3, 4]:
        LedBar(i)
        time.sleep(1)