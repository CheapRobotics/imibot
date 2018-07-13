#!/usr/bin/env python
from time import sleep

import rospy
from imibot.msg import StickControl


def main():
    rospy.init_node('imibot_move_sender')

    pub = rospy.Publisher('imibot/stick_control', StickControl, queue_size=10)

    ld = StickControl()
    ld.strength = 0
    ld.angle = 0
    pub.publish(ld)
    #rospy.spin()


if __name__ == '__main__':
    main()

