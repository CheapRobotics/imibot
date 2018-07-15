#!/usr/bin/env python
import math

from chassis import Chassis


class DiffDriveControlHandler:
    servo_min = 1000  # Min pulse length out of 4096
    servo_max = 4095  # Max pulse length out of 4096
    servo_scale = servo_max - servo_min

    def __init__(self):
        self.chassis = Chassis()

    def setSpeed(self):
        self.chassis.setLeftSpeed(int(self.leftFreq))
        self.chassis.setRightSpeed(int(self.rightFreq))

    def move(self, msg):
        self.left_speed = msg.left_speed
        self.right_speed = msg.right_speed

        if self.left_speed == 0 and self.right_speed == 0 :
            self.chassis.stop()
        else:
            self.leftFreq = (self.servo_scale * (self.left_speed / 100)) + self.servo_min
            self.rightFreq = (self.servo_scale * (self.right_speed / 100)) + self.servo_min

            if self.left_speed > 0 and self.right_speed > 0:
                self.chassis.forward()
                self.setSpeed()
            elif self.left_speed < 0 and self.right_speed > 0:
                self.chassis.turnLeft()
                self.setSpeed()
            elif self.left_speed > 0 and self.right_speed < 0:
                self.chassis.turnRight()
                self.setSpeed()
            elif self.left_speed < 0 and self.right_speed < 0:
                self.chassis.reverse()
                self.setSpeed()
