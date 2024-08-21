import sys
import re
import os
comfyscript_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the comfyscript folder to the Python path
sys.path.append(comfyscript_path)

# Now you can import from the led folder
from LED.led_class import LED

def execute_command(command_separated):
    if(command_separated[0] == 'comfy'):
        command_separated.pop(0)
    
    object = command_separated[0]

    if(object == 'led'):
        identification = command_separated[1]
        action = command_separated[2]

        pin_num = extract_integer(identification)
        print('pin number is ', pin_num)
        led = LED(pin_num)

        if(action == 'on' or action == '1'):
            led.on()
        else:
            led.off()
            

def extract_integer(string):
    # This pattern matches only integers, including negative integers
    match = re.search(r'-?\d+', string)
    if match:
        print(match.group())
        return int(match.group())
        
    return None  # Return None if no integer is found


execute_command(['comfy', 'led', '1', 'on'])