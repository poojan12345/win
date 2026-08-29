from time import monotonic

import rclpy
from rclpy.node import Node


class SwarmCoordinatorNode(Node):
    """Minimal ROS 2 coordinator shell for Phase 1 integration testing."""

    def __init__(self):
        super().__init__('swarm_coordinator')
        self.declare_parameter('robot_count', 10)
        self.declare_parameter('heartbeat_timeout_s', 5.0)
        self.robot_count = int(self.get_parameter('robot_count').value)
        self.heartbeat_timeout_s = float(self.get_parameter('heartbeat_timeout_s').value)
        self.last_tick = monotonic()
        self.get_logger().info(
            f'Swarm coordinator online: {self.robot_count} robots, '
            f'heartbeat timeout {self.heartbeat_timeout_s:.1f}s'
        )
        self.create_timer(1.0, self._tick)

    def _tick(self):
        now = monotonic()
        self.last_tick = now
        self.get_logger().debug('Coordinator heartbeat cycle')


def main(args=None):
    rclpy.init(args=args)
    node = SwarmCoordinatorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
