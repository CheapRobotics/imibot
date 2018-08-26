import random
import time
from data_point import DataPoint
from i2clibraries.i2c_adxl345 import i2c_adxl345
from libhmc5883l import HMC5883L
from itg3200.ITG3200 import ITG3200


class SensorReader:
    """
    Reads data from accelerometer, gyroscope and compass
    """

    def __init__(self):
        self.__stopped = True
        self.accelerometer = i2c_adxl345(1)
        self.gyroscope = ITG3200()
        self.compass = HMC5883L(1)
        if self.compass.set_parameter('meas_mode', 'continuous'):
            print("Set measurement mode to continuous")
        else:
            exit("Could not set parameter, check I2C periph number")

    def read_accelerometer(self):
        accel_reading = DataPoint()
        accel_reading.sensor_type = 'acc'
        (accel_reading.x, accel_reading.y, accel_reading.z) = self.accelerometer.getAxes()
        return accel_reading

    def read_gyroscope(self):
        gyr_reading = DataPoint()
        gyr_reading.sensor_type = 'gyr'
        gyr = self.gyroscope.read_data()
        gyr_reading.x = gyr[0]
        gyr_reading.y = gyr[1]
        gyr_reading.z = gyr[2]
        return gyr_reading

    def read_compass(self):
        return self.compass.get_field_xyz()
