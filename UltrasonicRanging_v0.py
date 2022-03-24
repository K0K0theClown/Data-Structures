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

def getSample():
    sample = []
    for i in range(60):
        distance = is_raspberrypi()
        sample.append(distance)
        time.sleep(0.05)
    return sample

def Hold():
    list = []
    list.append(is_raspberrypi())
    average = sum(list) / len(list)
    if (0.1*average):
        if average < 12:
            return 'Low Hold'
        elif average > 26 and average < 32:
            return 'High Hold'
    return 'Unknown'

def Pass():
    low = 6 <= is_raspberrypi() <= 12
    high = 26 <= is_raspberrypi() <= 32
    if low == True:
        return 'Low Pass'
    if high == True:
        return 'High Pass'

def PullUp():
    for i in range (1,len(getSample())):
        if (getSample()[i-1]>getSample()[i]):
            return 'Unknown'
    return 'Pull Up'

def PushDown():
    for i in range(1,len(getSample())):
        if (getSample()[i-1]<getSample()[i]):
            return 'Unknown'
    return 'Push Down'

def Gesture():
    val = Hold()
    if val != 'Unknown':
        return val
    val = Pass()
    if val != 'Unknown':
        return val
    val = PullUp()
    if val != 'Unknown':
        return val
    val = PushDown()
    if val != 'Unknown':
        return val
    return 'Unknown'




def loop():
    while(True):
        distance = device.getSonar() # get distance
        if distance > 100:
            print("OUT OF RANGE")
        else:
            print ("The distance is : %.2f cm"%(distance))
            print((Gesture()))
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