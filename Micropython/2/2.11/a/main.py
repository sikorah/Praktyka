from my_peri import LedPoint
import time

leds = [0, 1, 2, 3]

while(True):
    for i in leds:
        LedPoint(i)
        time.sleep(0.5)
    for i in reversed(leds):
        LedPoint(i)
        time.sleep(0.5)