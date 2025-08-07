from my_peri import LedPoint
from peripherals import LedSet, LedClr
import time

def LedDimm(pwm, time_s):
    frq = 0.02
    on = (pwm/100) * frq
    off = frq - on
    
    for i in range(50*time_s):
        LedSet(0)
        time.sleep(on)
        LedClr(0)
        time.sleep(off)

while(True):
    for pwm in 5, 10, 15, 20, 15, 10:
        LedDimm(pwm, 0.5)
