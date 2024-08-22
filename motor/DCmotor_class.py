import RPi.GPIO as GPIO
import sys
import time

class DC_motor:
    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin1, GPIO.IN)
        GPIO.setup(self.pin2, GPIO.IN)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.output(self.pin1,GPIO.LOW)
        GPIO.output(self.pin1,GPIO.LOW)

    def cleanup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.cleanup()
        
    def disable(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin1, GPIO.IN)
        GPIO.setup(self.pin2, GPIO.IN)
        GPIO.cleanup()
    
    def rotate(self):
        while True:
            GPIO.output(self.pin1,GPIO.HIGH)
            GPIO.output(self.pin2,GPIO.LOW)
    
    def reverse(self):
        while True:
            GPIO.output(self.pin1,GPIO.LOW)
            GPIO.output(self.pin2,GPIO.HIGH)
    
    def stop(self):
        while True:
            GPIO.output(self.pin1,GPIO.LOW)
            GPIO.output(self.pin2,GPIO.LOW)
        
    def turnOn(self, state1, state2):
        self.setup()
        while True:
            if GPIO.gpio_function(self.pin1)==0:
                if state1 ==1 and state2 ==1:
                    GPIO.output(self.pin1,GPIO.HIGH)
                    GPIO.output(self.pin2,GPIO.HIGH)
                    exit(1)
                elif state1 ==1 and state2 == 0:
                    GPIO.output(self.pin1,GPIO.HIGH)
                    GPIO.output(self.pin2,GPIO.LOW)
                    exit(1)
                elif state1 ==0 and state2 == 1:
                    GPIO.output(self.pin1,GPIO.LOW)
                    GPIO.output(self.pin2,GPIO.HIGH)
                    exit(1)
                elif state1 ==0 and state2 == 0:
                    GPIO.output(self.pin1,GPIO.LOW)
                    GPIO.output(self.pin2,GPIO.LOW)
                    exit(1)
                else:
                    print("wrong state values - keep it 1 or 0")
                    exit(1)
            else:
                print("finished")
                self.disable()
                self.cleanup()
                exit(1)
                