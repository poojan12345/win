#!/usr/bin/env python3
"""Verify the expected per-robot ROS topics exist after bringup."""
import subprocess
import sys

robots = [f"robot_{i:02d}" for i in range(1, 11)]
expected = []
for robot in robots:
    expected += [
        f"/swarm/{robot}/scan",
        f"/swarm/{robot}/odom",
        f"/swarm/{robot}/cmd_vel",
    ]

result = subprocess.run(["ros2", "topic", "list"], capture_output=True, text=True, check=True)
active = set(result.stdout.splitlines())
missing = [topic for topic in expected if topic not in active]

if missing:
    print("FAIL: missing topics")
    print("\n".join(missing))
    sys.exit(1)

print(f"PASS: all {len(expected)} robot topics are present")
