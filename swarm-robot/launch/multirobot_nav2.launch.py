#!/usr/bin/env python3
"""Launch ten namespaced Nav2 instances for the Phase 1 swarm."""

from pathlib import Path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

ROBOT_COUNT = 10
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PARAMS = str(ROOT / 'config' / 'nav2_params.yaml')


def generate_launch_description():
    params_arg = DeclareLaunchArgument(
        'params_file',
        default_value=DEFAULT_PARAMS,
        description='Shared Nav2 parameter file',
    )

    nav2_launch = FindPackageShare('nav2_bringup')
    includes = []

    for i in range(1, ROBOT_COUNT + 1):
        namespace = f'swarm/robot_{i:02d}'
        includes.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    nav2_launch,
                    '/launch/bringup_launch.py',
                ]),
                launch_arguments={
                    'namespace': namespace,
                    'use_namespace': 'True',
                    'params_file': LaunchConfiguration('params_file'),
                    'use_sim_time': 'True',
                    'autostart': 'True',
                    'use_rviz': 'False',
                }.items(),
            )
        )

    return LaunchDescription([params_arg, *includes])
