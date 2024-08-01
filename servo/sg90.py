#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys

class Servo:
    def __init__(self, pin):
        self.pin = pin
        self.setup_motor()

    def setup_motor(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo_pwm = GPIO.PWM(self.pin, 50)  # 50Hz frequency
        self.servo_pwm.start(0)

    def cleanup(self):
        self.servo_pwm.stop()
        GPIO.cleanup()

    def rotate(self, angle):
        if angle < 0 or angle > 180:
            print("Angle must be between 0 and 180 degrees")
            return

        duty = self.angle_to_duty_cycle(angle)
        self.servo_pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)
        self.servo_pwm.ChangeDutyCycle(0)  # Stop sending signal

    def angle_to_duty_cycle(self, angle):
        return 2 + (angle / 18.0)

    def __del__(self):
        self.cleanup()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 servo.py <pin> <angle>")
        sys.exit(1)

    pin = int(sys.argv[1])
    angle = int(sys.argv[2])

    servo = Servo(pin)
    servo.rotate(angle)
