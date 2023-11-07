#!/usr/bin/env python3

import rospy
from ros_assignment.srv import Trajectory
import matplotlib.pyplot as plt

def trajectory_client(vx, vy):
    rospy.wait_for_service('get_trajectory')
    try:
        get_trajectory = rospy.ServiceProxy('get_trajectory', Trajectory)
        response = get_trajectory(vx, vy)
        return response.trajectory
    except rospy.ServiceException as e:
        rospy.logerr(f'Service call failed: {e}')

if __name__ == '__main__':
    rospy.init_node('trajectory_client')
    
    # You can change these values based on your requirements
    vx_command = 1.0
    vy_command = 0.5

    intermediate_trajectory = trajectory_client(vx_command, vy_command)

    # Plotting the intermediate trajectory
    x_values, y_values = zip(*intermediate_trajectory)
    plt.plot(x_values, y_values, label='Intermediate Trajectory')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()
