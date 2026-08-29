# Phase 1 local runbook

This is the first executable simulation path. It assumes Ubuntu with ROS 2 Jazzy, Gazebo Harmonic, Nav2 and ros_gz installed.

## 1. Source ROS

```bash
source /opt/ros/jazzy/setup.bash
```

## 2. Start Gazebo

```bash
gz sim -r swarm-robot/worlds/swarm_test_world.sdf
```

## 3. Spawn the 10 robots

From the repository root:

```bash
python3 swarm-robot/launch/spawn_swarm.py
```

The script creates robot_01 through robot_10 at deterministic starting positions.

## 4. Bridge required topics

Use `ros_gz_bridge` to bridge the command, odometry and laser topics needed by the ROS side. The exact bridge topic names should be confirmed against the installed Gazebo/ROS package versions before running Nav2.

Example pattern:

```bash
ros2 run ros_gz_bridge parameter_bridge /scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan
```

## 5. Next integration layer

The next implementation step is per-robot TF/odometry namespacing and Nav2 bringup. Do not treat this runbook as a completed Nav2 swarm demo until the acceptance tests pass.

## 6. Acceptance target

- 10 robots visible in Gazebo
- independent robot command/odometry topics
- unique ROS namespaces
- individual navigation working
- swarm task allocation working
- one simulated dropout causes task reassignment
- automated test records pass/fail

## Safety

Phase 1 is a civilian/research simulation. No weapon, targeting, engagement or harmful payload functionality is included.
