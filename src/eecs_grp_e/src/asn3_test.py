#!/usr/bin/env python
import roslib
import rospy

import nns
import convert_ir_dms as con
import asn3_data_gen as dg

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
# GetSensorValue
# GetMotorTargetPosition
# GetMotorCurrentPosition
# SetMotorTargetPosition

def enum(**enums):
	return type('Enum', (), enums)

COMMANDS = enum(GetSensorValue='GetSensorValue', GetMotorTargetPosition='GetMotorTargetPosition', GetMotorCurrentPosition='GetMotorCurrentPosition', SetMotorTargetPosition='SetMotorTargetPosition')

def sendCommand(cmd, **kwargs):
	"""Abstracted function for calling ROS services

	   Note that the 'receiver' keyword arg is not optional (the command needs to be sent /somewhere/!)
	"""
	rospy.wait_for_service('allcmd')
	try:
		send_command = rospy.ServiceProxy('allcmd', allcmd)
		try:
			resp1 = send_command(cmd, kwargs['receiver'], kwargs['val'], 0, [0], [0])
		except KeyError:
			resp1 = send_command(cmd, kwargs['receiver'], 0, 0, [0], [0])
		return resp1.val
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e


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

	   Keyword arguments:
	   init -- if True, orient the motors to make strafing easy (default: False)
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

	   Keyword arguments:
	   init -- if True, orient the motors to make strafing easy (default: False)
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

	
