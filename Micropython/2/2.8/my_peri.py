from peripherals import LedSet, LedClr

def LedPoint(LedNum):
    for i in range(0, 4):
        LedClr(i)
    if LedNum != None:
        LedSet(LedNum)