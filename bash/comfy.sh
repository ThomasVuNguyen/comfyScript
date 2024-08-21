#!/bin/bash
# calling comfy + component + pins


python3 comfyScript/bash/comfy.py "$@"

case $1 in

  led)
  
  python3 comfyScript/LED/led.py $2 $3
  ;;

  rgbled)
  python3 comfyScript/LED/RGB_led.py $2 $3 $4 $5 $6 $7
  ;;

  stepper)
  python3 comfyScript/stepper/stepper.py $2 $3 $4 $5 $6
  ;;

  distance)
  python3 comfyScript/distance_sensor/HC-SR04.py $2 $3 $4
  ;;

  avoidance)
  python3 comfyScript/avoidance_sensor/avoidance_sensor.py $2 $3
  ;;

  buzzer)
  python3 comfyScript/buzzer/buzzer.py $2 $3
  ;;

  servo)
  python3 comfyScript/servo/sg90.py $2 $3
  ;;

  dc)
  python3 comfyScript/motor/DCmotor_single.py $2 $3 $4 $5
  ;;

  buzzer)
  python3 comfyScript/buzzer/buzzer.py $2 $3
  ;;

  passive_buzzer)
  python3 comfyScript/buzzer/passive_buzzer.py $2 $3
  ;;

  dht_temp)
  python3 comfyScript/DHT/dht_temp.py $2 $3
  ;;

  dht_humid)
  python3 comfyScript/DHT/dht_humid.py $2 $3
  ;;

  camera)
  python3 comfyScript/camera/$2.py
  ;;
  
  web_socket)
  python3 comfyScript/web_socket/start_socket.py
  ;;

  gemini_setup)
  python3 comfyScript/gemini_ai/setup.py $2
  ;;

  gemini_run)
  python3 comfyScript/gemini_ai/convo.py $2
  ;;
  
  *)
  echo "Wrong command, try again"
  ;;

esac

