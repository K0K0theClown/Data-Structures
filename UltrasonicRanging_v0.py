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
    list = []
    list.append(is_raspberrypi())
    average = sum(list) / len(list)
    if (0.1*average):
        if average < 12:
            print("Low Hold")
        elif average > 26 and average < 32:
            print("High Hold")
    return 'Unknown'

def Pass():
    list = []
    list.append(is_raspberrypi())
    for low in range(len(list)):
        if list[low] < 150:
            break
    for high in range(len(list)-1,low,-1):
        if list[high] < 150:
            break
    if low > 0.2*len(list) and high < 0.8*len(list):
        result = list()
        if result == 'Low Hold':
            print("Low Pass")
        elif result == 'High Hold':
            print("High Pass")
    return 'Unknown'

def PullUp():
    list = []
    list.append(is_raspberrypi())
    for i in range (1,len(list)):
        if (list[i-1]>list[i]):
            return 'Unknown'
    return 'Pull Up'

def PushDown():
    list = []
    list.append(is_raspberrypi())
    for i in range(1,len(list)):
        if (list[i-1]<list[i]):
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

#def Movements():


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