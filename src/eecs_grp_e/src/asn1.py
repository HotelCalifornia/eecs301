#!/usr/bin/env python
import roslib
import rospy
from fw_wrapper.srv import *
from sys import argv

# -----------SERVICE DEFINITION-----------
# allcmd REQUEST DATA
# ---------
# string command_type
# int8 device_id
# int16 target_val
# int8 n_dev
# int8[] dev_ids
# int16[] target_vals

# allcmd RESPONSE DATA
# ---------
# int16 val
# --------END SERVICE DEFINITION----------

# ----------COMMAND TYPE LIST-------------
# GetMotorTargetPosition
# GetMotorCurrentPosition
# GetIsMotorMoving
# GetSensorValue
# GetMotorWheelSpeed
# SetMotorTargetPosition
# SetMotorTargetSpeed
# SetMotorTargetPositionsSync
# SetMotorMode
# SetMotorWheelSpeed

target0 = 200
target1 = 824
target2 = 512

target0_0 = 250
target0_1 = 200
target1_0 = 512
target1_1 = 824	

MOTORS = [1,2,3,4,5,6,7,8,9]

LEFT_FRONT = MOTORS[0]
RIGHT_FRONT = MOTORS[1]
LEFT_BACK = MOTORS[2]
RIGHT_BACK = MOTORS[3]

LEFT_FRONT_E = MOTORS[4]
RIGHT_FRONT_E = MOTORS[5]
LEFT_BACK_E = MOTORS[6]
RIGHT_BACK_E = MOTORS[7]

DMS = MOTORS[8]

# wrapper function to call service to get sensor value
def getSensorValue(port):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('GetSensorValue', port, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to set a motor target position
def setMotorTargetPositionCommand(motor_id, target_val):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
	resp1 = send_command('SetMotorTargetPosition', motor_id, target_val, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to get a motor's current position
def getMotorPositionCommand(motor_id):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
	resp1 = send_command('GetMotorCurrentPosition', motor_id, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to check if a motor is currently moving
def getIsMotorMovingCommand(motor_id):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
	resp1 = send_command('GetIsMotorMoving', motor_id, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def init_motors_w():
	for motor in MOTORS:
		if motor == LEFT_FRONT_E or motor == RIGHT_BACK_E:
			setMotorTargetPositionCommand(motor, target0)
		elif motor == RIGHT_FRONT_E or motor == LEFT_BACK_E:
			setMotorTargetPositionCommand(motor, target1)
		elif motor == LEFT_FRONT or motor == LEFT_BACK:
			setMotorTargetPositionCommand(motor, target2)
		elif motor == RIGHT_BACK:
			setMotorTargetPositionCommand(motor, target0)
		elif motor == RIGHT_FRONT:
			setMotorTargetPositionCommand(motor, target1)
		else:
			setMotorTargetPositionCommand(motor, target2)
#take one step forward
def walk():
	setMotorTargetPositionCommand(RIGHT_FRONT_E, 724)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)

	setMotorTargetPositionCommand(LEFT_BACK_E, 724)
	setMotorTargetPositionCommand(LEFT_BACK, target2)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)

	setMotorTargetPositionCommand(LEFT_FRONT_E, 300)
	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)

	setMotorTargetPositionCommand(RIGHT_BACK_E, 300)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_BACK, target1)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)

#turn slightly counterclockwise
def rotate_CCW():
	setMotorTargetPositionCommand(LEFT_FRONT_E, 300)
	setMotorTargetPositionCommand(LEFT_FRONT, 356)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 724)
	setMotorTargetPositionCommand(RIGHT_FRONT, 668)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)

	setMotorTargetPositionCommand(RIGHT_BACK_E, 300)
	setMotorTargetPositionCommand(RIGHT_BACK, 356)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)

	setMotorTargetPositionCommand(LEFT_BACK_E, 724)
	setMotorTargetPositionCommand(LEFT_BACK, 668)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)

	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(LEFT_BACK, target2)

#turn slightly clockwise
def rotate_CW():
	setMotorTargetPositionCommand(LEFT_FRONT_E, 300)
	setMotorTargetPositionCommand(LEFT_FRONT, 356)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 724)
	setMotorTargetPositionCommand(RIGHT_FRONT, 668)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)

	setMotorTargetPositionCommand(RIGHT_BACK_E, 300)
	setMotorTargetPositionCommand(RIGHT_BACK, 356)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)

	setMotorTargetPositionCommand(LEFT_BACK_E, 724)
	setMotorTargetPositionCommand(LEFT_BACK, 668)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)

	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_BACK, target1)

#wrapper function for rotate_CCW() which causes the robot to turn roughly 180 degrees counterclockwise
def rotate_180_CCW():
	for i in range(0,8):
		rotate_CCW()

#wrapper function for rotate_CCW() which causes the robot to turn roughly 90 degrees counterclockwise
def rotate_90_CCW():
	for i in range(0,4):
		rotate_CCW()

#wrapper function for rotate_CW() which causes the robot to turn roughly 90 degrees clockwise
def rotate_90_CW():
	for i in range(0,4):
		rotate_CW()

#the robot follows a wall to its right, adjusting its position as needed
def wall_follow_right():
	init_motors_w()
	setMotorTargetPositionCommand(DMS, target1)
	rospy.sleep(0.1)
	r = rospy.Rate(10)
	while not rospy.is_shutdown():
		if 1200 <= getSensorValue(3) <= 1800:
			walk()
		elif getSensorValue(3) < 1200:
			rotate_90_CW()
			rospy.sleep(0.1)
			for i in range(0,4):
				walk()
			rospy.sleep(0.1)
			rotate_90_CCW()
		elif getSensorValue(3) > 1800:
			rotate_90_CCW()
			rospy.sleep(0.1)
			for i in range(0,4):
				walk()
			rospy.sleep(0.1)
			rotate_90_CW()
		r.sleep()

#the robot follows a wall to its left, adjusting its position as needed
def wall_follow_left():
	init_motors_w()
	setMotorTargetPositionCommand(DMS, target0)
	rospy.sleep(0.1)
	r = rospy.Rate(10)
	while not rospy.is_shutdown():
		if 1200 <= getSensorValue(3) <= 1800:
			walk()
		elif getSensorValue(3) < 1200:
			rotate_90_CCW
			rospy.sleep(0.1)
			for i in range(0,4):
				walk()
			rospy.sleep(0.1)
			rotate_90_CW()
		elif getSensorValue(3) > 1800:
			rotate_90_CW()
			rospy.sleep(0.1)
			for i in range(0,4):
				walk()
			rospy.sleep(0.1)
			rotate_90_CCW()
		r.sleep()

STATUS = {
	'CLEAR': True,
	'FRONT': False,
	'LEFT': False,
	'RIGHT': False
}

#check the robot's current status and act accordingly (like a state machine)
def check_status():
	if STATUS['CLEAR']:
		walk()
	elif STATUS['FRONT'] and STATUS['LEFT'] and STATUS['RIGHT']:
		rotate_180_CCW()
	elif STATUS['FRONT'] and STATUS['LEFT'] and not STATUS['RIGHT']:
		rotate_CW()
	elif STATUS['FRONT'] and not STATUS['LEFT'] and STATUS['RIGHT']:
		rotate_CCW()
	else:
		rotate_90_CCW()

#update the robot's current status based on sensor values (like a state machine)
def update_status():
	if getSensorValue(3) <= 20:
		STATUS['CLEAR'] = True
	elif getSensorValue(3) >= 800 and getSensorValue(1) >= 45 and getSensorValue(5) >= 45:
		STATUS['CLEAR'] = False
		STATUS['FRONT'] = True
		STATUS['LEFT'] = True
		STATUS['RIGHT'] = True
	elif getSensorValue(3) >= 800 and getSensorValue(1) >= 45:
		STATUS['CLEAR'] = False
		STATUS['FRONT'] = True
		STATUS['LEFT'] = True
		STATUS['RIGHT'] = False
	elif getSensorValue(3) >= 800 and getSensorValue(5) >= 45:
		STATUS['CLEAR'] = False
		STATUS['FRONT'] = True
		STATUS['LEFT'] = False
		STATUS['RIGHT'] = True

#reset the robot's status to the initial values
def reset_status():
	STATUS['CLEAR'] = True
	STATUS['FRONT'] = False
	STATUS['LEFT'] = False
	STATUS['RIGHT'] = False

#the robot moves forward, reacting to obstacles in its path
def reactive():
	init_motors_w()

	r = rospy.Rate(10)
	while not rospy.is_shutdown():
		update_status()
		for status in STATUS:
			rospy.loginfo(status + ": %i", STATUS[status])
		print '\n'
		rospy.loginfo("Front: %f", getSensorValue(3))
		rospy.loginfo("Left: %f", getSensorValue(2))
		rospy.loginfo("Right: %f", getSensorValue(5))
		check_status()
		reset_status()

		r.sleep()

def walk_loop(sec=5):
	times = sec
	curr = 0
	r = rospy.Rate(10)
	while curr < times:
		walk()
		curr += 1
		r.sleep()

# Main function
if __name__ == "__main__":
	rospy.init_node('asn0_node', anonymous=True)
	rospy.loginfo("Starting Group E Control Node...")

	if argv[1] == 'wall_follow_right':
		wall_follow_right()
	elif argv[1] == 'wall_follow_left':
		wall_follow_left()
	elif argv[1] == 'reactive':
		reactive()
	elif argv[1] == 'turn_90_left':
		rotate_90_CCW()
	elif argv[1] == 'turn_90_right':
		rotate_90_CW()
	elif argv[1] == 'turn_180':
		rotate_180_CCW()
	elif argv[1] == 'walk':
		while not rospy.is_shutdown():
			walk_loop(int(argv[2]))
	else:
		print 'unknown argument\n'



