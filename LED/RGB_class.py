import RPi.GPIO as GPIO

class RGB_LED:
        def __init__(self, red, green, blue):
                print('initializing rgb', red, green, blue)
                self.red_pin = red
                self.green_pin = green
                self.blue_pin = blue
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)
                GPIO.setup(red, GPIO.OUT)
                GPIO.setup(green, GPIO.OUT)
                GPIO.setup(blue, GPIO.OUT)

        def red(self):
                GPIO.output(self.red_pin,GPIO.HIGH)
                GPIO.output(self.green_pin,GPIO.LOW)
                GPIO.output(self.blue_pin,GPIO.LOW)

        def green(self):
                GPIO.output(self.red_pin,GPIO.LOW)
                GPIO.output(self.green_pin,GPIO.HIGH)
                GPIO.output(self.blue_pin,GPIO.LOW)

        def blue(self):
                GPIO.output(self.red_pin,GPIO.LOW)
                GPIO.output(self.green_pin,GPIO.LOW)
                GPIO.output(self.blue_pin,GPIO.HIGH)

        def yellow(self):
                GPIO.output(self.red_pin,GPIO.HIGH)
                GPIO.output(self.green_pin,GPIO.HIGH)
                GPIO.output(self.blue_pin,GPIO.LOW)

        def magenta(self):
                GPIO.output(self.red_pin,GPIO.HIGH)
                GPIO.output(self.green_pin,GPIO.LOW)
                GPIO.output(self.blue_pin,GPIO.HIGH)

        def cyan(self):
                GPIO.output(self.red_pin,GPIO.LOW)
                GPIO.output(self.green_pin,GPIO.HIGH)
                GPIO.output(self.blue_pin,GPIO.HIGH)

        def off(self):
                GPIO.output(self.red_pin,GPIO.LOW)
                GPIO.output(self.green_pin,GPIO.LOW)
                GPIO.output(self.blue_pin,GPIO.LOW)