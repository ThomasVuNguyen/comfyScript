#!/bin/bash
# calling comfy + component + pins

case $1 in

  led)
  python3 comfyScript/LED/led.py $2 $3
  ;;

  stepper)
  python3 comfyScript/stepper/stepper.py $2 $3 $4 $5 $6
  ;;

  distance)
  python3 comfyScript/distance_sensor/HC-SR04.py $2 $3 $4
  ;;

  buzzer)
  python3 comfyScript/buzzer/buzzer.py $2 $3
  ;;

  dc)
  python3 comfyScript/motor/DCmotor_single.py $2 $3 $4 $5
  ;;

  DHT)
  case $2 in
    temp)
      python3 comfyScript/DHT/dht_temp.py $2 $3
  ;;
    humid)
      python3 comfyScript/DHT/dht_humid.py $2 $3
  ;;
  *)
  echo "Wrong command, try again"
  ;;

esac