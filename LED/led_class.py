import RPi.GPIO as GPIO
import time
class LED:
        def __init__(self, pin):
                print('pin is', pin)
                self.pin = pin
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)
                GPIO.setup(pin, GPIO.OUT)
        def on(self):
                GPIO.output(self.pin,GPIO.HIGH)
        def off(self):
                GPIO.output(self.pin,GPIO.LOW)
        def blink(self):
                while True:
                        self.on()
                        time.sleep(1)
                        self.off()
                        time.sleep(1)