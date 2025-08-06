from peripherals import ButRead
from my_peri import LedPoint
import time

while(True):
    if not ButRead(1) and not ButRead(0):
        LedPoint(0)
    elif not ButRead(1) and ButRead(0):
        LedPoint(1)
    elif ButRead(1) and not ButRead(0):
        LedPoint(2)
    elif ButRead(1) and ButRead(0):
        LedPoint(3)
        
    time.sleep(0.1)
    if ButRead(3):
        LedPoint(None)
    time.sleep(0.1)
        