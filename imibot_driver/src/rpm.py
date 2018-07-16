#!/usr/bin/python

import RPi.GPIO as GPIO
import time

sensor_left = 27  # define the GPIO pin our sensor is attached to
sensor_right = 17  # define the GPIO pin our sensor is attached to

GPIO.setmode(GPIO.BCM)  # set GPIO numbering system to BCM
GPIO.setup(sensor_left, GPIO.IN)  # set our sensor pin to an input
GPIO.setup(sensor_right, GPIO.IN)  # set our sensor pin to an input

sample = 10  # how many half revolutions to time
count_left = 0
count_right = 0

start_left = 0
end_left = 0
start_right = 0
end_right = 0

pi = 3.1415926

wheel_diameter = 0.066
circ = wheel_diameter * pi


def set_left_start():
    global start_left
    start_left = time.time()


def set_left_end():
    global end_left
    end_left = time.time()


def set_right_start():
    global start_right
    start_right = time.time()


def set_right_end():
    global end_right
    end_right = time.time()


def get_left_rpm(c):
    global count_left  # declare the count variable global so we can edit it

    if not count_left:
        set_left_start()  # create start time

    count_left = count_left + 1  # increase counter by 1

    if count_left == sample:
        set_left_end()  # create end time
        delta = end_left - start_left  # time taken to do a half rotation in seconds
        delta = delta * 1000  # converted to ms

        ms_left_for_one_turn = 40 / sample * delta

        rpm_left = 60 / (ms_left_for_one_turn / 1000)

        mps_left = rpm_left * circ / 60

        print 'left RPM : ', rpm_left
        print 'left m/s : ', mps_left
        count_left = 0  # reset the count to 0


def get_right_rpm(c):
    global count_right  # declare the count variable global so we can edit it

    if not count_right:
        set_right_start()  # create start time

    count_right = count_right + 1  # increase counter by 1

    if count_right == sample:
        set_right_end()  # create end time
        delta = end_right - start_right  # time taken to do a half rotation in seconds
        delta = delta * 1000  # converted to ms

        ms_right_for_one_turn = 40 / sample * delta

        rpm_right = 60 / (ms_right_for_one_turn / 1000)

        mps_right = rpm_right * circ / 60

        print 'right RPM : ', rpm_right
        print 'right m/s : ', mps_right
        count_right = 0  # reset the count to 0


GPIO.add_event_detect(sensor_left, GPIO.RISING, callback=get_left_rpm)
GPIO.add_event_detect(sensor_right, GPIO.RISING, callback=get_right_rpm)  # execute the get_rpm function when a HIGH signal is detected

try:
    while True:  # create an infinte loop to keep the script running
        time.sleep(0.1)
except KeyboardInterrupt:
    print "  Quit"
    GPIO.cleanup()
