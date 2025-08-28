from peripherals import PotRead
import time

while(True):
    pot = PotRead()
    pot = (pot - 480) / (65535 - 480)
    pot = pot * 3.3
    print(pot)
    time.sleep(0.5)