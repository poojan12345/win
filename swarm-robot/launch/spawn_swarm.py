#!/usr/bin/env python3
"""Spawn ten namespace-isolated research robots into Gazebo Harmonic."""
from pathlib import Path
import os
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "description" / "research_ground_robot.sdf"
POSES = [(-6,-6),(-2,-6),(2,-6),(6,-6),(-6,-2),(-2,-2),(2,-2),(6,-2),(-3,4),(3,4)]


def main():
    template = TEMPLATE.read_text(encoding="utf-8")
    cache = Path(tempfile.gettempdir()) / "swarm_robot_models"
    cache.mkdir(parents=True, exist_ok=True)
    for i, (x, y) in enumerate(POSES, 1):
        name = f"robot_{i:02d}"
        model = cache / f"{name}.sdf"
        model.write_text(template.replace("__ROBOT__", name), encoding="utf-8")
        cmd = [
            "ros2", "run", "ros_gz_sim", "create",
            "-name", name, "-file", str(model),
            "-x", str(x), "-y", str(y), "-z", "0.15",
        ]
        print(f"Spawning /swarm/{name} at ({x}, {y})")
        subprocess.run(cmd, check=True, env=os.environ.copy())


if __name__ == "__main__":
    main()
