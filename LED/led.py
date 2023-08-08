import RPi.GPIO as GPIO
import sys
ledPin = int(sys.argv[1])
ledStatus =  int(sys.argv[2])
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin, GPIO.OUT)
if ledStatus==1:
        GPIO.output(ledPin,GPIO.HIGH)
else:
        GPIO.output(ledPin, GPIO.LOW)

#to use run command: python3 LED/led.py ledPin ledStatus
