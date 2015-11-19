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

def getSensorValue(port):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('GetSensorValue', port, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


if __name__ == '__main__':
	rospy.init_node('test_node', anonymous=True)

	vals = []
	if raw_input('go? ') == 'yes':

		for i in xrange(1000):
			print i
			vals.append(getSensorValue(1))
			rospy.loginfo('%f', getSensorValue(1))

		result = 0.
		for v in vals:
			result += v

		print result / len(vals)
