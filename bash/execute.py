import sys
import re
import os
comfyscript_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the comfyscript folder to the Python path
sys.path.append(comfyscript_path)

# Now you can import from the led folder
from LED.led_class import LED
from LED.RGB_class import RGB_LED
from motor.DCmotor_class import DC_motor
from I2C_OLED.oled_class import OLED
from motor.DCmotor_i2c_single import i2c_motor
from ollama_class.tinyllama_class import tinyllama
def execute_command(command_separated):
    if(command_separated[0] == 'comfy'):
        command_separated.pop(0)
    
    object = command_separated[0]
    print(object)

    if(object == 'led'):
        identification = command_separated[1]
        action = command_separated[2]

        pin_num = extract_integer(identification)
        print('pin number is ', pin_num)
        led = LED(pin_num)

        if(action == 'on' or action == '1'):
            led.on()
        elif(action == 'off' or action == '0'):
            led.off()
        elif(action == 'blink'):
            led.blink()
        else:
            print('led function ', action, ' not found')
    
    elif(object in ['rgbled', 'led_rgb', 'rgb','rgb_led','ledrgb']):
        contains_red = find_matching_string(
                command_separated,
                ['red', 'r-'] 
                )
        red_pin = extract_integer(contains_red)

        contains_green = find_matching_string(
                command_separated,
                ['green', 'g-'] 
                )
        green_pin = extract_integer(contains_green)

        contains_blue = find_matching_string(
                command_separated,
                ['blue', 'b-'] 
                )
        blue_pin = extract_integer(contains_blue)
        action = command_separated[4]
        print('action: ', action)
        rgb = RGB_LED(red_pin, green_pin, blue_pin)

        if(action in ['red', 'r']):
            rgb.red()
        
        elif(action in ['green', 'g']):
            rgb.green()
        
        elif(action in ['blue', 'b']):
            rgb.blue()
        
        elif(action in ['yellow','y', 'orange', 'o']):
            rgb.yellow()

        elif(action in ['magenta','purple', 'mag', 'pur']):
            rgb.magenta()

        elif(action in ['cyan','sky']):
            rgb.cyan()
        
        elif(action in ['off', '0']):
            rgb.off()
    elif(object in ['dc', 'dcmotor', 'dc_motor']):
        identification = [extract_integer(command_separated[1]), extract_integer(command_separated[2])]
        action = command_separated[3]

        dc = DC_motor(identification[0], identification[1])

        if(action in ['rotate', 'on', '1' ,'spin', 'run', 'clockwise', 'clock-wise']):
            dc.rotate()
        elif(action in ['reverse', '-1', 'counter-clock', 'counterclock', 'counter_clock', 'counterclockwise']):
            dc.reverse()
        else:
            dc.stop()
    elif(object in ['oled', 'i2c_oled', 'oled_i2c']):
        action = command_separated[1]
        oled = OLED()
        if(action in ['speak', 'speaking']):
            oled.speak_face()
        elif(action in ['think', 'thinking']):
            oled.thinking_face()
        elif(action in ['smile', 'smiley', 'smiling']):
            oled.smiley_face()
    elif(object in ['ollama', 'llama', 'tinyllama', 'ai']):
        query = command_separated[1]
        ai = tinyllama()
        ai.ask(query)
    elif(object in ['motor-i2c', 'i2c-motor', 'i2c-dc','dc-i2c']):
        id = command_separated[1]
        print(id)
        speed = command_separated[2]
        print(speed)
        motor = i2c_motor(id)
        motor.spin(speed)


def extract_integer(string):
    # This pattern matches only integers, including negative integers
    match = re.search(r'\b\d+\b', string)
    if match:
        print(match.group())
        return int(match.group())
        
    return None  # Return None if no integer is found

def find_matching_string(string_list, search_terms):
    return next((s for s in string_list if any(term in s for term in search_terms)), None)


def parse_int_string(s):
    # Regular expression pattern to match the format
    pattern = r'^(\d+)(-\d+)*$'
    
    # Check if the string matches the pattern
    if not re.match(pattern, s):
        raise ValueError("Invalid format. Expected format: int-int-int-...")
    
    # Split the string by '-' and convert each part to an integer
    try:
        int_list = [int(x) for x in s.split('-')]
        return int_list
    except ValueError:
        raise ValueError("Invalid integer in the string")
