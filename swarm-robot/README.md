# Swarm Robot Phase 1

Simulation-first multi-robot research platform.

## Goal
Demonstrate 10 autonomous ground robots coordinating tasks, avoiding collisions, and recovering from the loss of one robot.

## Current architecture
ROS 2 Jazzy + Gazebo Harmonic + ros_gz + Nav2 + swarm coordination layer.

## Repository map
- `PROJECT.md` — project vision and success criteria
- `requirements.md` — testable requirements
- `architecture.md` — system architecture and state model

## Development order
1. Simulation package scaffold
2. Single robot model
3. Multi-robot spawning and namespaces
4. Individual navigation
5. Swarm registry
6. Task allocation
7. Dropout/reassignment
8. Acceptance test
9. Metrics and dashboard

## References
- Nav2 Gazebo setup: https://docs.nav2.org/setup_guides/gazebo.html
- Gazebo ROS 2 integration: https://gazebosim.org/docs/harmonic/ros2_integration/
