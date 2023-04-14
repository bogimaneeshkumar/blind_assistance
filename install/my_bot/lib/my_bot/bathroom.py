#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from action_msgs.msg import GoalStatus
from rclpy.action import ActionClient

class DestinationNode(Node):
    def __init__(self):
        super().__init__('destination_node')
        self.publisher = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

    def navigate_to_pose(self, x, y):
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = "map"
        goal_pose.pose.position.x = float(x)
        goal_pose.pose.position.y = float(y)
        goal_pose.pose.orientation.w = 1.0
        self.publisher.publish(goal_pose)
        self.send_goal(goal_pose)

    def send_goal(self, goal_pose):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = goal_pose
        self.action_client.wait_for_server()
        self.action_client.send_goal(goal_msg)

def main(args=None):
    rclpy.init(args=args)

    destination_node = DestinationNode()

    destination_node.navigate_to_pose(x=4.747, y=-4.437)

    rclpy.spin(destination_node)

    destination_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
