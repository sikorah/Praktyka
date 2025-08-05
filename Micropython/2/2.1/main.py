from peripherals import LedSet, LedClr
import time

# Wlasna funkcja - mozna rowniez uzyc gotowej funkcji sleep_ms 

def delay(nanoseconds):
    i = 0
    for i in range(0, nanoseconds/10):
        if i == nanoseconds - 1:
            break
        else:
            i = i + 1
            
while(True):
    LedSet(1)
    #delay(1000000)
    time.sleep_ms(1000)
    LedClr(1)
    #delay(1000000)
    time.sleep_ms(1000)
    
    