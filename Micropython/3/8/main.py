from my_peri import LedPoint, LedBar, ReadKeyboard
import time
from peripherals import ButRead

while(True):
    print(ReadKeyboard())
    time.sleep(0.5)