from gpiozero import AngularServo
import RPi.GPIO as GPIO
from time import sleep
import sys
servoPin = int(sys.argv[1])
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(0)

def SetAngle(angle):
    duty = angle/18+2
    GPIO.output(servoPin,True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPin, False)
    pwm.ChangeDutyCycle(0)

SetAngle(int(sys.argv[2]))

#to use run command: python3 angle.py pinNum servoAngle