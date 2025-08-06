from peripherals import ButRead
from my_peri import LedPoint
import time

while(True):
    if ButRead(0) == True:
        LedPoint(0)
    else:
        LedPoint(None)
        