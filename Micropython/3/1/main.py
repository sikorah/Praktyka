from peripherals import ButRead
import time

while(True):
    print(ButRead(0), ButRead(1), ButRead(2), ButRead(3))
    time.sleep(0.2)