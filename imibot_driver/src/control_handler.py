import math

from chassis import Chassis


class ControlHandler:
    servo_min = 1000  # Min pulse length out of 4096
    servo_max = 4095  # Max pulse length out of 4096
    servo_scale = servo_max - servo_min

    def __init__(self):
        self.chassis = Chassis()

    def setDirection(self):
        x = math.cos(math.radians(self.angle))
        # print int(self.totalFreq), int(self.totalFreq - self.totalFreq * math.fabs(x))

        if x > 0:
            self.chassis.setLeftSpeed(int(self.totalFreq))
            self.chassis.setRightSpeed(int(self.totalFreq - self.totalFreq * x))
        elif x < 0:
            self.chassis.setRightSpeed(int(self.totalFreq))
            self.chassis.setLeftSpeed(int(self.totalFreq - self.totalFreq * math.fabs(x)))

    def move(self, msg):
        self.angle = msg.angle
        self.strength = msg.strength

        if self.strength == 0:
            self.chassis.stop()
        else:
            factor = self.strength / 100
            self.totalFreq = (self.servo_scale * factor) + self.servo_min

            if 350 <= self.angle <= 360 or 0 <= self.angle <= 10:
                self.chassis.turnRight()
                self.chassis.setTotalSpeed(int(self.totalFreq))
            elif 11 <= self.angle <= 169:
                self.chassis.forward()
                self.setDirection()
            elif 170 <= self.angle <= 190:
                self.chassis.turnLeft()
                self.chassis.setTotalSpeed(int(self.totalFreq))
            elif 191 <= self.angle <= 349:
                self.chassis.reverse()
                self.setDirection()