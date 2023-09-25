import RPi.GPIO as GPIO
import sys
import time

class DCsensor:
    def __init__(self, pin1, pin2, pin3, pin4):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pin3, GPIO.OUT)
        GPIO.setup(self.pin4, GPIO.OUT)
        
    def cleanup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.cleanup()
        
    def disable(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin1, GPIO.IN)
        GPIO.setup(self.pin2, GPIO.IN)
        GPIO.setup(self.pin2, GPIO.IN)
        GPIO.setup(self.pin2, GPIO.IN)
        time.sleep(0.01)
        GPIO.cleanup()
        
    def turnOn(self, state1, state2, state3, state4):
        self.setup()
        while(GPIO.gpio_function(self.pin1)==0):
            time.sleep(0.2)
            if(state1 ==1):
                GPIO.output(self.pin1,GPIO.HIGH)
            else:
                GPIO.output(self.pin1,GPIO.LOW)
                
            if(state2 ==1):
                GPIO.output(self.pin2,GPIO.HIGH)
            else:
                GPIO.output(self.pin2,GPIO.LOW)
    
            if(state3 ==1):
                GPIO.output(self.pin3,GPIO.HIGH)
            else:
                GPIO.output(self.pin3,GPIO.LOW)
                
            if(state4 ==1):
                GPIO.output(self.pin4,GPIO.HIGH)
            else:
                GPIO.output(self.pin4,GPIO.LOW)
                
        self.disable()
        self.cleanup()
        exit(1)

        
pin1 = int(sys.argv[1])
pin2 = int(sys.argv[2])
pin3 = int(sys.argv[3])
pin4 = int(sys.argv[4])
state1 = int(sys.argv[5])
state2 = int(sys.argv[6])
state3 = int(sys.argv[7])
state4 = int(sys.argv[8])

DCsensor1 = DCsensor(pin1,pin2,pin3,pin4)
DCsensor1.turnOn(state1, state2, state3, state4)