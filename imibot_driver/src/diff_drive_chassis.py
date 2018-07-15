import RPi.GPIO as GPIO
import Adafruit_PCA9685


class DiffDriveChassis:

    def __init__(self):
        try:
            self.pwm = Adafruit_PCA9685.PCA9685()
            self.pwm.set_pwm_freq(60)
        except Exception:
            print('Pas de carte brancher en I2C')
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        self.stop()

    def stop(self):
        # print 'stop'
        GPIO.output(26, False)
        GPIO.output(13, False)
        GPIO.output(19, False)
        GPIO.output(6, False)

    def forward(self, tf=0.1):
        # print 'forward'
        GPIO.output(26, False)
        GPIO.output(13, False)
        GPIO.output(19, True)
        GPIO.output(6, True)
        # time.sleep(tf)

    def reverse(self, tf=0.1):
        # print 'reverse'
        GPIO.output(19, False)
        GPIO.output(6, False)
        GPIO.output(26, True)
        GPIO.output(13, True)
        # time.sleep(tf)

    def turnLeft(self, tf=0.1):
        # print 'left'
        GPIO.output(26, False)
        GPIO.output(6, False)
        GPIO.output(13, True)
        GPIO.output(19, True)
        # time.sleep(tf)

    def turnRight(self, tf=0.1):
        # print 'right'
        GPIO.output(13, False)
        GPIO.output(6, True)
        GPIO.output(19, False)
        GPIO.output(26, True)
        # time.sleep(tf)

    def setLeftSpeed(self, freq):
        try:
            self.pwm.set_pwm(0, 0, freq)
        except Exception:
            print('Pas de carte brancher en I2C')

    def setRightSpeed(self, freq):
        try:
            self.pwm.set_pwm(1, 0, freq)
        except Exception:
            print('Pas de carte brancher en I2C')

    def setTotalSpeed(self, freq):
        try:
            self.pwm.set_pwm(0, 0, freq)
            self.pwm.set_pwm(1, 0, freq)
        except Exception:
            print('Pas de carte brancher en I2C')
