import RPi.GPIO as GPIO
import sys
import time

try:
	from adafruit_motorkit import MotorKit
except ImportError as e:
	print('error importing adafruit_motorkit, you might want to install it with pip')
kit = MotorKit()

motor_list = {
    '1': kit.motor1, 
    '2': kit.motor2, 
    '3': kit.motor3,
    '4': kit.motor4,
    }
    
class i2c_motor:
    def __init__(self, id):
        self.id = id
    
    def spin(self, speed):
        state = float(speed)
        motor_list[self.id].throttle = state
