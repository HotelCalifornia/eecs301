#!/usr/bin/env python
import roslib
import rospy
from fw_wrapper.srv import *

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
# sets up motors for rotation
def init_motors_r():
	target0 = 200
	target1 = 824
	target2 = 512
	for motor in MOTORS:
		if motor == LEFT_FRONT_E or motor == RIGHT_BACK_E:
			setMotorTargetPositionCommand(motor, target0)
		elif motor == RIGHT_FRONT_E or motor == LEFT_BACK_E:
			setMotorTargetPositionCommand(motor, target1)
		elif motor == LEFT_FRONT or motor == RIGHT_BACK:
			setMotorTargetPositionCommand(motor, target0)
		elif motor == RIGHT_FRONT or motor == LEFT_BACK:
			setMotorTargetPositionCommand(motor, target2)

def init_motors_w():
	target0 = 200
	target1 = 824
	target2 = 512
	for motor in MOTORS:
		if motor == LEFT_FRONT_E or motor == RIGHT_BACK_E:
			setMotorTargetPositionCommand(motor, target0)
		elif motor == RIGHT_FRONT_E or motor == LEFT_BACK_E:
			setMotorTargetPositionCommand(motor, target1)
		elif motor == RIGHT_FRONT or motor == RIGHT_BACK:
			setMotorTargetPositionCommand(motor, target2)
		elif motor == LEFT_FRONT:
			setMotorTargetPositionCommand(motor, target0)
		elif motor == LEFT_BACK:
			setMotorTargetPositionCommand(motor, target1)
		else:
			setMotorTargetPositionCommand(motor, target2)

def walk():
	setMotorTargetPositionCommand(RIGHT_FRONT_E, 749)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)

	setMotorTargetPositionCommand(LEFT_BACK_E, 749)
	setMotorTargetPositionCommand(LEFT_BACK, target2)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)

	setMotorTargetPositionCommand(LEFT_FRONT_E, 125)
	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)

	setMotorTargetPositionCommand(RIGHT_BACK_E, 125)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_BACK, target1)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)

	# setMotorTargetPositionCommand(MOTORS[4], 125)
	# setMotorTargetPositionCommand(MOTORS[6], 749)

	# setMotorTargetPositionCommand(MOTORS[5], 749)	
	# setMotorTargetPositionCommand(MOTORS[7], 125)

	# setMotorTargetPositionCommand(MOTORS[4], 200)
	# setMotorTargetPositionCommand(MOTORS[6], 824)

	# setMotorTargetPositionCommand(MOTORS[5], 824)
	# setMotorTargetPositionCommand(MOTORS[7], 200)

def rotate_CW():
	setMotorTargetPositionCommand(MOTORS[5], target1_0)
	setMotorTargetPositionCommand(MOTORS[1], target1_1)
	rospy.sleep(0.05)
	setMotorTargetPositionCommand(MOTORS[5], target1_1)

	setMotorTargetPositionCommand(MOTORS[4], target0_0)
	setMotorTargetPositionCommand(MOTORS[0], target1_0)
	rospy.sleep(0.05)
	setMotorTargetPositionCommand(MOTORS[4], target0_1)

	setMotorTargetPositionCommand(MOTORS[6], target1_0)
	setMotorTargetPositionCommand(MOTORS[2], target1_1)
	rospy.sleep(0.05)
	setMotorTargetPositionCommand(MOTORS[6], target1_1)
		
	setMotorTargetPositionCommand(MOTORS[7], target1_0)
	setMotorTargetPositionCommand(MOTORS[3], target1_0)
	rospy.sleep(0.05)
	setMotorTargetPositionCommand(MOTORS[7], target0_1)

	setMotorTargetPositionCommand(MOTORS[1], target1_f)
	setMotorTargetPositionCommand(MOTORS[0], target0_f)
	setMotorTargetPositionCommand(MOTORS[2], target1_f)
	setMotorTargetPositionCommand(MOTORS[3], target0_f)

def rotate_180_CCW():
	for i in range(0,8):
		rotate_CCW()

def rotate_90_CCW():
	init_motors_r()
	for i in range(0,4):
		rotate_CCW()

def rotate_CCW():
	setMotorTargetPositionCommand(LEFT_FRONT_E, 275)
	setMotorTargetPositionCommand(LEFT_FRONT, 356)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 749)
	setMotorTargetPositionCommand(RIGHT_FRONT, 668)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)

	setMotorTargetPositionCommand(RIGHT_BACK_E, 275)
	setMotorTargetPositionCommand(RIGHT_BACK, 356)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)

	setMotorTargetPositionCommand(LEFT_BACK_E, 749)
	setMotorTargetPositionCommand(LEFT_BACK, 668)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)

	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(LEFT_BACK, target2)

def rotate_90_CW():
	for i in range(0,3):
		rotate_CW()

def wall_follow_right():
	init_motors_w()
	#turn DMS to the right
	setMotorTargetPositionCommand(DMS, target1)
	rospy.sleep(0.1)
	r = rospy.Rate(10)
	sensor_test()
	while not rospy.is_shutdown():
		sensor_test()
		if 1200 <= getSensorValue(3) <= 1600:
			walk()
		elif getSensorValue(3) < 1200:
			rotate_CCW()
		elif getSensorValue(3) > 1600:
			# TODO: reimplement rotate_CW() with the new algorithm so we can turn right
			rotate_CCW()
		r.sleep()
	sensor_test()

def sensor_test():
	rospy.loginfo("%f", getSensorValue(3))

# Main function
if __name__ == "__main__":
	rospy.init_node('asn0_node', anonymous=True)
	rospy.loginfo("Starting Group E Control Node...")
	



