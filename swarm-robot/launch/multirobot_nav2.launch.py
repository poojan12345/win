#!/usr/bin/env python3
"""Launch ten namespaced Nav2 navigation stacks for the swarm."""
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from nav2_common.launch import RewrittenYaml

ROBOT_COUNT = 10


def generate_launch_description():
    params_arg = DeclareLaunchArgument(
        "params_file",
        default_value=PathJoinSubstitution([
            FindPackageShare("swarm_robot"), "config", "nav2_params.yaml"
        ]),
        description="Shared Nav2 parameters; frame IDs are rewritten per robot.",
    )
    nav2_launch = PathJoinSubstitution([
        FindPackageShare("nav2_bringup"), "launch", "navigation_launch.py"
    ])
    actions = [params_arg]
    for i in range(1, ROBOT_COUNT + 1):
        robot = f"robot_{i:02d}"
        namespace = f"swarm/{robot}"
        rewritten = RewrittenYaml(
            source_file=LaunchConfiguration("params_file"),
            root_key=namespace,
            param_rewrites={
                "robot_base_frame": f"{robot}/base_link",
                "global_frame": f"{robot}/odom",
                "odom_frame": f"{robot}/odom",
            },
            convert_types=True,
        )
        actions.append(IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_launch),
            launch_arguments={
                "namespace": namespace,
                "params_file": rewritten,
                "use_sim_time": "True",
                "autostart": "True",
                "use_composition": "False",
            }.items(),
        ))
    return LaunchDescription(actions)
