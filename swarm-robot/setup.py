from setuptools import setup
from glob import glob
import os

package_name = 'swarm_robot'

data_files = [
    ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
]
for directory in ['launch', 'config', 'description', 'world', 'rviz']:
    files = glob(os.path.join(directory, '*'))
    if files:
        data_files.append((f'share/{package_name}/{directory}', files))

data_files.append(('share/' + package_name + '/swarm-robot', []))

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    description='Simulation-first multi-robot swarm research platform',
    entry_points={
        'console_scripts': [
            'swarm_coordinator = swarm_robot.swarm_coordinator:main',
        ],
    },
)
