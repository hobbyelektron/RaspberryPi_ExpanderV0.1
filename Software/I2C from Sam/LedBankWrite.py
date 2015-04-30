import RPi.GPIO as GPIO #import library
import smbus
import time

I2CLEDADDRES = 0x20 
 
bus = smbus.SMBus(1)

while true:
  for a in range(0,256):
	bus.write_byte(I2CLEDADDRES,a)
	time.sleep(0.1)
  
