from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
  

    bathroom_node = Node(
        package='my_bot',
        executable='bathroom.py',
        name='bathroom_node',
        output='screen'
    )

    

    return LaunchDescription([
        bathroom_node
        ])
