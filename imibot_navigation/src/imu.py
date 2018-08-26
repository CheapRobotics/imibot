#!/usr/bin/python
# coding=utf-8

from sensor_reader import SensorReader
import time
import rospy
from sensor_msgs.msg import Imu
from threading import Thread


class IMU(Thread):

    def __init__(self, rospy):
        self.seq = 0
        self.imu_msg = Imu()
        self.imu_msg.orientation_covariance[0] = -1
        self.imu_msg.angular_velocity_covariance[0] = -1
        self.imu_msg.linear_acceleration_covariance[0] = -1
        self.pub = rospy.Publisher('imibot/imu_sensor', Imu, queue_size=50)
        self.sensor_reader = SensorReader()

        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            self.publishSensorsValues()
            time.sleep(0.1)

    def publishSensorsValues(self):
        compass = self.sensor_reader.read_compass()
        accel = self.sensor_reader.read_accelerometer()
        gyro = self.sensor_reader.read_gyroscope()

        print(self.sensor_reader.read_compass())
        print(self.sensor_reader.read_accelerometer())
        print(self.sensor_reader.read_gyroscope())

        self.imu_msg.linear_acceleration.x = accel.x
        self.imu_msg.linear_acceleration.y = accel.y
        self.imu_msg.linear_acceleration.z = accel.z

        self.imu_msg.angular_velocity.x = gyro.x
        self.imu_msg.angular_velocity.y = gyro.y
        self.imu_msg.angular_velocity.z = gyro.z

        # self.imu_msg.orientation.x = compass.x
        # self.imu_msg.orientation.y = compass.y
        # self.imu_msg.orientation.z = compass.z
        # self.imu_msg.header.seq = self.seq

        self.imu_msg.header.stamp = rospy.Time.now()
        self.imu_msg.header.frame_id = "base_link"

        self.seq += 1
        self.pub.publish(self.imu_msg)
