#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def helloworld_combiner():

    rospy.init_node('helloworld_combiner', anonymous=True)
    hello_sub = rospy.Subscriber("/hello", String, hello_callback)
    world_sub = rospy.Subscriber("/world", String, world_callback)
    global pub
    pub = rospy.Publisher("/helloworld",String,queue_size=10)
    rospy.spin()

def hello_callback(data):
    global hello_str
    hello_str = data.data
    combine_and_publish()

def world_callback(data):
    global world_str
    world_str = data.data
    combine_and_publish()

def combine_and_publish():
    
    combined_str = hello_str + " " + world_str
    rospy.loginfo(combined_str)
    pub.publish(combined_str)

if __name__ == '__main__':
    helloworld_combiner()
