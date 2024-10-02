**Differential Drive Robot with SLAM and Autonomous Navigation**

This project implements a differential drive robot equipped with SLAM (Simultaneous Localization and Mapping) capabilities using gmapping. The robot creates a 2D map of its environment and saves it locally, which can then be used for localization through AMCL (Adaptive Monte Carlo Localization) and autonomous navigation using move_base.

Table of Contents
Project Overview
Features
Installation
Usage
Images
Contributing


Project Overview
The differential drive robot in this project performs:

Mapping: Uses gmapping to generate a 2D map of its environment.
Localization: Uses the generated map with AMCL for localization.
Navigation: Plans and follows paths using move_base to autonomously navigate the environment.
This project is designed for use in various indoor environments such as warehouses, greenhouses, or industrial settings, where autonomous mapping and navigation are essential.

Features
Gmapping for SLAM: Creates a real-time map of the environment.
AMCL Localization: Localizes the robot on a pre-existing map.
Move Base Navigation: Autonomously navigates to specified goals using path planning.
Real-time Visualization: Visualization of the robot, map, and path using Rviz.
Installation
Prerequisites
Ensure the following dependencies are installed:

ROS (Robot Operating System)
gmapping package
amcl package
move_base package
Rviz for visualization

Steps
Clone the repository:
bash
git clone https://github.com/yourusername/yourproject.git
Build the project:
cd yourproject
catkin_make

Source the workspace:

source devel/setup.bash
Mapping
To start mapping the environment, run:

roslaunch yourproject gmapping.launch
Save Map
Once the map is generated, you can save it locally:

bash
Copy code
rosrun map_server map_saver -f ~/your_map_name
Localization and Navigation
To localize and navigate using the saved map:

bash
Copy code
roslaunch yourproject amcl_navigation.launch
Rviz Visualization
To visualize the robot and environment in Rviz:

roslaunch yourproject rviz.launch

Images
Figure 1: Example of environment mapping using gmapping.

Figure 2: Robot navigating through the mapped environment using move_base.

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements.
Run 
map.launch (includes slam)
amcl.launch

docker run -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --privileged --runtime=runc -v /home/user/.Xauthority:/home/user/.Xauthority:ro  >

