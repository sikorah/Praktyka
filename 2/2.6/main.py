from peripherals import LedSet, LedClr
import time
    

while (True):
    LedSet(1)
    LedSet(2)
    time.sleep(0.002)
    LedClr(2)
    time.sleep(0.0018)
    
    
    