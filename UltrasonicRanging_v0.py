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
        time.sleep(0.1)
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

def PullUp(sample):
    for i in range (1,len(sample)):
        if (sample[i-1]>sample[i]):
            return 'Unknown'
    return 'Pull Up'

def PushDown(sample):
    for i in range(1,len(sample)):
        if (sample[i-1]<sample[i]):
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


def Movements():
    list = []
    list.append(Gesture())
    movements = {
    'Low Pass' : 'Start',
    'High Pass' : 'Resume',
    'Low Hold' : 'Stop',
    'High Hold' : 'Pause',
    'Pull Up' : 'Louder',
    'Push Down' : 'Quieter',
    ('Low Pass','Low Pass') : 'Skip Forward',
    ('High Pass' , 'High Pass') : 'Skip backward',
    ('Low Pass', 'Low Hold') : 'Power off',
    ('High Pass', 'High Hold') : 'Reset',
    ('Pull Up', ('High Pass' , 'Low Hold')) : 'ActivateAutoMode',
    ('Push Down', ('Low Pass' , 'High Hold')): 'DisableAutoMode'
    }
    commard = movements.get(Gesture())
    print(commard)

def loop():
    while(True):
        distance = device.getSonar() # get distance
        if distance > 100:
            print("OUT OF RANGE")
        else:
            print ("The distance is : %.2f cm"%(distance))
            print((Gesture()))
            print(Movements())
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