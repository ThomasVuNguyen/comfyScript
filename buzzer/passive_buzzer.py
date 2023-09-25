import RPi.GPIO as GPIO
import sys
import time

class Passize_buzzer:
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
        print(state)
        self.setup()
        if(state==1):  
            while(GPIO.gpio_function(self.pin)==0):
                time.sleep(0.5)
                GPIO.output(self.pin, GPIO.HIGH)
                print("high")
                time.sleep(0.5)
                GPIO.output(self.pin, GPIO.LOW)
                print("low")
        else:
            self.disable()
            exit(1)
        self.cleanup()
        exit(1)
        
pin = int(sys.argv[1])
state = int(sys.argv[2])

Buzzer1 =   Passize_buzzer(pin)
Buzzer1.turnOn(state)