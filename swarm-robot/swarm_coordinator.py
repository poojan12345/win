from dataclasses import dataclass, field
from enum import Enum
from time import monotonic

class RobotState(str, Enum):
    DISCOVERED = "DISCOVERED"
    AVAILABLE = "AVAILABLE"
    ASSIGNED = "ASSIGNED"
    EXECUTING = "EXECUTING"
    COMPLETE = "COMPLETE"
    UNAVAILABLE = "UNAVAILABLE"

class TaskState(str, Enum):
    UNASSIGNED = "UNASSIGNED"
    ASSIGNED = "ASSIGNED"
    COMPLETE = "COMPLETE"

@dataclass
class Robot:
    robot_id: str
    state: RobotState = RobotState.AVAILABLE
    last_heartbeat: float = field(default_factory=monotonic)
    task_id: str | None = None

@dataclass
class Task:
    task_id: str
    goal: tuple[float, float]
    state: TaskState = TaskState.UNASSIGNED
    robot_id: str | None = None

class SwarmCoordinator:
    def __init__(self, heartbeat_timeout_s=5.0):
        self.heartbeat_timeout_s = heartbeat_timeout_s
        self.robots = {}
        self.tasks = {}

    def register_robot(self, robot_id):
        self.robots[robot_id] = Robot(robot_id)

    def heartbeat(self, robot_id):
        if robot_id in self.robots:
            self.robots[robot_id].last_heartbeat = monotonic()
            if self.robots[robot_id].state == RobotState.UNAVAILABLE:
                self.robots[robot_id].state = RobotState.AVAILABLE

    def add_task(self, task_id, goal):
        self.tasks[task_id] = Task(task_id, goal)

    def allocate(self):
        available = [r for r in self.robots.values() if r.state == RobotState.AVAILABLE and r.task_id is None]
        pending = [t for t in self.tasks.values() if t.state == TaskState.UNASSIGNED]
        assignments = []
        for robot, task in zip(available, pending):
            robot.state = RobotState.ASSIGNED
            robot.task_id = task.task_id
            task.state = TaskState.ASSIGNED
            task.robot_id = robot.robot_id
            assignments.append((robot.robot_id, task.task_id))
        return assignments

    def mark_complete(self, robot_id):
        robot = self.robots[robot_id]
        if robot.task_id in self.tasks:
            self.tasks[robot.task_id].state = TaskState.COMPLETE
        robot.task_id = None
        robot.state = RobotState.COMPLETE

    def check_heartbeats(self):
        now = monotonic()
        dropped = []
        for robot in self.robots.values():
            if now - robot.last_heartbeat > self.heartbeat_timeout_s and robot.state != RobotState.UNAVAILABLE:
                robot.state = RobotState.UNAVAILABLE
                if robot.task_id in self.tasks:
                    self.tasks[robot.task_id].state = TaskState.UNASSIGNED
                    self.tasks[robot.task_id].robot_id = None
                    robot.task_id = None
                dropped.append(robot.robot_id)
        return dropped
