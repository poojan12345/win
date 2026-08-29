#!/usr/bin/env python3
"""One-command Phase 1 simulation bringup."""
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    headless = DeclareLaunchArgument('headless', default_value='False')
    pkg = FindPackageShare('swarm_robot')
    world = PathJoinSubstitution([pkg, 'world', 'swarm_test_world.sdf'])
    bridge_cfg = PathJoinSubstitution([pkg, 'config', 'bridge_config.yaml'])
    spawn = PathJoinSubstitution([pkg, 'launch', 'spawn_swarm.py'])
    nav2 = PathJoinSubstitution([pkg, 'launch', 'multirobot_nav2.launch.py'])

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('ros_gz_sim'), '/launch/gz_sim.launch.py'
        ]),
        launch_arguments={
            'gz_args': ['-r ', world],
        }.items(),
    )
    bridge = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('ros_gz_bridge'), '/launch/ros_gz_bridge.launch.py'
        ]),
        launch_arguments={
            'bridge_name': 'swarm_bridge',
            'config_file': bridge_cfg,
        }.items(),
    )
    spawn_action = TimerAction(
        period=3.0,
        actions=[ExecuteProcess(cmd=['python3', spawn], output='screen')],
    )
    nav_action = TimerAction(
        period=8.0,
        actions=[IncludeLaunchDescription(PythonLaunchDescriptionSource(nav2))],
    )
    return LaunchDescription([headless, gazebo, bridge, spawn_action, nav_action])
