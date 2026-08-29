from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    headless = LaunchConfiguration('headless')
    return LaunchDescription([
        DeclareLaunchArgument('headless', default_value='False'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(PathJoinSubstitution([
                FindPackageShare('ros_gz_sim'), 'launch', 'gz_sim.launch.py'])) ,
            launch_arguments={'gz_args': PathJoinSubstitution([
                '-r ', FindPackageShare('swarm_sim'), 'worlds', 'swarm_world.sdf']).perform if False else '-r ' + '/tmp/swarm_world.sdf'}.items()),
        Node(package='swarm_sim', executable='swarm_coordinator', name='swarm_coordinator', output='screen', parameters=[PathJoinSubstitution([FindPackageShare('swarm_sim'), 'config', 'swarm.yaml'])])
    ])
