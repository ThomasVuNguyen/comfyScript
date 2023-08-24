import RPi.GPIO as GPIO
import time
import os
import sys

class Stepper:
        def __init__(self, pin1, pin2, pin3, pin4):
            self.pin1 = pin1
            self.pin2 = pin2
            self.pin3 = pin3
            self.pin4 = pin4
            self.sleep = 0.002
            self.step = 4096
            self.sequence = [[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1],]
            self.pinList = [pin1, pin2, pin3, pin4]
        def cleanup(self):
            GPIO.setmode(GPIO.BCM)
            for pin in self.pinList:
                GPIO.output(pin, GPIO.LOW)
            GPIO.cleanup()
        def setupMotor(self):
            GPIO.setmode(GPIO.BCM)
            GPIO.setup( self.pin1, GPIO.OUT)
            GPIO.setup( self.pin2, GPIO.OUT)
            GPIO.setup( self.pin3, GPIO.OUT)
            GPIO.setup( self.pin4, GPIO.OUT)
            GPIO.output( self.pin1, GPIO.LOW)
            GPIO.output( self.pin2, GPIO.LOW)
            GPIO.output( self.pin3, GPIO.LOW)
            GPIO.output( self.pin4, GPIO.LOW)
            
        def disable(self):
            GPIO.setmode(GPIO.BCM)
            for  pin in self.pinList:
                GPIO.setup( self.pin1, GPIO.IN)
                time.sleep(0.1)
            GPIO.cleanup()
            
        def rotate(self, direction): #direction is 1 or 0 - clickwise or counter clockwise
            self.setupMotor()
            step_counter = 0
            i = 0
            while True:
                for i in range(self.step):
                    for pin in range(0, len(self.pinList)):
                        GPIO.output(self.pinList[pin], self.sequence[step_counter][pin])
                    if direction == 1 and GPIO.gpio_function(self.pin1)==0:
                        step_counter = (step_counter - 1) % 4
                    elif direction == 0 and GPIO.gpio_function(self.pin1)==0:
                        step_counter = (step_counter +1) % 4
                    elif GPIO.gpio_function(self.pin1)==1 or KeyboardInterrupt:
                        GPIO.setmode(GPIO.BCM)
                        print("broken")
                        exit(1)
                        break
                    else:
                        print("wrong direction input")
                        self.cleanup()
                        exit(1)
                    time.sleep(self.sleep)
        def testPin(self):
            while True:
                self.setupMotor()
                GPIO.output(self.pin2, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(self.pin2, GPIO.LOW)
                time.sleep(1)
                
pin1 = int(sys.argv[1])
pin2 = int(sys.argv[2])
pin3 = int(sys.argv[3])
pin4 = int(sys.argv[4])
direction = int(sys.argv[5])

Stepper1 = Stepper(pin1,pin2,pin3,pin4) #example: 27,22,10,9
Stepper1.disable()
Stepper1.rotate(direction)

