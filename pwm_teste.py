
#import needed libs
import math
import time
import board
import busio
import adafruit_pca9685

#setup i2c object
i2c = busio.I2C(board.SCL, board.SDA)

#setup pca9685 board communication object
pca = adafruit_pca9685.PCA9685(i2c)

#set global pwm frequency to 50Hz (measured 49.96Hz)
pca.frequency = 50.5

#16 bit value that dictates how much of one cycle is high (1) versus low (0).
#0xffff will always be high, 0 will always be low and 0x7fff will be half high and then half low.

#there are 65536 different possibilities of duty-cycle precision
#then, for 50Hz, each unit of duty cycle corresponds to approx 0.305176us

#if the servo has operating range from 500us to 2500us, then d.c. varies linearly from 1639 to 8192.

#proposing a formula: duty = (angle/270)*(8192-1639)+1639
#135 degrees corresponds to 4916 or 0x1334

#450-2520

for i in range(0,len(pca.channels)):
	pca.channels[i].duty_cycle=0x1334


"""for i in range(1,270):
	pca.channels[13].duty_cycle=math.floor((i/270)*(8192-1639)+1639)
	print(i)
	time.sleep(0.05)
"""

#pca.channels[13].duty_cycle=round(((135+86)/270)*(8192-1639)+1639)

#sweep range

j=135
for i in range(0,3000,10):
	try:
		j=float(input("angle: "))
	except:
		print("Not a float.")
	j=round(((j)/270)*(8192-1639)+1639)
	pca.channels[13].duty_cycle=round(j)

