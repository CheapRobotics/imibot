# IMIBot

School Project - Autonomous robot powered by ROS.
Components are pretty cheap and you can buy everything online for approximatively 150-300 $ :

* Raspberry Pi 3
* Car Chassis Kit with chassis and 4 motors
* PCA9685 (PWM Extension card)
* L298N (H Bridge for motor control)
* Infrared opto-sensor x 2 (for reading the coded wheels on front motors) 
* Kinect, Xition or other stereo camera

## Install ROS on Pi and laptop

* Install Ubuntu 16.04 on Pi
* Follow [this link](https://www.intorobotics.com/how-to-install-ros-kinetic-on-raspberry-pi-3-ubuntu-mate/)

## Clone the repo and build code

> `cd ~/catkin_ws/src`

> `git clone https://github.com/CheapRobotics/imibot.git`

> `cd imibot`

> `./setup.sh`

> `sudo raspi-config` and enable i2c in "Interfacing options"

> `pip install Adafruit_PCA9685`

imibot_base ***might not build*** successfully on Pi with Ubuntu. In this case, you can just remove it for building.

> `cd ~/catkin_ws && catkin_make`

## Launch stacks

> `roslaunch imibot_launcher desktop.launch` on laptop

> `roslaunch imibot_launcher robot.launch` on pi

## Map Room

> `rosrun gmapping slam_gmapping scan:=depth_scan`