# Launch plan

Phase 1 launch sequence:

1. Start Gazebo Harmonic world.
2. Spawn 10 research_ground_robot instances using unique namespaces `/swarm/robot_01` through `/swarm/robot_10`.
3. Start the ROS-Gazebo bridge.
4. Bring up individual Nav2 stacks.
5. Start the swarm coordinator.
6. Publish exploration tasks.
7. Monitor heartbeats and task state.
8. Inject one simulated dropout and verify reassignment.

For ROS 2 Jazzy and Gazebo Harmonic, use `ros_gz_sim` for model spawning and `ros_gz_bridge` for transport interoperability.
