
import RPi.GPIO as GPIO
import time
import sys

class servo:
    def __init__(self, pin):
        self.pin = pin
    def cleanup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
    def setupMotor(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        pass
    def disable(self):
        GPIO.cleanup()
    def rotate(self, angle):
        self.setupMotor()
        servoRun = GPIO.PWM(self.pin, 50)
        servoRun.start(0)
        try:
            while True:
                duty = angle/18+2
                servoRun.ChangeDutyCycle(duty)
                time.sleep(0.4)
                servoRun.ChangeDutyCycle(0)
                break
        finally:
            servoRun.stop()
            self.disable()
pin = int(sys.argv[1])
angle = int(sys.argv[2])

servo1 = servo(pin)
servo1.rotate(angle%180)

