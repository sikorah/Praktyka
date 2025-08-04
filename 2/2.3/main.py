from peripherals import LedSet, LedClr
import time
    
leds = [0, 1, 2, 3]

while(True):
    
    for led in leds:
        LedSet(led)           
        time.sleep(1)    

    for led in reversed(leds):
        LedClr(led)
        time.sleep(1)
    
    
    