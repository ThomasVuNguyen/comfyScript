import RPi.GPIO as GPIO
import sys
import time

class avoidance_sensor:
    def __init__(self, shock):
        self.shock = shock
        
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.shock, GPIO.IN)
        
    def cleanup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.cleanup()
        
    def disable(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.shock, GPIO.OUT)
        time.sleep(0.01)
        GPIO.cleanup()
        
    def turnOn(self, state):
        print(state)
        self.setup()
        if(state==1):  
            while(GPIO.gpio_function(self.shock)==1):
                time.sleep(0.5)
                print(GPIO.input(self.shock))
        else:
            self.disable()
            exit(1)
        self.cleanup()
        exit(1)
        
shock = int(sys.argv[1])
state = int(sys.argv[2])

avoidance_sensor1 = avoidance_sensor(shock)
avoidance_sensor1.turnOn(state)