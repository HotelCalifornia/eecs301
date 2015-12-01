from utility import enum

__doc__ = """Yeah, globals might be bad, but here's a file full of them anyway"""

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

IR_X = 1
IR_Y = 2

COMMANDS = enum(GetSensorValue='GetSensorValue', GetMotorTargetPosition='GetMotorTargetPosition', GetMotorCurrentPosition='GetMotorCurrentPosition', SetMotorTargetPosition='SetMotorTargetPosition')