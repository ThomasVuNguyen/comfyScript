import sys
import Adafruit_DHT

while True:
    humid, temp = Adafruit_DHT.read_retry(int(sys.argv[1]),int(sys.argv[2]))
    print(temp)