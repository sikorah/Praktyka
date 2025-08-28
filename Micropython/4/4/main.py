from peripherals import PotRead
from my_peri import LedPoint
import time

while(True):
    pot = PotRead()
    pot = (pot - 480) / (65535 - 480)
    pot = pot * 3
    led = 3 - int(pot)
    LedPoint(led)
    