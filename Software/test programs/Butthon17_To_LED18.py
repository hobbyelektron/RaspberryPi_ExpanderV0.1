import RPi.GPIO as GPIO #import library

button = 17
led = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(button, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
  if (GPIO.input(button)):
    print("Button Pressed")
    GPIO.output(led, GPIO.HIGH)
  else:
    GPIO.output(led, GPIO.LOW)
    
  
