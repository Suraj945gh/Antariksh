#!/usr/bin/env python3
import rospy
from ros_assignment.srv import ComputeAngVel, ComputeAngVelResponse
from std_msgs.msg import Float64

def compute_ang_vel_server(req):
    # Assuming linear velocity of 0.1
    linear_velocity = 0.1
    radius = req.radius

    # Compute angular velocity using v = ω * r
    angular_velocity = linear_velocity / radius

    return ComputeAngVelResponse(angular_velocity)

if __name__ == "__main__":
    rospy.init_node('compute_ang_vel_server')
    s = rospy.Service('compute_ang_vel', ComputeAngVel, compute_ang_vel_server)
    rospy.loginfo("Compute Angular Velocity Server is ready.")
    rospy.spin()
