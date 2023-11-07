#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def world_publisher():
    pub = rospy.Publisher('/world', String, queue_size=10)
    rospy.init_node('world_publisher', anonymous=True) 
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        world_str = "World !" 
        # Basically this rospy.get_time() function returns current time, so here we are
        # printing hello + (current time) , just using this for timestamp
        rospy.loginfo(world_str)  # Just logging in to display on to the console
        pub.publish(world_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        world_publisher()
    except rospy.ROSInterruptException:
        pass