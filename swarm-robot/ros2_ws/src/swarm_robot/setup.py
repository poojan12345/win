from setuptools import setup
from glob import glob
import os

package_name = 'swarm_robot'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('../../../config/*')),
        (os.path.join('share', package_name, 'launch'), glob('../../../launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    description='Simulation-first multi-robot swarm research platform',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'swarm_coordinator = swarm_robot.swarm_coordinator:main',
        ],
    },
)
