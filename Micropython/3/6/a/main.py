from peripherals import ButRead
from my_peri import LedPoint, LedBar
import time

while(True):
    i = ButRead(0)+ButRead(1)+ButRead(2)+ButRead(3)
    LedBar(i)