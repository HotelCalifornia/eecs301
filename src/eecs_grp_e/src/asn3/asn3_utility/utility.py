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
# GetSensorValue

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