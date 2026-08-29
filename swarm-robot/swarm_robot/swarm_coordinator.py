"""Minimal ROS 2 swarm coordinator for the Phase 1 simulation."""
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SwarmCoordinator(Node):
    def __init__(self):
        super().__init__('swarm_coordinator')
        self.robot_count = 10
        self.last_seen = {f'robot_{i:02d}': time.monotonic() for i in range(1, 11)}
        self.state_pub = self.create_publisher(String, 'swarm/status', 10)
        self.timer = self.create_timer(1.0, self.tick)

    def tick(self):
        active = sum(time.monotonic() - t < 5.0 for t in self.last_seen.values())
        msg = String()
        msg.data = f'active_robots={active};total={self.robot_count}'
        self.state_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = SwarmCoordinator()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()
