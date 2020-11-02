from adafruit_servokit import ServoKit
import time
import csv

#traj = [[0,0,0,0,0,0],[0,0,-0,-0,0,0],[1,0,-0,-1,1,1],[2,1,-1,-2,2,2],[3,2,-2,-4,3,4],[6,3,-3,-7,6,7],[9,5,-5,-11,9,10],[13,7,-8,-16,14,15],[18,9,-10,-21,18,20],[23,11,-13,-27,23,25],[28,14,-16,-32,28,31],[33,16,-19,-38,33,36],[38,19,-21,-43,38,41],[42,21,-24,-48,42,46],[45,22,-26,-52,45,50],[48,24,-27,-55,48,53],[49,25,-28,-57,49,55],[51,25,-29,-59,51,56],[51,25,-29,-59,51,56],[51,25,-29,-59,51,56]]
traj = []
kit = ServoKit(channels=16) #16 channel pca9685


#Read Trajectory
def read_traj_csv():
	with open("traj.csv", newline='') as tfile:
		spamreader = csv.reader(tfile,delimiter=',')
		for row in spamreader:
			traj.append([int(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5])])
	print(traj)
#Default angles:
def default_angles():
	kit.servo[0].angle = 90+30 #right motor
	kit.servo[1].angle = 90-30 #left motor (disabled for now)

	kit.servo[4].angle = 90+5 #base
	kit.servo[5].angle = 90-10 #axis 3

	kit.servo[8].angle = 90-2 #axis 4
	kit.servo[9].angle = 90-36 #axis 5

	kit.servo[12].angle = 25 #jaw
	kit.servo[13].angle = 90-2 #axis 6

def tilt(ang):
	kit.servo[13].angle=kit.servo[13].angle+ang

def yaw(ang):
	kit.servo[4].angle=kit.servo[4].angle+ang

def grip(state):
	if state:
		kit.servo[12].angle=25
	else:
		kit.servo[12].angle=50

def set_q(q):
	kit.servo[0].angle = 90+30+q[1] #right motor
	kit.servo[1].angle = 90-30-q[1] #left motor
	kit.servo[4].angle = 90+5+q[0] #base
	kit.servo[5].angle = 90-10+q[2] #axis 3
	kit.servo[8].angle = 90-2+q[3] #axis 4
	kit.servo[9].angle = 90-36+q[4] #axis 5
	kit.servo[13].angle = 90-2+q[5] #axis 6


while True:
	entry=input("command: ")
	if entry=="default":
		default_angles()
		print(traj[0])
	elif entry=="set":
		for q in traj:
			set_q(q)
			time.sleep(0.01)
		traj.reverse()
	elif entry=="read":
		read_traj_csv()
	elif entry=="g":
		grip(0)
	elif entry=="h":
		grip(1)

