from peripherals import LedSet, LedClr
import time
    
LedSet(1)
while (True):
    LedSet(2)
    time.sleep(0.01)
    LedClr(2)
    time.sleep(0.09)