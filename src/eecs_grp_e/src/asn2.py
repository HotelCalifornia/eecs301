#!/usr/bin/env python
import roslib
import rospy
import Queue
from fw_wrapper.srv import *
from map import *
from math import *

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

INITIAL_H_X = 0
INITIAL_H_Y = 0

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

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __ne__(self, other):
		return not self.__eq__(other)

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

def walk_N():
	"""Make the robot move to the north"""

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 624)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(LEFT_BACK_E, 624)
	setMotorTargetPositionCommand(LEFT_BACK, target2)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(LEFT_FRONT_E, 400)
	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(RIGHT_BACK_E, 400)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_BACK, target1)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)
	rospy.sleep(0.5)

	rospy.loginfo('gyro x: %f' % getSensorValue(4))
	rospy.loginfo('gryo y: %f' % getSensorValue(3))

def walk_S():
	"""Make the robot move to the south"""
	setMotorTargetPositionCommand(RIGHT_BACK_E, 300)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(LEFT_BACK, target2)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(LEFT_FRONT_E, 300)
	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(LEFT_BACK_E, 724)
	setMotorTargetPositionCommand(LEFT_BACK, target1)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 724)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)
	rospy.sleep(0.5)

	rospy.loginfo('gyro x: %f' % getSensorValue(4))
	rospy.loginfo('gryo y: %f' % getSensorValue(3))

def walk_E(init=False):
	"""Make the robot move to the east

	   Keyword arguments:
	   init -- if True, orient the motors to make strafing easy (default: False)
	"""
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

	# rospy.loginfo('gyro x: %f' % getSensorValue(4))
	# rospy.loginfo('gryo y: %f' % getSensorValue(3))

def walk_W(init=False):
	"""Make the robot move to the west

	   Keyword arguments:
	   init -- if True, orient the motors to make strafing easy (default: False)
	"""	
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

	rospy.loginfo('gyro x: %f' % getSensorValue(4))
	rospy.loginfo('gryo y: %f' % getSensorValue(3))

def walk(dir=DIRECTION.North):
	"""Make the robot walk in the direction specified

	   Keyword arguments:
	   dir -- the desired direction (default: DIRECTION.North)
	"""
	if dir == DIRECTION.East:
		walk_E()
		rospy.sleep(0.25)
	elif dir == DIRECTION.South:
		walk_S()
		rospy.sleep(0.25)
	elif dir == DIRECTION.West:
		walk_W()
		rospy.sleep(0.25)
	else:
		walk_N()


def move_N(pos):
	"""Wrapper function to make the robot move one cell north

	   Keyword arguments:
	   pos -- the robot's current Position
	"""
	for motor in MOTORS:
		setMotorTargetSpeed(motor, 400)
	r = rospy.Rate(RATE)
	for i in range(5):
		walk(DIRECTION.North)
		r.sleep()
	pos.incr_y()

def move_S(pos):
	"""Wrapper function to make the robot move one cell south

	   Keyword arguments:
	   pos -- the robot's current Position
	"""
	for motor in MOTORS:
		setMotorTargetSpeed(motor, 400)
	r = rospy.Rate(RATE)
	for i in range(5):
		walk(DIRECTION.South)
		r.sleep()
	pos.decr_y()

def move_E(pos):
	"""Wrapper function to make the robot move one cell east

	   Keyword arguments:
	   pos -- the robot's current Position
	"""
	for motor in MOTORS:
		setMotorTargetSpeed(motor, 400)
	r = rospy.Rate(RATE)
	for i in range(4):
		walk(DIRECTION.East)
		r.sleep()
	pos.incr_x()

def move_W(pos):
	"""Wrapper function to make the robot move one cell west

	   Keyword arguments:
	   pos -- the robot's current Position
	"""
	for motor in MOTORS:
		setMotorTargetSpeed(motor, 400)
	r = rospy.Rate(RATE)
	for i in range(5):
		walk(DIRECTION.West)
		r.sleep()
	pos.decr_x()

def move_to(c_pos, g_pos):
	if c_pos != g_pos:
		if c_pos.y > g_pos.y:
			move_S(c_pos)
		elif c_pos.y < g_pos.y:
			move_N(c_pos)
		else:
			if c_pos.x > g_pos.x:
				move_W(c_pos)
			elif c_pos.x < g_pos.x:
				move_E(c_pos)
		move_to(c_pos, g_pos)

########################
## Pathfinding Things ##
########################
def getNeighbours(pos):
	return [Position(pos.x+1, pos.y), Position(pos.x, pos.y+1), Position(pos.x-1, pos.y), Position(pos.x, pos.y-1)]

def heuristic(p0, p1):
	return abs(p0.x - p1.x) + abs(p0.y - p1.y)

def something(start, goal):
	frontier = PriorityQueue()
	frontier.put(start)
	_from = {}
	cost = {}
	_from[start] = None
	cost[start] = 0

	while not frontier.empty():
		current = frontier.get()
		if current == goal:
			break

		for nxt in getNeighbours(current)
			new_cost = cost[current] 
			if nxt not in _from:
				priority = heuristic(goal, nxt)
				frontier.put(nxt, priority)
				_from[nxt] = current

	current = goal
	path = [current]
	while current != start:
		current = _from[current]
		path += [current]

	return path.reverse()

def generate_costmap(start, map):
	frontier = Queue()
	frontier.put(start)
	cost = {}
	cost[start] = 0

	while not frontier.empty():
		current = frontier.get()
		direction = DIRECTION.South
		for nxt in getNeighbours(current):
			if nxt.x > current.x:
				direction = DIRECTION.East
			elif nxt.x < current.x:
				direction = DIRECTION.West
			elif nxt.y > current.y:
				direction = DIRECTION.North
			else:
				direction = DIRECTION.South

			if map.getNeighborObstacle(current.x, current.y, direction) > 0:
				map.setNeighborCost(current.x, current.y, direction, 1000)
			else:
				map.setNeighborCost(current.x, current.y, direction, 0)


if __name__ == '__main__':
	"""Main function"""
	rospy.init_node('asn0_node', anonymous=True)
	rospy.loginfo('Starting Group E Control Node...')

	x0 = int(raw_input('Enter the starting x position: '))
	y0 = int(raw_input('Enter the starting y position: '))

	xf = int(raw_input('Enter the final x position: '))
	yf = int(raw_input('Enter the final y position: '))
	#Make a new Position object to store the robot's position in the world
	start = Position(x0, y0)
	#Create the EECSMap object that will store the map to navigate
	# mp = EECSMap()

	goal = Position(xf, yf)
	# r = rospy.Rate(100)
	# total = 0
	# for i in xrange(100):
	# 	total += getSensorValue(3)
	# 	r.sleep()
	# INITIAL_H_Y = total / 100

	# INITIAL_H_X = getSensorValue(4)
	# print INITIAL_H_Y



	move_to(pos, goal)