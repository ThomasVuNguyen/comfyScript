# comfyScript
A scripting language to control Raspberry Pi with comfyPi
<div id="header" align="center">
  <img src="assets/icon.png" width="100"/>
</div>
<div id="badges" align="center">
  <a href="https://www.linkedin.com/in/tung-thomas-nguyen-9b010317b">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge"/>
  </a>
  <a href="https://www.youtube.com/@thomasthemaker">
    <img src="https://img.shields.io/badge/-Raspberry Pi-C51A4A?style=for-the-badge&logo=Raspberry-Pi" alt="Raspberry Pi Badge"/>
  </a>
    <a href="https://comfystudio.tech">
    <img src="https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Bash Shell Script Badge"/>
  </a>
</div>

**`A more elegant approach to Raspberry Pi`**

## Single-color LED
<div id="header" style="float: left;" >
  <img src="assets/led.png" width="40"/>
</div>

```
Usage:
python3 comfyScript/LED/led.py [ledPin] [ledStatus]
  where:
    ledPin: LED power pin (BCM pinout)
    ledStatus: 1/0 or GPIO.HIGH/GPIO.LOW
```

## RGB LED
<div id="header" style="float: left;" >
  <img src="assets/RGBLED.png" width="40"/>
</div>

```
Usage:
python3 comfyScript/LED/RGB_led.py [redPin] [greenPin] [bluePin] [redStatus][greenStatus] [blueStatus]
  where:
    redPin, greenPin & bluePin: pins for red, green & blue terminals (BCM pinout)
    redStatus, greenStatus, blueStatus: 1/0 or GPIO.HIGH/GPIO.LOW
```

## Servo motor
<div id="header" style="float: left;" >
  <img src="assets/servo.png" width="40"/>
</div>

```
Usage:
python3 comfyScript/servo/angle.py [controlPin] [angle]
  where:
    controlPin: pinout to control servo PWM (BCM layout)
    angle: desired angle (0-180 or 0-360)
```

## DHT (3 pins)
<div id="header" style="float: left;" >
  <img src="assets/dht11.png" width="40"/>
</div>

```
Usage:
python3 comfyScript/DHT/dht_temp.py [sensor type] [pinout]   -> temperature (C)
python3 comfyScript/DHT/dht_humid.py [sensor type] [pinout]   -> relative humidity
  where:
    sensor type: 11,22, or 2302
    pinout: pinout to read sensor
```

## Stepper Motor 
<div id="header" style="float: left;" >
  <img src="assets/stepper-motor.png" width="40"/>
</div>

```
Usage:
python3 comfyScript/stepper/stepper.py [pin1] [pin2] [pin3] [pin4] [direction]

  where:
    pin1 to pin4: pins 1 -> 4 (ULN2003 driver board)
    direction: -1 for clockwise, 0 for stop & 1 for counter clockwise

future plan: option for full, one-and-a-half, and one step control
note: currently, there is a 0.1 second delay between direction changes - to be improved
```

## Distance Sensor (HC-SR04 and infared shock sensor)
<div id="header" style="float: left;" >
  <img src="assets/distance-sensor.png" width="40"/>
</div>

```
Usage:
python3 comfyScript/distance_sensor/HC-SR04.py [trig] [echo] [state]
python3 comfyScript/avoidance_sensor/avoidance_sensor.py [pin] [state]

  where:
    HC-SR04.py -> ultrasound sensor & avoidance_sensor.py for infared sensor
    pin: avoidance sensor pun
    trig & echo: trigger & echo pins
    state: 1 - running & 0 - disable (used to enable sensor from different SSH clients)

future plan: option for distance in m, inches & ft (currently in cm)
note: the reading rate is once every 0.1s, this can be changed manually if needed
```

##  Buzzer (and passive buzzer)
<div id="header" style="float: left;" >
  <img src="assets/buzzer.png" width="40"/>
</div>

```
Usage:
python3 comfyScript/buzzer/buzzer.py [pin] [state]
python3 comfyScript/buzzer/passive_buzzer.py [pin] [state]

  where:
    passive_buzzer.py is used to passive buzzer
    pin: pinout to control buzzer
    state: 1 - running & 0 - disable 

```

##  DC Motor & L298N motor controller
<div id="header" style="float: left;" >
  <img src="assets/dc-motor.png" width="40"/>
</div>

```
Usage:
python3 motor/DCmotor.py pin1 pin2 pin3 pin4 state1 state2 state3 state4
python3 motor/DCmotor_single.py pin1 pin2 state1 state2 (for single motor control)

  where:
    
    pin1 -> pin4: L298 pinout connections
    state1 -> state 1: states of pin1 to pin4 (state = 1 means on and state = 0 means off)

```

##  2.7 in. e-Paper HAT
<div id="header" style="float: left;" >
  <img src="assets/dc-motor.png" width="40"/>
</div>

```
Setup (once):
Enable SPI interface on your Raspberry Pi & reboot

Usage:
python3 comfyScript/motor/DCmotor.py pin1 pin2 pin3 pin4 state1 state2 state3 state4
python3 comfyScript/motor/DCmotor_single.py pin1 pin2 state1 state2 (for single motor control)

  where:
    
    pin1 -> pin4: L298 pinout connections
    state1 -> state 1: states of pin1 to pin4 (state = 1 means on and state = 0 means off)

```

<a href="https://iconduck.com/sets/arduino-icons-kit" target="_blank">Icons</a> by <a href="https://iconduck.com/" target="_blank">Iconduck</a>, <a href="https://www.reshot.com/" target="_blank">Reshot</a><br>
<a href="https://icons8.com/illustrations/illustration/3d-fluency-raspberry" target="_blank">3D Raspberry</a> icon by <a href="https://icons8.com/illustrations" target="_blank">Icon8</a><br>
<a href="https://icons8.com/icon/8BGi5ks3s1pY/led-diode" target="_blank">LED Diode</a> icon by <a href="https://icons8.com/illustrations" target="_blank">Icon8</a><br>
<a href="https://iconduck.com/sets/arduino-icons-kit" target="_blank">Icons</a> by <a href="https://iconduck.com/" target="_blank">Iconduck</a><br /><br>
