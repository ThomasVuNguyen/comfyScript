import RPi.GPIO as GPIO
import time
import sys

reading_rate = 0.1
class sensor:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo 
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trig, GPIO.LOW)
    def cleanup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.trig, GPIO.LOW)
        GPIO.cleanup()
    def disable(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.IN)
        time.sleep(0.01)
        GPIO.cleanup()
    def read_distance(self, state):
        self.setup()
        while True:
            GPIO.output(self.trig, GPIO.HIGH)
            time.sleep(reading_rate)
            GPIO.output(self.trig, GPIO.LOW)
            if state==0:
                self.disable()
                exit(1)
            while GPIO.input(self.echo) ==0 and GPIO.gpio_function(self.trig)==0:
                pulse_start_time = time.time()
            while GPIO.input(self.echo) ==1 and GPIO.gpio_function(self.trig)==0:
                pulse_end_time = time.time()
            if GPIO.gpio_function(self.trig)==1:
                exit(1)
            pulse_duration = pulse_end_time - pulse_start_time
            distance_cm = round(pulse_duration * 17150, 2)
            print(distance_cm)

trig = int(sys.argv[1])
echo = int(sys.argv[2])
state = int(sys.argv[3])

distance1 = sensor(trig,echo)
distance1.read_distance(state)
