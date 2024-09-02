import RPi.GPIO as GPIO
import time

import board
import digitalio
from PIL import Image, ImageDraw
import adafruit_ssd1306

class OLED:
        def __init__(self):
              print('oled initialized')
        def speak_face(self):
            # Define the reset pin
            oled_reset = digitalio.DigitalInOut(board.D4)

            # Create the I2C interface
            i2c = board.I2C()

            # Create the SSD1306 OLED class
            WIDTH = 128
            HEIGHT = 64
            oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

            # Clear display
            oled.fill(0)
            oled.show()
                # Create blank image for drawing
            image = Image.new("1", (oled.width, oled.height))
            draw = ImageDraw.Draw(image)

            # Draw a face with an open mouth (speaking)
            # Head
            draw.ellipse((30, 5, 98, 59), outline=1)

            # Eyes
            draw.ellipse((45, 20, 55, 30), fill=1)
            draw.ellipse((73, 20, 83, 30), fill=1)

            # Open mouth (ellipse)
            draw.ellipse((55, 40, 73, 50), outline=1, fill=0)

            # Speech lines (to represent sound waves)
            draw.line((80, 35, 100, 25), fill=1, width=1)
            draw.line((80, 45, 100, 45), fill=1, width=1)
            draw.line((80, 55, 100, 65), fill=1, width=1)

            # Display image
            oled.image(image)
            oled.show()
        def thinking_face(self):
              # Define the reset pin
            oled_reset = digitalio.DigitalInOut(board.D4)

            # Create the I2C interface
            i2c = board.I2C()

            # Create the SSD1306 OLED class
            WIDTH = 128
            HEIGHT = 64
            oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

            # Clear display
            oled.fill(0)
            oled.show()

            # Create blank image for drawing
            image = Image.new("1", (oled.width, oled.height))
            draw = ImageDraw.Draw(image)

            # Draw a thinking man face
            # Head
            draw.ellipse((30, 5, 98, 59), outline=1)

            # Eyes
            draw.ellipse((45, 20, 55, 30), fill=1)
            draw.ellipse((73, 20, 83, 30), fill=1)

            # Mouth (slightly curved line)
            draw.arc((50, 35, 78, 50), start=0, end=180, fill=1, width=2)

            # Eyebrow (raised)
            draw.arc((40, 10, 60, 25), start=0, end=180, fill=1, width=2)
            draw.arc((68, 10, 88, 25), start=0, end=180, fill=1, width=2)

            # Hand on chin
            draw.ellipse((80, 45, 100, 65), outline=1)  # Hand
            draw.line((90, 55, 90, 70), fill=1, width=2)  # Arm

            # Thinking bubble
            draw.ellipse((105, 10, 110, 15), outline=1)
            draw.ellipse((110, 5, 118, 13), outline=1)
            draw.ellipse((118, 0, 128, 10), outline=1)

            # Display image
            oled.image(image)
            oled.show()
        def smiley_face(self):
              # Define the reset pin
            oled_reset = digitalio.DigitalInOut(board.D4)

            # Create the I2C interface
            i2c = board.I2C()

            # Create the SSD1306 OLED class
            # The first two parameters are the pixel width and pixel height.  Change these
            # to the right size for your display!
            WIDTH = 128
            HEIGHT = 64
            oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

            # Clear display
            oled.fill(0)
            oled.show()

            # Create blank image for drawing
            image = Image.new("1", (oled.width, oled.height))
            draw = ImageDraw.Draw(image)

            # Draw a smiley face
            # Face
            draw.ellipse((20, 10, 108, 54), outline=1)

            # Eyes
            draw.ellipse((40, 20, 55, 35), fill=1)
            draw.ellipse((73, 20, 88, 35), fill=1)

            # Mouth
            draw.arc((35, 25, 93, 55), start=0, end=180, fill=1, width=3)

            # Display image
            oled.image(image)
            oled.show()
