from peripherals import LedSet, LedClr
import time
    
LedSet(1)
while (True):
    LedSet(2)
    time.sleep(0.002)
    LedClr(2)
    time.sleep(0.0018)
    
    
    