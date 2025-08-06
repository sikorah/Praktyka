from peripherals import ButRead
from my_peri import LedPoint, LedBar
import time

while(True):
    j = 0
    for i in range(4):
        j = j + ButRead(i)
        LedBar(j)