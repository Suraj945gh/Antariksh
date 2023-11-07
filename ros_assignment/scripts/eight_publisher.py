#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def eight_publisher():
    rospy.init_node('eight_publisher', anonymous=True)
    rate = rospy.Rate(1)  # Publish rate of 1 Hz

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    while not rospy.is_shutdown():
        vel_msg = Twist()
        # Move in a figure-eight pattern
        vel_msg.linear.x = 0.2
        vel_msg.angular.z = 0.1
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        eight_publisher()
    except rospy.ROSInterruptException:
        pass
