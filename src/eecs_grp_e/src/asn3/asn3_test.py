#!/usr/bin/env python
import roslib
import rospy

import nns
import convert_ir_dms as con
import asn3_data_gen as dg

from asn3_utility.utility import sendCommand
from asn3_utility.globals import *

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

def rotate():
	target0_f = 200
	target1_f = 512
	
	target0_0 = 250
	target0_1 = 200
	target1_0 = 512
	target1_1 = 824 

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=target1_0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target1_1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=target1_1)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=target0_0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target1_0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=target0_1)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=target1_0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target1_1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=target1_1)
		
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=target1_0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target1_0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=target0_1)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target1_f)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target0_f)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target1_f)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target0_f)

def rotate_CCW():
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=300)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=356)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=target0)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=724)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=668)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=target1)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=300)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=356)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=target0)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=724)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=668)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=target1)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target2)


if __name__ == '__main__':
	rospy.init_node('test_node', anonymous=True)
	init_motors()
	while not rospy.is_shutdown():
		if raw_input('? ') == '!':
			rotate()


# if the robot has strayed from its path:
# let phi represent the change in angle with respect to the horizontal (when viewed from above)
# let theta represent the change in angle with respect to the vertical (when viewed from above)
# let S be the length of each section of wall
# let x_0 and x_1 be the distance to the wall from the left and right sides of the robot:
# -----------
# |         |
# |<-->X<-->|
# |x_0   x_1|
# |         |
# phi = arccos(S / (x_0 + x_1)) [* (180 / pi)]
# theta = 90 - phi
# now turn by an amount that makes theta --> 0


