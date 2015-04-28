import RPi.GPIO as GPIO #import library
import time

led = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

while True:
  GPIO.output(led, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(led, GPIO.LOW)
  time.sleep(1)
  
