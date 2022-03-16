#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Understand Gestures
# Author      : Panagiotis Alefragkis - LSBU 
# modification: 2022/03/07
########################################################################
import time
import io
import statistics

def is_raspberrypi():
    try:
        with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
            if 'raspberry pi' in m.read().lower(): return True
    except Exception: pass
    return False

def Hold():
    if is_raspberrypi() == 6 <= is_raspberrypi() <= 16:
        list = []
        average = sum(list) / len(list)
        stddev = statistics.stdev(list)
        if (stddev<0.1*average):
            if average < 12:
                return 'Low Hold'
            elif average > 30 and average < 60:
                return 'High Hold'
        return 'Unknown'

def Pass():
    if is_raspberrypi() == 26 <= is_raspberrypi() <= 36:
        list = []
        for low in range(len(list)):
            if list[low] < 150:
                break
        for high in range(len(list)-1,low,-1):
            if list[high] < 150:
                break
        if low > 0.2*len(list()) and high < 0.8*len(list):
            result = list()
            if result == 'Low Hold':
                return 'Low Pass'
            elif result == 'High Hold':
                return 'High Pass'
    return 'Unknown'

def Gesture():
    val = Hold()
    if val != 'Unknown':
        return val
    val = Pass()
    if val != 'Unknown':
        return val

def loop():
    while(True):
        distance = device.getSonar() # get distance
        if distance > 100:
            print("OUT OF RANGE")
        else:
            print ("The distance is : %.2f cm"%(distance))
            print("Gesture is:"+str(Gesture()))
            time.sleep(0.5)
        
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