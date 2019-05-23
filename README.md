# Drone
My project to transform the Parrot ArDrone to spawn multiple drones in a single simulation and control them seperately


## Getting Started
Simply clone the repo, compile and make sure you've installed the prerequisites and you're all ready to go.

### Prerequisites
1. ROS Kinetic
2. Gazebo7 - have not tested for compatibility with later versions of Gazebo.

### Running
Clone the repo into a catkin_workspace.
Create workspace using the following commands.

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
```

Once cloned compile using the following commands

```
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

To launch the simulation launch the main.launch file using the following command

```
roslaunch sjtu_drone main.launch
```

### Description
The sjtu_drone package is the ROS implementation of Parrot ArDrone Simulation. I have modified the package to spawn multiple drones simultaneously.

1. I have created URDF files for the simulation as they work better with ROS.
2. The drone.launch file contains the code to spawn multiple drones each controlled seperately. As modifying the launch file to include more drones would be arduous, I have created a python script generate_launch.py to automatically get information from user and create it.

If adding more drones ensure that your system enough RAM and GPU to support running the resulting simulation. 



## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details
