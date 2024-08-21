import RPi.GPIO as GPIO

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