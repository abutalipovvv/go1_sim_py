# Modified for ros2 by: abutalipovvv
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Запуск узла контроллера робота
        Node(
            package='go1_controller',
            executable='robot_controller_gazebo.py',
            name='ROBOT_CONTROLLER',
            output='screen',
            parameters=[{
                'use_sim_time': True  # Если вы используете симуляцию
            }]
        ),
    ])