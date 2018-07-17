#!/usr/bin/env python
import rospy
from imibot_driver.msg import SensorsReadings
from speed_sensor import SpeedSensors


def __init__(self):
	self.speed_measures = SpeedSensors()

def main():
    speed_reports = SensorsReadings()

    pub = rospy.Publisher('imibot/speed_sensors', SensorsReadings, queue_size = 10)

    speed_reports.left_measured_travel = 0
    speed_reports.right_measured_travel = 0
    speed_reports.left_measured_vel = self.speed_measures.get
    speed_reports.right_measured_vel = self.speed_measures.

    pub.publish(speed_reports)
    sleep(0.05)
    rospy.spin()


if __name__ == '__main__':
    main()