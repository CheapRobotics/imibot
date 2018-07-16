#!/usr/bin/env python
import rospy
from imibot_driver.msg import DiffSpeed
from speed_sensor import SpeedSensors


def main():
    speed_sensors = SpeedSensors()
    # publish
    rospy.spin()


if __name__ == '__main__':
    main()