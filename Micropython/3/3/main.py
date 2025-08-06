from peripherals import ButRead
from my_peri import LedPoint
import time

while(True):
    if ButRead(0) & ButRead(3):
        LedPoint(0)
    elif ButRead(1) & ButRead(2):
        LedPoint(1)
    else:
        LedPoint(None)
        