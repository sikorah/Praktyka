from peripherals import LedSet, LedClr
import time

leds = [0, 1, 2, 3]
    
def LedPoint(LedNum):
    for i in range(0, 4):
        LedClr(i)
    if LedNum != None:
        LedSet(LedNum)
    
i = 0
while(i<4):
    LedPoint(i)
    i += 1
    time.sleep(1)
LedPoint(None)