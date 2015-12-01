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
	"""Intialise the motors"""
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

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=300)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=target0)
	rospy.sleep(0.5)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=300)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=target0)
	rospy.sleep(0.5)


def walk_E():
	"""Make the robot move to the east"""
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


def walk_W():
	"""Make the robot move to the west"""
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=774)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT_E, val=target1)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=250)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT_E, val=target0)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=250)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_FRONT, val=target1)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=RIGHT_BACK_E, val=target0)

	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=774)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK, val=target2)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_FRONT, val=target0)
	sendCommand(COMMANDS.SetMotorTargetPosition, receiver=LEFT_BACK_E, val=target1)


def get_pos():
	"""Get the robot's current position"""
	try:
		x = con.convert_ir_cm(sendCommand(COMMANDS.GetSensorValue, receiver=IR_X))
	except ZeroDivisionError:
		x = 40
	try:
		y = con.convert_ir_cm(sendCommand(COMMANDS.GetSensorValue, receiver=IR_Y))
	except ZeroDivisionError:
		y = 40

	return x, y


def near_centre(pos):
	"""Is the given position near (within 2cm of) the centre?"""
	return 28 <= pos[0] + 4.5 <= 30 and 28 <= pos[1] + 3.25 <= 30


def correct(vec):
	"""Given a vector, move in the direction of the vector"""
	r0 = rospy.Rate(1)
	if vec[0] < 0:
		for i in xrange(abs(vec[0] // 6)):
			walk_W()
			r0.sleep()
	elif vec[0] > 0:
		for i in xrange(abs(vec[0] // 6)):
			walk_E()
			r0.sleep()
	if vec[1] < 0:
		for i in xrange(abs(vec[1] // 6)):
			walk_N()
			r0.sleep()
	elif vec[1] > 0:
		for i in xrange(abs(vec[1] // 6)):
			walk_S()
			r0.sleep()


def main():
	"""Main function"""
	init_motors()

	r = rospy.Rate(1)
	
	# generates data in the root of the node
	dg.generate_data(60)
	data = nns.read_data()

	while not rospy.is_shutdown():
		# find relative position
		pos = get_pos()
		print 'position: (%f, %f)' % (pos[0], pos[1])
		# exit if relative position is within reasonable margin from centre
		if near_centre(pos):
			break
		else:
			# get nearest neighbours
			neighbours = nns.nns(pos, data)
			# find direction and magnitude of correction
			vec = nns.analyse(data, neighbours)
			# act on correction
			correct(vec)
		r.sleep()


if __name__ == '__main__':
	rospy.init_node('test_node', anonymous=True)
	main()

