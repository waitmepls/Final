#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "          %s", data.data)
def exe():
    rospy.init_node('exe', anonymous=True)
    rospy.Subscriber("std_id", Int64, callback)
    rospy.spin()

if __name__ == '__main__':
    exe()