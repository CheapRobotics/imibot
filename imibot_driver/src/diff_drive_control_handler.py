#!/usr/bin/env python
import math
import rospy

from chassis import Chassis
from imibot_driver.msg import SensorsReadings
from speed_sensor import SpeedSensors


class DiffDriveControlHandler:
    servo_min = 1000  # Min pulse length out of 4096
    servo_max = 4095  # Max pulse length out of 4096
    servo_scale = servo_max - servo_min

    def __init__(self):
        self.chassis = Chassis()
        self.speed_measures = SpeedSensors()

        pub = rospy.Publisher('imibot/speed_sensors', SensorsReadings, queue_size = 10)
        print 'init bot'

        while True:
            self.publishSensors()
            time.sleep(0.5)

    def setSpeed(self):
        self.chassis.setLeftSpeed(int(self.leftFreq))
        self.chassis.setRightSpeed(int(self.rightFreq))

    def publishSensors(self):
        self.speed_msg = SensorsReadings()

        self.speed_msg.left_measured_travel = self.speed_measures.get_left_travel()
        self.speed_msg.right_measured_travel = self.speed_measures.get_right_travel()
        self.speed_msg.left_measured_vel = self.speed_measures.get_left_rpm()
        self.speed_msg.right_measured_vel = self.speed_measures.get_right_rpm()

        pub.publish(self.speed_msg)

    def move(self, msg):
        self.left_speed = msg.left_speed
        self.right_speed = msg.right_speed
        print self.left_speed, self.right_speed

        if self.left_speed == 0 and self.right_speed == 0 :
            self.chassis.stop()
            print 'stop'
        else:
            self.leftFreq = (self.servo_scale * (abs(self.left_speed) / 100)) + self.servo_min
            self.rightFreq = (self.servo_scale * (abs(self.right_speed) / 100)) + self.servo_min

            if self.left_speed > 0 and self.right_speed > 0:
                self.speed_measures.set_left_direction(1)
                self.speed_measures.set_right_direction(1)
                print 'forward'
                self.chassis.forward()
                self.setSpeed()
            elif self.left_speed < 0 and self.right_speed > 0:
                self.speed_measures.set_left_direction(0)
                self.speed_measures.set_right_direction(1)
                print 'left'
                self.chassis.turnLeft()
                self.setSpeed()
            elif self.left_speed > 0 and self.right_speed < 0:
                self.speed_measures.set_left_direction(1)
                self.speed_measures.set_right_direction(0)
                print 'right'
                self.chassis.turnRight()
                self.setSpeed()
            elif self.left_speed < 0 and self.right_speed < 0:
                self.speed_measures.set_left_direction(0)
                self.speed_measures.set_right_direction(0)
                print 'reverse'
                self.chassis.reverse()
                self.setSpeed()
