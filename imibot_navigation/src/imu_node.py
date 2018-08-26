#!/usr/bin/env python
import rospy
from imu import IMU


def main():
    rospy.init_node('imibot_imu')
    IMU(rospy)
    rospy.spin()


if __name__ == '__main__':
    main()