#!/usr/bin/env python
import rospy
from diff_drive_control_handler import DiffDriveControlHandler


def main():
    rospy.init_node('imibot_driver')
    DiffDriveControlHandler(rospy)
    rospy.spin()


if __name__ == '__main__':
    main()