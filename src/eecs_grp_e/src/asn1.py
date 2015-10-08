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

MOTORS = [1,2,3,4,5,6,7,8]

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
		if motor == 5 or motor == 8:
			setMotorTargetPositionCommand(motor, target0)
		elif motor == 6 or motor == 7:
			setMotorTargetPositionCommand(motor, target1)
		elif motor == 1 or motor == 4:
			setMotorTargetPositionCommand(motor, target0)
		elif motor == 2 or motor == 3:
			setMotorTargetPositionCommand(motor, target2)

def init_motors_w():
	target0 = 200
	target1 = 824
	target2 = 512
	for motor in MOTORS:
		if motor == 5 or motor == 8:
			setMotorTargetPositionCommand(motor, target0)
		elif motor == 6 or motor == 7:
			setMotorTargetPositionCommand(motor, target1)
		elif motor == 1 or motor == 4:
			setMotorTargetPositionCommand(motor, target2)
		elif motor == 2 or motor == 3:
			setMotorTargetPositionCommand(motor, target1)	

def rotate_CCW():
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
	for i in range(0,4):
		rotate_CCW()

def rotate_90_CCW():
	for i in range(0,2):
		rotate_CCW()

def rotate_CW():
	setMotorTargetPositionCommand(MOTORS[3], target1_0)	
	setMotorTargetPositionCommand(MOTORS[2], target1_1)
	setMotorTargetPositionCommand(MOTORS[0], target1_0)
	setMotorTargetPositionCommand(MOTORS[1], target1_1)
	
	setMotorTargetPositionCommand(MOTORS[4], target0_0)
	rospy.sleep(0.05)
	setMotorTargetPositionCommand(MOTORS[0], target0_f)
	setMotorTargetPositionCommand(MOTORS[4], target0_1)

	setMotorTargetPositionCommand(MOTORS[5], target1_0)
	rospy.sleep(0.05)
	setMotorTargetPositionCommand(MOTORS[1], target1_f)
	setMotorTargetPositionCommand(MOTORS[5], target1_1)

	setMotorTargetPositionCommand(MOTORS[7], target1_0)
	rospy.sleep(0.05)
	setMotorTargetPositionCommand(MOTORS[3], target0_f)
	setMotorTargetPositionCommand(MOTORS[7], target0_1)

	setMotorTargetPositionCommand(MOTORS[6], target1_0)
	rospy.sleep(0.05)
	setMotorTargetPositionCommand(MOTORS[2], target1_f)
	setMotorTargetPositionCommand(MOTORS[6], target1_1)
	rospy.sleep(0.05)

def rotate_90_CW():
	for i in range(0,3):
		rotate_CW()

def walk():
	setMotorTargetPositionCommand(MOTORS[4], 275)
	setMotorTargetPositionCommand(MOTORS[6], 749)

	setMotorTargetPositionCommand(MOTORS[5], 749)	
	setMotorTargetPositionCommand(MOTORS[7], 125)

	setMotorTargetPositionCommand(MOTORS[4], 200)
	setMotorTargetPositionCommand(MOTORS[6], 824)

	setMotorTargetPositionCommand(MOTORS[5], 824)
	setMotorTargetPositionCommand(MOTORS[7], 200)


# Main function
if __name__ == "__main__":
	rospy.init_node('asn0_node', anonymous=True)
	rospy.loginfo("Starting Group E Control Node...")

	# set initial motor position
	init_motors_w()
	# control loop running at 10hz
	r = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		walk()

		r.sleep()


