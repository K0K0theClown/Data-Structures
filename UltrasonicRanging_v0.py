#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Understand Gestures
# Author      : Panagiotis Alefragkis - LSBU 
# modification: 2022/03/07
########################################################################
import time
import io

def is_raspberrypi():
    try:
        with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
            if 'raspberry pi' in m.read().lower(): return True
    except Exception: pass
    return False


def loop():
    while(True):
        distance = device.getSonar() # get distance
        print ("The distance is : %.2f cm"%(distance))
        time.sleep(0.1)
        
if __name__ == '__main__':     # Program entrance
    if is_raspberrypi():
        import UltrasonicDriver as device
    else:
        import UltrasonicSimulator as device
    print ('Program is starting...')
    device.setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        device.cleanup()
        print ('Bye...')
