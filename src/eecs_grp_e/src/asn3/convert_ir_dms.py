#!/usr/bin/env python
import roslib
import rospy

from asn3_utility.utility import sendCommand
from asn3_utility.globals import *

from fw_wrapper.srv import *

# DMS
# 25 cm ==> 924.22 ==> 36.9688
# 20 cm ==> 1097.389 ==> 54.86945
# 15 cm ==> 1413.833 ==> 94.2555
# 10 cm ==> 2064.759 ==> 206.4759
# 5  cm ==> 2688.91 ==> 537.782
# # conv: 186.07033 = [sens] / [cm]
# # conv: [cm] = [sens] / k
# 413836.537 * (x ** -1.416) (+/- 2.5)

# IR
# 35 cm ==> 0
# 30 cm ==> 10
# 25 cm ==> 46
# 20 cm ==> 70
# 15 cm ==> 126
# 10 cm ==> 291
# 5  cm ==> 957
# 188.567 * (x ** -0.525)


def convert_dms_cm(dms_val):
    """Convert values from the DMS into centimetres
    :param dms_val: DMS value
    """
    return 413836.537 * (dms_val ** -1.416)


def convert_ir_cm(ir_val):
    """Convert values from the IR sensors into centimetres
    :param ir_val: IR sensor value
    """
    return 98.098 * (ir_val ** -0.406)


def avg(vals):
    """Compute the average value of a list of values
    :param vals: The list of values
    """
    r = 0
    for v in vals:
        r += v
    return r / len(vals)

if __name__ == '__main__':
    rospy.init_node('test_node', anonymous=True)

    v = sendCommand(COMMANDS.GetSensorValue, receiver=1)
    print 'sensor value: %f' % v
    print 'function returns: %f' % convert_dms_cm(v)

    # vals = []
    # if raw_input('go? ') == 'y':
    #     for i in xrange(1000):
    #         print i
    #         vals.append(sendCommand(COMMANDS.GetSensorValue, receiver=1))

    # print avg(vals)
