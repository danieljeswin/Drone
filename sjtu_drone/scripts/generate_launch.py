#!/usr/bin/env python

import xml.etree.ElementTree as ET
from xml.dom import minidom


def prettify(elem):

    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def getXML():
    launch = ET.Element('launch')
    urdf = ET.SubElement(launch, 'arg')
    urdf.set('name', 'xacro_robot_file')
    urdf.set('value', '$(find sjtu_drone)/urdf/drone.urdf.xacro')

    num = input("Enter number of drones : ")

    for i in range(num):
        print "Drone " + str(i+1) + " :"
        drone_name = raw_input("Enter name of the drone :")

        group = ET.SubElement(launch, 'group')
        group.set('ns', drone_name)

        drone_name_arg = ET.SubElement(group, 'arg')
        drone_name_arg.set('name', 'name')
        drone_name_arg.set('value', drone_name)

        coords = raw_input("Enter starting coordinates (x,y) : ").split(",")
        x_arg = ET.SubElement(group, 'arg')
        x_arg.set('name', 'xloc')
        x_arg.set('value', coords[0])

        y_arg = ET.SubElement(group, 'arg')
        y_arg.set('name', 'yloc')
        y_arg.set('value', coords[1])

        z_arg = ET.SubElement(group, 'arg')
        z_arg.set('name', 'zloc')
        z_arg.set('value', '0')

        param = ET.SubElement(group, 'param')
        param.set('name', 'robot_description')
        param.set('command', "$(find xacro)/xacro '$(arg xacro_robot_file)' prefix:=$(arg name) xPos:=$(arg xloc) yPos:=$(arg yloc) zPos:=$(arg zloc)")

        node = ET.SubElement(group, 'node')
        node.set('name', 'spawn_urdf')
        node.set('pkg', 'gazebo_ros')
        node.set('type', 'spawn_model')
        node.set('args', '-param robot_description -urdf -model $(arg name) -z 0.5')

    return launch




if __name__ == "__main__":
    data = prettify(getXML())
    print data
    file = open("../launch/drone.launch", "w")
    file.write(data)
    file.close()

