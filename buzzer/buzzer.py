import RPi.GPIO as GPIO
import sys
import time

class Buzzer:
    def __init__(self, pin):
        self.pin = pin
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)
    def cleanup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.cleanup()
    def disable(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN)
        time.sleep(0.01)
        GPIO.cleanup()
    def turnOn(self, state):
        self.setup()
        if(state==1):  
            while(GPIO.gpio_function(self.pin)==0):
                GPIO.output(self.pin, GPIO.HIGH)
        else:
            self.disable()
            exit(1)
        self.cleanup()
        exit(1)
        
pin = int(sys.argv[1])
state = int(sys.argv[2])

Buzzer1 = Buzzer(pin)
Buzzer1.turnOn(state)