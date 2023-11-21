import sys
import os
if sys.argv[1]=='led':
    os.system("python3 comfyScript/LED/led.py" + " " + sys.argv[2] +" " +sys.argv[3])
    
else:
    print("Wrong command, try again")