#!/usr/bin/env python3

import rospy
from ros_assignment.srv import Trajectory, TrajectoryResponse
import matplotlib.pyplot as plt

class TrajectoryServer:
    def __init__(self):
        rospy.init_node('trajectory_server')
        self.state = {'x': 0.0, 'y': 0.0}
        self.default_vx = 1.0
        self.default_vy = 0.0
        self.trajectory = []

        rospy.Service('get_trajectory', Trajectory, self.handle_trajectory_request)
        rospy.loginfo('Trajectory Server Ready')

    def handle_trajectory_request(self, req):
        vx = req.vx if req.vx != 0.0 else self.default_vx
        vy = req.vy if req.vy != 0.0 else self.default_vy

        intermediate_trajectory = self.calculate_trajectory(vx, vy)
        self.publish_trajectory_plot(intermediate_trajectory)

        return TrajectoryResponse(intermediate_trajectory)

    def calculate_trajectory(self, vx, vy):
        dt = 0.1
        num_steps = 50
        intermediate_trajectory = []

        for _ in range(num_steps):
            self.state['x'] += vx * dt
            self.state['y'] += vy * dt
            intermediate_trajectory.append((self.state['x'], self.state['y']))

        return intermediate_trajectory

    def publish_trajectory_plot(self, trajectory):
        x_values, y_values = zip(*trajectory)
        plt.plot(x_values, y_values, label='Intermediate Trajectory')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    server = TrajectoryServer()
    rospy.spin()
