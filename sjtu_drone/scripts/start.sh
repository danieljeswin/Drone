#!/bin/sh
python generate_launch.py
roslaunch sjtu_drone launch_world.launch
roslaunch sjtu_drone drone.launch