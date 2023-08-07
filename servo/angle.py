from gpiozero import AngularServo
from time import sleep

servo = AngularServo(4, min_angle=0, max_angle=180)
angle = 90
servo.angle=angle
