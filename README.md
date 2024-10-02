# **Differential Drive Robot with SLAM and Autonomous Navigation**

This project implements a differential drive robot equipped with SLAM (Simultaneous Localization and Mapping) capabilities using gmapping. The robot creates a 2D map of its environment and saves it locally, which can then be used for localization through AMCL (Adaptive Monte Carlo Localization) and autonomous navigation using move_base.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Images](#images)
- [Contributing](#contributing)


## Project Overview

The differential drive robot in this project performs:

- **Mapping**: Uses gmapping to generate a 2D map of its environment.
- **Localization**: Uses the generated map with AMCL for localization.
- **Navigation**: Plans and follows paths using `move_base` to autonomously navigate the environment.

This project is designed for use in various indoor environments such as warehouses, greenhouses, or industrial settings, where autonomous mapping and navigation are essential.

## Features

- **Gmapping for SLAM**: Creates a real-time map of the environment.
- **AMCL Localization**: Localizes the robot on a pre-existing map.
- **Move Base Navigation**: Autonomously navigates to specified goals using path planning.
- **Real-time Visualization**: Visualizes the robot, map, and path using Rviz.

## Installation

### Prerequisites

Ensure the following dependencies are installed:

- ROS Noetic
- `gmapping` package:
  ```
  sudo apt-get install ros-noetic-slam-gmapping
  ```
- `amcl` package: 
  ```
  sudo apt-get install ros-noetic-amcl
  sudo apt-get install ros-noetic-dwa-local-planner
  ```
- `move_base` package:
   ```
  sudo apt-get install ros-noetic-move-base
  ```
- `teleop-twis-keyboard` package: 
  ```
  sudo apt-get install ros-noetic-teleop-twist-keyboard
  ```
- `map-server` package: 
  ```
  sudo apt-get install ros-noetic-map-server
  ```

### Steps

1. Clone the repository:
    ```
    git clone https://github.com/S-Sidharthan/ROS-slam-amcl-autonomous-robot.git
    ```

2. Build the project:
    ```
    cd ROS-slam-amcl-autonomous-robot
    catkin_make
    ```

3. Source the workspace:
    ```
    source devel/setup.bash
    ```

## Usage

### Mapping

To start mapping the environment, run:

```
roslaunch robot_gazebo robot_gazebo.launch
roslaunch yourproject gmapping.launch
rosrun teleop_twist_keyboard teleop_twist_keyboard.py

```
### Localization and Navigation
To localize and navigate using the saved map :
(Note: change the map path in amcl.launch)
```
roslaunch diff_wheeled_robot amcl.launch 
```

## Images
Figure 1: Environment mapping. 
![Screenshot from 2024-10-02 19-32-07](https://github.com/user-attachments/assets/316ba7cc-bcc6-41a9-968e-b2746fdf55a0)


Figure 2: Robot navigating through the mapped environment using move_base. 
![Screenshot from 2024-10-02 19-48-09](https://github.com/user-attachments/assets/391d2ab6-c1b7-4ee0-b684-f72c24443ad8)

## Video Demo

Watch a demo of the robot in action on YouTube:

[![Watch the video](https://img.youtube.com/vi/YOUR_VIDEO_ID/maxresdefault.jpg)](https://youtu.be/YOUR_VIDEO_ID)

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

