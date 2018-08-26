#!/usr/bin/python
# coding=utf-8

from sensor_reader import SensorReader
import time

sensor_reader = SensorReader()
while (True):
    print(sensor_reader.read_compass())
    print(sensor_reader.read_accelerometer())
    print(sensor_reader.read_gyroscope())
    time.sleep(1)
