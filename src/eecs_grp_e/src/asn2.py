#!/usr/bin/env python
import roslib
import rospy
from fw_wrapper.srv import *
from map import *

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

RATE = 1

class Position(object):
	"""docstring for Position"""
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def incr_x(self):
		self.x += 1

	def incr_y(self):
		self.y += 1

	def decr_x(self):
		self.x -= 1

	def decr_y(self):
		self.y -= 1

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

 # wrapper function to call service to set motor target speed
def setMotorTargetSpeed(motor_id, target_val):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('SetMotorTargetSpeed', motor_id, target_val, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def init_motors():
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

def walk_N():
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

def walk_S():
	setMotorTargetPositionCommand(RIGHT_BACK_E, 300)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(LEFT_BACK, target2)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)

	setMotorTargetPositionCommand(LEFT_FRONT_E, 300)
	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)

	setMotorTargetPositionCommand(LEFT_BACK_E, 724)
	setMotorTargetPositionCommand(LEFT_BACK, target1)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 724)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)

def walk_E(init=False):
	if init:
		setMotorTargetPositionCommand(RIGHT_FRONT, target1)
		setMotorTargetPositionCommand(LEFT_FRONT, target0)
		setMotorTargetPositionCommand(RIGHT_BACK, target2)
		setMotorTargetPositionCommand(LEFT_BACK, target2)

	setMotorTargetPositionCommand(RIGHT_BACK_E, 300)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)

	setMotorTargetPositionCommand(LEFT_BACK_E, 724)
	setMotorTargetPositionCommand(LEFT_BACK, target1)
	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 724)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)

	setMotorTargetPositionCommand(LEFT_FRONT_E, 300)
	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(LEFT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)

def walk_W(init=False):
	if init:
		setMotorTargetPositionCommand(RIGHT_FRONT, target1)
		setMotorTargetPositionCommand(LEFT_FRONT, target0)
		setMotorTargetPositionCommand(RIGHT_BACK, target2)
		setMotorTargetPositionCommand(LEFT_BACK, target2)

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 724)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)

	setMotorTargetPositionCommand(LEFT_FRONT_E, 300)
	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(LEFT_BACK, target1)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)

	setMotorTargetPositionCommand(RIGHT_BACK_E, 300)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)

	setMotorTargetPositionCommand(LEFT_BACK_E, 724)
	setMotorTargetPositionCommand(LEFT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)

def walk(dir=DIRECTION.North):
	if dir == DIRECTION.East:
		walk_E()
	elif dir == DIRECTION.South:
		walk_S()
	elif dir == DIRECTION.West:
		walk_W()
	else:
		walk_N()

def move_N(pos):
	for motor in MOTORS:
		setMotorTargetSpeed(motor, 400)
	r = rospy.Rate(RATE)
	for i in range(5):
		walk(DIRECTION.North)
		r.sleep()
	pos.incr_y()

def move_S(pos):
	for motor in MOTORS:
		setMotorTargetSpeed(motor, 400)
	r = rospy.Rate(RATE)
	for i in range(5):
		walk(DIRECTION.South)
		r.sleep()
	pos.decr_y()

def move_E(pos):
	for motor in MOTORS:
		setMotorTargetSpeed(motor, 362)
	r = rospy.Rate(RATE)
	for i in range(4):
		walk(DIRECTION.East)
		r.sleep()
	pos.incr_x()

def move_W(pos):
	for motor in MOTORS:
		setMotorTargetSpeed(motor, 375)
	r = rospy.Rate(RATE)
	for i in range(5):
		walk(DIRECTION.West)
		r.sleep()
	pos.decr_x()


if __name__ == "__main__":
	rospy.init_node('asn0_node', anonymous=True)
	rospy.loginfo("Starting Group E Control Node...")
	pos = Position()

	move_N(pos)
	move_W(pos)
	move_S(pos)
	move_E(pos)
	

	