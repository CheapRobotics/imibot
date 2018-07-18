#!/usr/bin/python
# coding=utf-8

import RPi.GPIO as GPIO
import time
import rospy

from imibot_driver.msg import SensorsReadings
from threading import Thread


class SpeedSensors(Thread):
    sensor_left = 27  # define the GPIO pin our sensor is attached to
    sensor_right = 17  # define the GPIO pin our sensor is attached to

    sample = 10  # how many half revolutions to time
    total_ticks = 40
    count_left = 0
    count_right = 0

    start_left = 0
    end_left = 0
    start_right = 0
    end_right = 0

    left_travel = 0
    right_travel = 0
    mps_left = 0
    mps_right = 0

    pi = 3.1415926

    wheel_diameter = 0.066
    circ = wheel_diameter * pi

    left_direction = 1
    right_direction = 1

    def __init__(self):
        self.speed_msg = SensorsReadings()
        rospy.init_node('imibot_driver')
        self.pub = rospy.Publisher('imibot/speed_sensors', SensorsReadings, queue_size=10)

        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):

        GPIO.setmode(GPIO.BCM)  # set GPIO numbering system to BCM
        GPIO.setup(self.sensor_left, GPIO.IN)  # set our sensor pin to an input
        GPIO.setup(self.sensor_right, GPIO.IN)  # set our sensor pin to an input
        GPIO.add_event_detect(self.sensor_left, GPIO.RISING, callback=self.measure_left)
        GPIO.add_event_detect(self.sensor_right, GPIO.RISING, callback=self.measure_right)

        while True:
            self.publishSensors()
            time.sleep(0.1)

    def publishSensors(self):
        self.speed_msg.left_measured_travel = self.left_travel
        self.speed_msg.right_measured_travel = self.right_travel
        self.speed_msg.left_measured_vel = self.mps_left
        self.speed_msg.right_measured_vel = self.mps_right

        self.pub.publish(self.speed_msg)

    def set_left_start(self):
        self.start_left = time.time()

    def set_left_end(self):
        self.end_left = time.time()

    def set_right_start(self):
        self.start_right = time.time()

    def set_right_end(self):
        self.end_right = time.time()

    def set_left_direction(self, direction):
        self.left_direction = direction
        if direction == 1:
            print 'L : Forward'
        else:
            print 'L : Reverse'

    def set_right_direction(self, direction):
        self.right_direction = direction
        if direction == 1:
            print 'R : Forward'
        else:
            print 'R : Reverse'

    def stop_left_speed(self):
        self.mps_left = 0

    def stop_right_speed(self):
        self.mps_right = 0

    def measure_left(self, c):
        if not self.count_left:
            self.set_left_start()  # create start time

        if (time.time() - self.start_left) > 100:
            self.count_left += 1  # increase counter by 1
            if self.left_direction == 1:
                self.left_travel += self.circ / self.total_ticks
            elif self.left_direction == 0:
                self.left_travel -= self.circ / self.total_ticks

        if self.count_left == self.sample:
            self.set_left_end()  # create end time
            delta = self.end_left - self.start_left  # time taken to do a half rotation in seconds
            delta *= 1000  # converted to ms

            ms_left_for_one_turn = self.total_ticks / self.sample * delta

            rpm_left = 60 / (ms_left_for_one_turn / 1000)

            self.mps_left = rpm_left * self.circ / 60

            print 'left RPM : ', self.rpm_left
            print 'distance parcourue à gauche : ', self.left_travel
            self.count_left = 0  # reset the count to 0

    def measure_right(self, c):
        if not self.count_right:
            self.set_right_start()  # create start time

        if (time.time() - self.start_right) > 100:
            self.count_right += 1  # increase counter by 1
            if self.right_direction == 1:
                self.right_travel += self.circ / self.total_ticks
            elif self.right_direction == 0:
                self.right_travel -= self.circ / self.total_ticks

        if self.count_right == self.sample:
            self.set_right_end()  # create end time
            delta = self.end_right - self.start_right  # time taken to do a half rotation in seconds
            delta *= 1000  # converted to ms

            ms_right_for_one_turn = total_ticks / self.sample * delta

            rpm_right = 60 / (ms_right_for_one_turn / 1000)

            self.mps_right = rpm_right * self.circ / 60

            print 'right RPM : ', self.rpm_right
            print 'distance parcourue à droite : ', self.right_travel
            self.count_right = 0  # reset the count to 0
