#!/usr/bin/env python
import rospy
from imibot_driver.msg import DiffSpeed
from diff_drive_control_handler import DiffDriveControlHandler


def main():
    # Init ROS
    rospy.init_node('imibot_driver')
    
    # Init Driver of robot
    diff_drive_control_handler = DiffDriveControlHandler(rospy)
    
    # Loop over...
    rospy.spin()


if __name__ == '__main__':
    main()
