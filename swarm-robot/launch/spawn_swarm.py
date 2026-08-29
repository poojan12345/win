#!/usr/bin/env python3
"""Spawn the Phase 1 research robots into Gazebo using ros_gz_sim."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "description" / "research_ground_robot.sdf"

POSES = [(-6,-6),(-2,-6),(2,-6),(6,-6),(-6,-2),(-2,-2),(2,-2),(6,-2),(-3,4),(3,4)]

for i, (x, y) in enumerate(POSES, 1):
    name = f"robot_{i:02d}"
    namespace = f"/swarm/{name}"
    cmd = [
        "ros2", "run", "ros_gz_sim", "create",
        "-name", name,
        "-file", str(MODEL),
        "-x", str(x), "-y", str(y), "-z", "0.15",
    ]
    print(f"Spawning {namespace} at ({x}, {y})")
    subprocess.run(cmd, check=True)
