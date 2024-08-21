import sys
import re
import os
comfyscript_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the comfyscript folder to the Python path
sys.path.append(comfyscript_path)

# Now you can import from the led folder
from LED.led_class import LED
from LED.RGB_class import RGB_LED
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
        
        


def extract_integer(string):
    # This pattern matches only integers, including negative integers
    match = re.search(r'\b\d+\b', string)
    if match:
        print(match.group())
        return int(match.group())
        
    return None  # Return None if no integer is found

def find_matching_string(string_list, search_terms):
    return next((s for s in string_list if any(term in s for term in search_terms)), None)