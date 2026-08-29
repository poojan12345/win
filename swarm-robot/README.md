# Swarm Robot Simulation

Phase 1 is a simulation-first research platform for coordinated multi-robot ground systems.

## Stack
- ROS 2 Jazzy
- Gazebo Harmonic
- Nav2
- ros_gz bridge
- Python/C++ swarm coordination layer

## Phase 1 demo
10 robots spawn in a controlled world, receive distributed tasks, navigate, maintain separation, recover from one robot dropout, and complete the mission.

## Repository layout
- `config/` simulation and swarm parameters
- `description/` robot model assets
- `worlds/` simulation worlds
- `launch/` launch files
- `swarm/` coordination package
- `tests/` acceptance tests

## Development rule
Simulation and civilian/research behaviors first. No weapon payloads, targeting, engagement, or harmful operational functions are part of this phase.
