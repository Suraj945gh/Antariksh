#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def hello_publisher():
    pub = rospy.Publisher('/hello', String, queue_size=10)
    rospy.init_node('hello_publisher', anonymous=True) 
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # hello_str = "hello %s" % rospy.get_time() 
        # Basically this rospy.get_time() function returns current time, so here we are
        # printing hello + (current time) , just using this for timestamp

        hello_str = "Hello," 
        rospy.loginfo(hello_str)  # Just logging in to display on to the console
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        hello_publisher()
    except rospy.ROSInterruptException:
        pass