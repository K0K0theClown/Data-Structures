import random
import time
import statistics



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


def Sonar():
	return random.randrange(1,200)

print(Sonar())

def Low():
	return 6 <= Sonar() <= 12

def High():
	return 28 <= Sonar() <= 32

def Hold():
	high = High()
	low = Low()
	average = sum(Sonar()) / high
	stddev = statistics.stdev(High())
	if (stddev<0.1*average):
		if average < 12:
			return 'Low Hold'
		elif average > 30 and average < 60:
			return 'High Hold'
	return 'Unknown'
	time.sleep(1)

def Pass():
	for low in range(len(Low())):
		if Low()[low] < 150:
			break
	for high in range(len(High())-1,low,-1):
		if High()[high] < 150:
			break
	if low > 0.2*len(Low()) and high < 0.8*len(High()):
		result = Hold()
		if result == 'Low Hold':
			return 'Low Pass'
		elif result == 'High Hold':
			return 'High Pass'
	return 'Unknown'
	time.sleep(0.5)

def Gesture():
	val = Hold()
	if val != 'Unknown':
		return val
	val = Pass()
	if val != 'Unknown':
		return val


#def loop():
	#while True:
		#distance = Sonar()
		#print("distance:"+str(Sonar()))
		#print("Hold:"+str(Gesture()))
		#time.sleep(0.1)

#if __name__ == '__main__':
	#print('Program is Starting...')

	#try:
		#loop()
	#except KeyboardInterrupt:
		#exit()

