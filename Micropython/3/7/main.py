from my_peri import LedPoint, LedBar, ReadKeyboard
import time
from peripherals import ButRead

    
def ReadKeyboard():
    if ButRead(0):
        return 0
    elif ButRead(1):
        return 1
    elif ButRead(2):
        return 2
    elif ButRead(3):
        return 3
    else:
        return None
    
while(True):
    print(ReadKeyboard())
    time.sleep(0.2)