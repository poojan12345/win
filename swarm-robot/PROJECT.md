# Swarm Robot Project

## Vision
Build a simulation-first multi-robot swarm platform that demonstrates distributed coordination, autonomous navigation, collision avoidance, task allocation, and graceful handling of robot loss.

## Phase 1 objective
Demonstrate 10 simulated ground robots operating as a coordinated swarm in a controlled environment.

## Scope
- Multi-robot simulation
- Per-robot navigation
- Robot namespaces and state
- Swarm communication abstraction
- Task allocation
- Collision avoidance
- Formation and exploration behaviors
- Central monitoring dashboard
- Repeatable automated tests

## Safety boundary
This project is initially a civilian/research robotics platform. No weapon payloads, targeting, or harmful operational functions are included in Phase 1.

## Architecture
- ROS 2 middleware
- Gazebo-based simulation
- Nav2 for individual navigation
- Swarm coordination layer above navigation
- Ground-station/monitoring layer
- Airtable for engineering inventory and test tracking
- Notion for requirements and decisions

## Initial success criteria
1. Spawn 10 robots reliably.
2. Assign unique identities and namespaces.
3. Send a mission/task to the swarm.
4. Allocate work among available robots.
5. Prevent robot-robot collisions in normal scenarios.
6. Complete a coordinated demonstration without manual driving.
7. Remove one simulated robot during execution and show graceful reallocation.
8. Log all major robot states and mission events.

## Research baselines
- ROS2swarm: reusable swarm-behavior concepts.
- Multi-robot Nav2/Gazebo examples: scalable simulation patterns.
- ReMRoC: realistic multi-robot coordination and benchmarking.

## Engineering principle
Simulation first, then a small safe physical prototype. Hardware procurement happens only after the simulation architecture and acceptance tests are stable.
