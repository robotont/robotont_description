from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    prefix_decl = DeclareLaunchArgument("prefix", default_value="")
    generation_decl = DeclareLaunchArgument("generation", default_value="3")

    generation_arg = LaunchConfiguration("generation")

    model_path = PathJoinSubstitution([
        FindPackageShare("robotont_description"),
        "urdf",
        PythonExpression([
            '"gen2_1/robotont.urdf.xacro" if "', generation_arg, '" == "2.1" else "gen3/robotont.urdf.xacro"'
        ])
    ])

    robot_description_param = ParameterValue(
        Command([
            "xacro ", model_path, " prefix:=", LaunchConfiguration("prefix")
        ]),
        value_type=str
    )

    param_server = Node(
        package="rclcpp_components",
        executable="component_container",
        name="robot_description_server",
        parameters=[{"robot_description": robot_description_param}],
        output="screen"
    )

    return LaunchDescription([
        prefix_decl,
        generation_decl,
        param_server,
    ])
