#!/usr/bin/env python
import roslib
import rospy

import nns
import convert_ir_dms as con
import asn3_data_gen as dg

from asn3_utility.utility import COMMANDS, sendCommand
from fw_wrapper.srv import *

def init_motors():
	for motor in MOTORS:
		if motor == LEFT_FRONT_E or motor == RIGHT_BACK_E:
			sendCommand(COMMANDS.SetMotorTargetPosition, receiver=motor, val=target0)
		elif motor == RIGHT_FRONT_E or motor == LEFT_BACK_E:
			sendCommand(COMMANDS.SetMotorTargetPosition, receiver=motor, val=target1)
		elif motor == LEFT_FRONT or motor == LEFT_BACK:
			sendCommand(COMMANDS.SetMotorTargetPosition, receiver=motor, val=target2)
		elif motor == RIGHT_BACK:
			sendCommand(COMMANDS.SetMotorTargetPosition, receiver=motor, val=target0)
		elif motor == RIGHT_FRONT:
			sendCommand(COMMANDS.SetMotorTargetPosition, receiver=motor, val=target1)
		elif motor == DMS:
			sendCommand(COMMANDS.SetMotorTargetPosition, receiver=motor, val=target2)


def walk_N():
	"""Make the robot move to the north"""
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=724)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=target1)
	rospy.sleep(0.5)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=724)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=target1)
	rospy.sleep(0.5)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=300)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=target0)
	rospy.sleep(0.5)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=300)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=target0)
	rospy.sleep(0.5)


def walk_S():
	"""Make the robot move to the south"""
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=250)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=target0)
	rospy.sleep(0.5)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=250)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=target0)
	rospy.sleep(0.5)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=774)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=target1)
	rospy.sleep(0.5)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=774)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=target1)
	rospy.sleep(0.5)


def walk_E(init=False):
	"""Make the robot move to the east
	:param init: Used to mark whether or not the function should set up the motors for strafing [default: False]
	"""
	if init:
		sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target1)
		sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target0)
		sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target2)
		sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target2)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=250)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=target0)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=774)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=target1)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=774)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=target1)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=250)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=target0)


def walk_W(init=False):
	"""Make the robot move to the west
	:param init: Used to mark whether or not the function should set up the motors for strafing [default: False]
	"""	
	if init:
		sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, target1)
		sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, target0)
		sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, target2)
		sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, target2)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, 774)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, target1)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, 250)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, target1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, target0)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, 250)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, target1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, target0)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, 774)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, target1)


if __name__ == '__main__':
	rospy.init_node('test_node', anonymous=True)
	rospy.loginfo('%f', sendCommand(COMMANDS.GetSensorValue, receiver=1))

	
