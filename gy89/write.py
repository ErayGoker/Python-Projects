import read
import time
import math

read.wake()

try:
    while True:
        print(read.getHeading())
        time.sleep(10)
except KeyboardInterrupt:
    print("hata")