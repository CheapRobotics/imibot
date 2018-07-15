#!/usr/bin/env python
import rospy
from imibot_driver.msg import StickControl
from control_handler import ControlHandler


def main():
    controls_handler = ControlHandler()
    rospy.init_node('imibot_move')
    rospy.Subscriber("imibot/stick_control", StickControl, controls_handler.move)
    rospy.spin()


if __name__ == '__main__':
    main()
