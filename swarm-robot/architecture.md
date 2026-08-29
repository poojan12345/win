# Phase 1 Swarm Architecture

## Stack
- ROS 2 Jazzy
- Gazebo Harmonic
- ros_gz bridge
- Nav2
- Python/C++ swarm coordination layer

ROS 2 Jazzy + Gazebo Harmonic is the selected baseline because current Nav2 documentation targets this combination for modern Gazebo simulation.

## Layers

### Layer 1: Simulation
Gazebo world, robot models, physics, sensors and simulated failures.

### Layer 2: Individual robot autonomy
Each robot owns its namespace, state, localization and navigation stack. Nav2 handles individual navigation and obstacle avoidance.

### Layer 3: Swarm coordination
A separate coordinator maintains:
- robot registry
- task registry
- availability/health state
- task allocation
- task completion
- timeout/reassignment
- mission state

### Layer 4: Mission interface
A ground-station-facing interface sends high-level missions and receives telemetry/events. It should not directly drive every robot during normal autonomous operation.

## Robot namespace pattern
`/swarm/robot_01`
`/swarm/robot_02`
...
`/swarm/robot_10`

Each robot should expose isolated topics/actions beneath its namespace.

## Core swarm state machine
DISCOVERED -> AVAILABLE -> ASSIGNED -> EXECUTING -> COMPLETE
                         |              |
                         +-> UNAVAILABLE +-> TIMEOUT -> AVAILABLE

If a robot becomes unavailable while holding unfinished work, the coordinator marks the task as unassigned and reallocates it to an available robot.

## Phase 1 mission
Use a bounded simulated environment containing multiple exploration/waypoint tasks. Ten robots independently navigate to assigned tasks while the coordinator tracks progress. During the mission, deliberately remove one robot and verify that unfinished work is reassigned and the mission completes.

## Metrics
- Mission completion rate
- Task completion time
- Reassignment latency
- Collision count
- Minimum inter-robot distance
- Robot availability percentage
- Communication/message latency where measurable

## Safety boundary
The initial system is for civilian/research robotics simulation. No weaponization, targeting, engagement, or harmful payload behavior is part of Phase 1.
