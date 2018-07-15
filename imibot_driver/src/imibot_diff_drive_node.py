#!/usr/bin/env python
import rospy
from imibot_driver.msg import DiffSpeed
from diff_drive_control_handler import DiffDriveControlHandler


def main():
    diff_drive_control_handler = DiffDriveControlHandler()
    rospy.init_node('imibot_driver')
    rospy.Subscriber("robot_mg", DiffSpeed, diff_drive_control_handler.move)
    rospy.spin()


if __name__ == '__main__':
    main()