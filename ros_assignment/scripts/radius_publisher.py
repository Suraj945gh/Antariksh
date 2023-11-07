#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def radius_publisher():
    rospy.init_node('radius_publisher', anonymous=True)
    rate = rospy.Rate(1)  # Publish rate of 1 Hz

    pub = rospy.Publisher('/radius', Float64, queue_size=10)

    while not rospy.is_shutdown():
        radius = 2.0  # You can set the desired radius value here
        pub.publish(radius)
        rate.sleep()

if __name__ == '__main__':
    try:
        radius_publisher()
    except rospy.ROSInterruptException:
        pass
