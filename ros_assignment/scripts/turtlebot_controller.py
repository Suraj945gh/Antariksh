#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from ros_assignment.srv import ComputeAngVel

class TurtlebotController:
    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher for cmd_vel
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Subscriber for /radius
        rospy.Subscriber('/radius', Float64, self.radius_callback)

        # Service client for compute_ang_vel
        rospy.wait_for_service('compute_ang_vel')
        self.compute_ang_vel_client = rospy.ServiceProxy('compute_ang_vel', ComputeAngVel)

        # Linear velocity
        self.linear_velocity = 0.1

    def radius_callback(self, radius_msg):
        rospy.loginfo("Received radius: %f", radius_msg.data)

        try:
            # Call the compute_ang_vel service to get angular velocity
            response = self.compute_ang_vel_client(radius_msg.data)
            angular_velocity = response.angular_velocity

            # Create Twist message for cmd_vel
            vel_msg = Twist()
            vel_msg.linear.x = self.linear_velocity
            vel_msg.angular.z = angular_velocity

            # Publish the velocity to cmd_vel
            self.vel_pub.publish(vel_msg)

        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: %s", str(e))

if __name__ == "__main__":
    turtlebot_controller = TurtlebotController()
    rospy.spin()
