import RPi.GPIO as GPIO #import library
import time

button = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)

while True:
  if (GPIO.input(button)):
    print("Button Pressed")
    time.sleep(0.5)
  
