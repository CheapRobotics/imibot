import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time

try:
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(500)
    pwm.set_pwm(0, 0, 4000)
    pwm.set_pwm(1, 0, 4000)
except Exception:
    print('Pas de carte branchée en I2C')

GPIO.setmode(GPIO.BCM)

GPIO.output(26, False)
GPIO.output(13, False)
GPIO.output(19, True)
GPIO.output(6, True)

time.sleep(3)

GPIO.output(26, False)
GPIO.output(13, False)
GPIO.output(19, False)
GPIO.output(6, False)
