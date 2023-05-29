#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
def unload():
    pub = rospy.Publisher('std_id', Int64, queue_size=10)
    rospy.init_node('unload', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = 6352500374
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
if __name__ == '__main__':
    try:
        unload()
    except rospy.ROSInterruptException:
        pass