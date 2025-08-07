from my_peri import LedPoint
import time

leds = [0, 1, 2, 3, None]

while(True):
    for i in reversed(leds):
        LedPoint(i)
        time.sleep(0.5)