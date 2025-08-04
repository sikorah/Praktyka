from peripherals import LedSet, LedClr
import time
    
Counter = 0
while (Counter < 3):
    Counter = Counter + 1
    LedSet(2)
    time.sleep(1)
    LedClr(2)
    time.sleep(1)
    
    
    