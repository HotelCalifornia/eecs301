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

# 25 cm ==> 924.22 ==> 36.9688
# 20 cm ==> 1097.389 ==> 54.86945
# 15 cm ==> 1413.833 ==> 94.2555
# 10 cm ==> 2064.759 ==> 206.4759
# 5  cm ==> 2688.91 ==> 537.782
# conv: 186.07033 = [sens] / [cm]
# conv: [cm] = [sens] / k

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

K = 186.07033

def convert_dms_cm(dms_val):
    return dms_val / K


def convert_ir_cm(ir_val):
    return ir_val / K

def avg(vals):
	r = 0
	for v in vals:
		r += v
	return r / len(vals)

if __name__ == '__main__':
	rospy.init_node('test_node', anonymous=True)

	vals = []
	if raw_input('go? ') == 'yes':
		for i in xrange(1000):
			print i
			vals.append(sendCommand(COMMANDS.GetSensorValue, receiver=1))

	print avg(vals)
