from ament_index_python.packages import get_package_share_path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    package = get_package_share_path('robotont_description')
    default_rviz_config_path = package / 'config/robotont_description.rviz'

    model_decl = DeclareLaunchArgument(name='model', default_value='')
    rviz_config_decl = DeclareLaunchArgument(name='rviz_config', default_value=str(default_rviz_config_path))
    rviz_fixed_frame_decl = DeclareLaunchArgument(name='rviz_fixed_frame', default_value='base_link')
    generation_decl = DeclareLaunchArgument(name='generation', default_value='3')
    primary_color_decl = DeclareLaunchArgument(
        name='primary_color',
        default_value='light_blue'   # light blue
    )

    model_arg = LaunchConfiguration('model')
    rviz_config_arg = LaunchConfiguration('rviz_config')
    rviz_fixed_frame_arg = LaunchConfiguration('rviz_fixed_frame')
    generation_arg = LaunchConfiguration('generation')
    primary_color_name = LaunchConfiguration('primary_color')

    robot_model_path = PythonExpression([
        '"" if "', model_arg,
        '" else "', str(package / "urdf/"), '" + (',
        '"/gen2_1/robotont.urdf.xacro" if "', generation_arg, '" == "2.1" else "/gen3/robotont.urdf.xacro")'
    ])
    primary_color_rgba = PythonExpression([
        '"0.16 0.65 0.98 1.0" if "', primary_color_name, '" == "light_blue" else ',
        '"0.00 0.35 0.90 1.0" if "', primary_color_name, '" == "blue" else ',
        '"1.00 1.00 0.00 1.0" if "', primary_color_name, '" == "yellow" else ',
        '"0.10 0.10 0.10 1.0" if "', primary_color_name, '" == "black" else ',
        '"0.45 0.20 0.65 1.0" if "', primary_color_name, '" == "purple" else ',
        '"0.65 0.65 0.65 1.0" if "', primary_color_name, '" == "gray" else ',
        '"0.00 0.45 0.25 1.0" if "', primary_color_name, '" == "dark_green" else ',
        '"0.00 0.80 0.30 1.0" if "', primary_color_name, '" == "green" else ',
        '"0.16 0.65 0.98 1.0"'
    ])
    robot_description = ParameterValue(Command(['xacro ', robot_model_path, ' main_color:="', primary_color_rgba, '"']), value_type=str)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{ 'robot_description': robot_description }]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=[
            '-d',
            rviz_config_arg,
            '--fixed-frame',
            rviz_fixed_frame_arg
        ]
    )

    return LaunchDescription(
        [
            model_decl,
            generation_decl,
            rviz_config_decl,
            rviz_fixed_frame_decl,
            primary_color_decl,
            joint_state_publisher_node,
            robot_state_publisher_node,
            rviz_node
        ]
    )
