#!/usr/bin/env python3
from dataclasses import dataclass
from enum import Enum
from time import monotonic
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotState(str, Enum):
    AVAILABLE='AVAILABLE'; ASSIGNED='ASSIGNED'; EXECUTING='EXECUTING'; COMPLETE='COMPLETE'; UNAVAILABLE='UNAVAILABLE'

@dataclass
class Robot:
    robot_id: str
    state: RobotState = RobotState.AVAILABLE
    task_id: str | None = None
    last_heartbeat: float = 0.0

@dataclass
class Task:
    task_id: str
    goal_x: float
    goal_y: float
    robot_id: str | None = None
    complete: bool = False

class SwarmCoordinator(Node):
    def __init__(self):
        super().__init__('swarm_coordinator')
        self.declare_parameter('robot_count', 10)
        self.declare_parameter('heartbeat_timeout_s', 5.0)
        self.robot_count = int(self.get_parameter('robot_count').value)
        self.timeout = float(self.get_parameter('heartbeat_timeout_s').value)
        self.robots = {f'robot_{i:02d}': Robot(f'robot_{i:02d}', last_heartbeat=monotonic()) for i in range(1, self.robot_count+1)}
        self.tasks = {f'task_{i:02d}': Task(f'task_{i:02d}', float((i%5)*2-4), float((i//5)*4-2)) for i in range(1, self.robot_count+1)}
        self.pub = self.create_publisher(String, '/swarm/events', 10)
        self.timer = self.create_timer(1.0, self.tick)
        self.allocate()

    def emit(self, text):
        msg = String(); msg.data = text; self.pub.publish(msg); self.get_logger().info(text)

    def allocate(self):
        available = [r for r in self.robots.values() if r.state == RobotState.AVAILABLE and r.task_id is None]
        pending = [t for t in self.tasks.values() if t.robot_id is None and not t.complete]
        for robot, task in zip(available, pending):
            robot.state = RobotState.ASSIGNED; robot.task_id = task.task_id; task.robot_id = robot.robot_id
            self.emit(f'ASSIGN {robot.robot_id} -> {task.task_id}')

    def tick(self):
        now = monotonic()
        for robot in self.robots.values():
            if robot.state != RobotState.UNAVAILABLE and now - robot.last_heartbeat > self.timeout:
                old_task = robot.task_id
                robot.state = RobotState.UNAVAILABLE; robot.task_id = None
                if old_task and old_task in self.tasks: self.tasks[old_task].robot_id = None
                self.emit(f'DROPOUT {robot.robot_id}; released={old_task}')
        self.allocate()


def main(args=None):
    rclpy.init(args=args); node=SwarmCoordinator()
    try: rclpy.spin(node)
    except KeyboardInterrupt: pass
    finally: node.destroy_node(); rclpy.shutdown()

if __name__ == '__main__': main()
