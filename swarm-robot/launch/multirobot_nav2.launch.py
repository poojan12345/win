#!/usr/bin/env python3
"""Launch the Phase 1 multi-robot Nav2 stack.

This launch file intentionally keeps every robot inside its own ROS namespace.
It is designed for ROS 2 Jazzy + Gazebo Harmonic and assumes the simulation
world and robot models have already been started.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, PushRosNamespace
from launch_ros.descriptions import ComposableNode
from launch_ros.actions import ComposableNodeContainer

ROBOT_COUNT = 10


def robot_group(name: str):
    return GroupAction([
        PushRosNamespace(name),
        Node(
            package='nav2_bringup',
            executable='bringup_launch.py',
            name='nav2_bringup',
            output='screen',
            parameters=[
                LaunchConfiguration('params_file'),
                {'use_sim_time': True},
            ],
            arguments=['namespace:=', name, 'use_namespace:=True', 'autostart:=True'],
        ),
    ])


def generate_launch_description():
    params_file = DeclareLaunchArgument(
        'params_file',
        default_value='swarm-robot/config/nav2_params.yaml',
        description='Shared namespaced Nav2 parameter file',
    )

    groups = [robot_group(f'swarm/robot_{i:02d}') for i in range(1, ROBOT_COUNT + 1)]

    return LaunchDescription([params_file, *groups])
