#!/usr/bin/env python
import roslib
import rospy
import random as r
from Queue import Queue, PriorityQueue
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
DMS_S = 6
IR_S = 4

RATE = 1

# Can store an ordered pair. It's useful
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
		return self.x != other.x and self.y != other.y
	
	def __str__(self):
		return '(' + str(self.x) + ',' + str(self.y) + ')'

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
		elif motor == DMS:
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

# Wrapper functions for stepping in each of the cardinal directions
def walk_N():
	"""Make the robot move to the north"""

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 724)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(LEFT_BACK_E, 724)
	setMotorTargetPositionCommand(LEFT_BACK, target2)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(LEFT_FRONT_E, 300)
	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(RIGHT_BACK_E, 300)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_BACK, target1)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)
	rospy.sleep(0.5)

def walk_S():
	"""Make the robot move to the south"""
	setMotorTargetPositionCommand(RIGHT_BACK_E, 250)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(LEFT_BACK, target2)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(LEFT_FRONT_E, 250)
	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(LEFT_BACK_E, 774)
	setMotorTargetPositionCommand(LEFT_BACK, target1)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)
	rospy.sleep(0.5)

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 774)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)
	rospy.sleep(0.5)

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

	setMotorTargetPositionCommand(RIGHT_BACK_E, 250)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)

	setMotorTargetPositionCommand(LEFT_BACK_E, 774)
	setMotorTargetPositionCommand(LEFT_BACK, target1)
	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 774)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)

	setMotorTargetPositionCommand(LEFT_FRONT_E, 250)
	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(LEFT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)

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

	setMotorTargetPositionCommand(RIGHT_FRONT_E, 774)
	setMotorTargetPositionCommand(RIGHT_FRONT, target2)
	setMotorTargetPositionCommand(RIGHT_BACK, target0)
	setMotorTargetPositionCommand(RIGHT_FRONT_E, target1)

	setMotorTargetPositionCommand(LEFT_FRONT_E, 250)
	setMotorTargetPositionCommand(LEFT_FRONT, target2)
	setMotorTargetPositionCommand(LEFT_BACK, target1)
	setMotorTargetPositionCommand(LEFT_FRONT_E, target0)

	setMotorTargetPositionCommand(RIGHT_BACK_E, 250)
	setMotorTargetPositionCommand(RIGHT_BACK, target2)
	setMotorTargetPositionCommand(RIGHT_FRONT, target1)
	setMotorTargetPositionCommand(RIGHT_BACK_E, target0)

	setMotorTargetPositionCommand(LEFT_BACK_E, 774)
	setMotorTargetPositionCommand(LEFT_BACK, target2)
	setMotorTargetPositionCommand(LEFT_FRONT, target0)
	setMotorTargetPositionCommand(LEFT_BACK_E, target1)

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

# Wrapper functions for moving a full cell in each of the cardinal directions
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
		setMotorTargetSpeed(motor, 600)
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

# Returns the DIRECTION from pos0 to pos1. A very naive function, only works when pos0 and pos1 are direct neighbours 
def get_direction(pos0, pos1):
	if pos0.x < pos1.x:
		return DIRECTION.South
	elif pos0.x > pos1.x:
		return DIRECTION.North

	if pos0.y < pos1.y:
		return DIRECTION.East
	elif pos0.y > pos1.y:
		return DIRECTION.West

# Make the robot move from c_pos to g_pos
def move_to(c_pos, g_pos):
	d = get_direction(c_pos, g_pos)
	r = rospy.Rate(RATE)
	if abs(g_pos.x - c_pos.x) > 1 or abs(g_pos.y - g_pos.y) > 1:
		if g_pos.x - c_pos.x > 1:
			while c_pos != g_pos:
				move_S(c_pos)
				r.sleep
		elif g_pos.y - c_pos.y > 1:
			while c_pos != g_pos:
				move_E(c_pos)
				r.sleep()
		elif g_pos.x - c_pos.x < 0:
			while c_pos != g_pos:
				move_N(c_pos)
				r.sleep()
		else:
			while c_pos != g_pos:
				move_W(c_pos)
				r.sleep()

	else:
		if d == DIRECTION.North:
			move_N(c_pos)
		elif d == DIRECTION.South:
			move_S(c_pos)
		elif d == DIRECTION.East:
			move_E(c_pos)
		elif d == DIRECTION.West:
			move_W(c_pos)
		else:
			print 'move_to(',str(c_pos),', ',str(g_pos),'): Invalid direction :('

def get_is_any_motor_moving():
	for motor in MOTORS:
		if getIsMotorMovingCommand(motor):
			return True
	return False

########################
## Pathfinding Things ##
########################

# Returns True if val is present in lst. We had to use this because for some reason, writing `key in dictionary` made our code loop infinitely
def sauce(val, lst):
    for v in lst:
        if v == val:
            return True
    return False

# Get all valid neighbours around pos
def getNeighbours(pos, map):
    n = []
    if map.getNeighborObstacle(pos.x, pos.y, DIRECTION.East) == 0:
        n.append(Position(pos.x, pos.y + 1))
    if map.getNeighborObstacle(pos.x, pos.y, DIRECTION.South) == 0:
        n.append(Position(pos.x + 1, pos.y))
    if map.getNeighborObstacle(pos.x, pos.y, DIRECTION.West) == 0:
        n.append(Position(pos.x, pos.y - 1))
    if map.getNeighborObstacle(pos.x, pos.y, DIRECTION.North) == 0:
        n.append(Position(pos.x - 1, pos.y))
    return n

# Return the Manhattan distance from p0 to p1
def heuristic(p0, p1):
	return abs(p0.x - p1.x) + abs(p0.y - p1.y)

def get_lowest_cost_neighbour(node, map):
	print 'I should be working ; ;'
	costs = {}
	# costs = { Position(x,y):int }
	for n in getNeighbours(node, map):
		costs[n] = map.getNeighborCost(node.x, node.y, get_direction(node, n))
		print str(costs[n])
		
	for k in costs.keys():
		print str(k),':',str(costs[k])
		
	#print str(min(costs, key=costs.get))
	return min(costs, key=costs.get)


def r_p(start, goal, map):
	pth = [goal]
	current = goal
	print str(start)
	print str(goal)
	print str(current)
	while current != start:
		print str(current)
		current = get_lowest_cost_neighbour(current, map)
		print str(current)		
		pth.append(current)

	pth.reverse()
	return pth

# An implementation of the A* algorithm (Patrick, as in Patrick Star)
def a_patrick(start, goal, map):
	frontier = PriorityQueue()
	frontier.put(start, 0)
	cost = {}
	cost[start] = 0

	while not frontier.empty():
		current = frontier.get()

		if current == goal:
			break

		for nxt in getNeighbours(current, map):
			new_cost = cost[current] + map.getNeighborCost(current.x, current.y, get_direction(current, nxt)) 
			if not nxt in cost.keys():
				cost[nxt] = new_cost
				map.setCost(nxt.x, nxt.y, new_cost)
				priority = new_cost + heuristic(goal, nxt)
				frontier.put(nxt, priority)

	return r_p(start, goal, map)

# Generate the costmap from start to goal on map
def generate_costmap(start, goal, map):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        for next in getNeighbours(current, map):
            if not sauce(next, visited):
                map.setCost(next.x, next.y, map.getCost(current.x, current.y) + 1)
                frontier.put(next)
                visited[next] = True

def explore(pos, map):
	rat = rospy.Rate(RATE)
	while not rospy.is_shutdown():
		s = False
		e = False
		w = False
		n = False
		## place obstacles on the map ##
		setMotorTargetPositionCommand(DMS, target2)
		rospy.sleep(1)
		if getSensorValue(DMS_S) > 1400:
			#obstacle to the south

			n = True

		setMotorTargetPositionCommand(DMS, target0)
		rospy.sleep(1)
		if getSensorValue(DMS_S) > 1400:
			#obstacle to the wast
			
			e = True
		
		setMotorTargetPositionCommand(DMS, target2)
		setMotorTargetPositionCommand(DMS, target1)
		rospy.sleep(1)
		if getSensorValue(DMS_S) > 1400:
			#obstacle to the east
			
			w = True
		setMotorTargetPositionCommand(DMS, target2)
		if getSensorValue(IR_S) > 120:
			#obstacle to the north

			s = True
		
		print 's: ' + str(s) + ' w: ' + str(w) + ' e: ' + str(e) + ' n: ' + str(n)
		map.printObstacleMap()
		
		## move robot ##
		if s and e and w and not n:
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.South)
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.East)
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.West)
			move_N(pos)
		elif s and e and not w and not n:
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.South)
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.East)
			if r.randint(0,1) > 0:
				move_N(pos)
			else:
				move_W(pos)
		elif s and w and not e:
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.South)
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.West)
			if r.randint(0,1) > 0:
				move_N(pos)
			else:
				move_E(pos)
		elif n and e and w and not s:
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.North)
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.East)
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.West)
			move_S(pos)
		elif n and e and not w:
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.North)
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.East)
			if r.randint(0,1) > 0:
				move_S(pos)
			else:
				move_W(pos)
		elif n and w and not e and not s:
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.North)
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.West)
			if r.randint(0,1) > 0:
				move_S(pos)
			else:
				move_E(pos)
		elif s and not e and not w and not n:
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.South)
			move_N(pos)
		elif e and not w and not s and not n:
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.East)
			move_W(pos)
		elif w and not e and not s and not n:
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.West)
			move_E(pos)
		else:
			map.setObstacle(pos.x, pos.y, 1, DIRECTION.North)
			move_S(pos)

		rat.sleep()

# Make the robot move along a path calculated by a_patrick(...)
def path(start, goal, map):
	pth = a_patrick(start, goal, map)
	print str(len(pth))
	r = rospy.Rate(RATE)
	for p in pth:
	    print str(p)
	last = start
	for p in pth:
		print 'moving from ' + str(last) + ' to ' + str(p)
		move_to(last, p)
		last = p
		r.sleep()
	
if __name__ == '__main__':
	"""Main function"""
	rospy.init_node('asn0_node', anonymous=True)
	rospy.loginfo('Starting Group E Control Node...')
	if raw_input('Type E for Exploration or P for Pathfinding: ').upper() == 'E':
		init_motors()
		map = EECSMap()
		map.clearObstacleMap()
		explore(Position(x=0, y=0), map)
	else:
		# User input
		x0 = int(raw_input('Enter the starting x position: '))
		y0 = int(raw_input('Enter the starting y position: '))

		xf = int(raw_input('Enter the final x position: '))
		yf = int(raw_input('Enter the final y position: '))

		init_motors()

		# Make a new Position object to store the robot's position in the world
		start = Position(x0, y0)
		# Make a new Position object to store the robot's goal position
		goal = Position(xf, yf)
		# Create the EECSMap object that will store the map to navigate
		map = EECSMap()
		map.printObstacleMap()
		generate_costmap(start, goal, map)
		map.printCostMap()
		r = rospy.Rate(RATE)
		path(start, goal, map)
