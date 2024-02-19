from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    package = get_package_share_path('robotont_description')
    default_model_path = package / 'urdf/robotont_base.urdf.xacro'
    default_rviz_config_path = package / 'config/robotont_description.rviz'

    model_arg = DeclareLaunchArgument(name='model', default_value=str(default_model_path))
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=str(default_rviz_config_path))
    rviz_fixed_frame_arg = DeclareLaunchArgument(name='rviz_fixed_frame', default_value='base_link')

    robot_description = ParameterValue(Command(['xacro ', LaunchConfiguration('model')]), value_type=str)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig'),
        '--fixed-frame', LaunchConfiguration(variable_name='rviz_fixed_frame')
        ],

    )

    return LaunchDescription([
        model_arg,
        rviz_arg,
        rviz_fixed_frame_arg,
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node
    ])