from peripherals import LedSet, LedClr
import time
    

while (True):
    LedSet(1)
    LedSet(2)
    time.sleep(0.01)
    LedClr(2)
    time.sleep(0.09)
    
    
    