# robotont_description

![ROS 2](https://img.shields.io/badge/ROS2%20-Jazzy-blue.svg) [![CI](https://github.com/robotont/robotont_description/actions/workflows/industrial_ci_action.yml/badge.svg)](https://github.com/robotont/robotont_description/actions/workflows/industrial_ci_action.yml) ![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)

## **Overview**
Description package for robotont.
## **Table of Contents**
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Building the Package](#building-the-package)
- [Launch Files](#launch-files)
- [License](#license)

---

## **Installation**

### **1. Clone the Repository**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>/src
git clone https://github.com/robotont/robotont_description.git
```

## **Dependencies**
### **1. List of dependencies**
1.1. rviz<br>
1.2. urdf<br>
1.3. xacro
### **2. Install dependencies**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>
rosdep install --from-paths src --ignore-src -r -y
```

## **Building the package**
```bash
cd ~/<YOUR_WORKSPACE_NAME_HERE>
colcon build --packages-select robotont_description
```

## **Launch files**
### **1. Source workspace**
```bash
source ~/<YOUR_WORKSPACE_NAME_HERE>/install/setup.bash
```
### **2. Available launch files**
Supported parameters:

| Name         | Default | Description                                                                             |
|--------------|---------|-----------------------------------------------------------------------------------------|
| `generation` | `3`     | Specify the generation of robotont model that is to be loaded (2.1 and 3 are supported) |
#### 2.1. Display simulated robot
Displays the robot's model in rviz, starts joint_state_publisher and robot_state_publisher
```bash
#### Load generation 3 model
ros2 launch robotont_description display_robot_model.launch.py
```
Displays the robot's model in rviz, with different frame colors (blue, light_blue, purple, yellow, green, dark_green, black, gray):
```bash
#### Load generation 3 model with specific frame color
ros2 launch robotont_description display_robot_model.launch.py primary_color:=light_blue
```

Supported formats for `primary_color`:
- color name:      primary_color:=lightblue 
- RGBA (0..1):     primary_color:="0.16 0.65 0.98 1.0"
- RGBA (0..255):   primary_color:="41 166 250 255"
- HEX:             primary_color:="#29a6faff" 

```bash
#### Load generation 2.1 model
ros2 launch robotont_description display_robot_model.launch.py generation:=2.1
```
#### 2.2. Description
Starts joint_state_publisher and robot_state_publisher, robot model is published on /robot_description topic.
```bash
ros2 launch robotont_description upload_description.launch.py
```

## **License**
This project is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for more information.
