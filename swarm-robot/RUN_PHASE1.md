# Phase 1 Runtime

## Environment
Use Ubuntu with ROS 2 Jazzy and Gazebo Harmonic. Nav2's current Gazebo setup guide targets Gazebo Harmonic or newer with ROS 2 Jazzy or newer.

## Install dependencies

```bash
sudo apt update
sudo apt install ros-jazzy-navigation2 ros-jazzy-nav2-bringup ros-jazzy-ros-gz
```

## Build

From the workspace root:

```bash
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
```

## Launch

```bash
ros2 launch swarm_robot phase1_bringup.launch.py
```

The launch sequence starts Gazebo, the ROS-Gazebo bridge, ten namespace-isolated robots, and ten Nav2 navigation stacks.

## Verify isolation

In a second terminal:

```bash
source /opt/ros/jazzy/setup.bash
source install/setup.bash
python3 src/win/swarm-robot/tests/verify_swarm_topics.py
```

Expected result:

`PASS: all 30 robot topics are present`

## Inspect one robot

```bash
ros2 topic list | grep /swarm/robot_01
ros2 topic echo /swarm/robot_01/odom
ros2 topic echo /swarm/robot_01/scan
```

## Current acceptance gate

The project is not considered runtime-validated until all ten robots publish isolated scan/odom/cmd_vel topics and each Nav2 instance resolves its own `robot_N/odom` -> `robot_N/base_link` TF chain without conflicts.
