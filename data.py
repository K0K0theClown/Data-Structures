import random
import time
import threading



def pulseIn(pin,level,timeOut):
	t0 = time.time()
	while(GPIO.input(pin) != level):
		if((time.time() - t0) > timeOut*0.000001):
			return 0;
	t0 = time.time()
	while(GPIO.input(pin) == level):
		if((time.time() - t0) > timeOut*0.000001):
			return 0;
	pulseTime = (time.time() - t0)*1000000
	return pulseTime

class Waiter():

    def __init__(self):#, init_value):
    	init_value = {}
    	self.var = init_value
    	self.var_mutex = threading.Lock()
    	self.var_event = threading.Event()

    def WaitUntil(self, v):
        while True:
            self.var_mutex.acquire()
            if self.var == v:
                self.var_mutex.release()
                return # Done waiting
            self.var_mutex.release()
            self.var_event.wait(1) # Wait 1 sec

    def Set(self, v):
        self.var_mutex.acquire()
        self.var = v
        self.var_mutex.release()
        self.var_event.set() # In case someone is waiting
        self.var_event.clear()

def lowHold():
	lowHold = 6 <= distance <= 12
	return lowHold

while True:
	distance = random.randrange(0,20)
	print(distance)
	time.sleep(0.5)
	x = Waiter()
	if lowHold() == True:
		if x == True:
			print("Low Hold")