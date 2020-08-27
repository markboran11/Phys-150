# from adafruit
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
  # note the new line: "a" is a variable that takes the values that are 
  # listed in square brackets.  This loop is sometimes called a "foreach"
  for a in [1,1,1,5,5,5,1,1,1]:
        led.value = True
        time.sleep(a/5)
        led.value = False
        time.sleep(a/15)
    
# What if you wanted the LED to be a bright-dim oscillating pattern?
# loops? You could blink out an SOS pattern (...---...) with a foreach loop that specifies duration
