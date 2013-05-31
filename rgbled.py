#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

RED=sys.argv[1]
GREEN=sys.argv[2]
BLUE=sys.argv[3]

RPIN=23
GPIN=24
BPIN=25

# set LOW_VALUE to '1' for common anode and '0' for common cathode
# be sure to double check your wiring diagram for the LED type you are using 
LOW_VALUE='1'
def rgb():
   if (RED == LOW_VALUE) : 
      GPIO.output(RPIN, GPIO.LOW)
   else : 
      GPIO.output(RPIN, GPIO.HIGH)

   if (GREEN == LOW_VALUE) : 
      GPIO.output(GPIN, GPIO.LOW)
   else : 
      GPIO.output(GPIN, GPIO.HIGH)

   if (BLUE == LOW_VALUE) : 
      GPIO.output(BPIN, GPIO.LOW)
   else : 
      GPIO.output(BPIN, GPIO.HIGH)
  
   time.sleep(10) 
   return

GPIO.setmode(GPIO.BCM)
GPIO.setup(RPIN, GPIO.OUT)
GPIO.setup(GPIN, GPIO.OUT)
GPIO.setup(BPIN, GPIO.OUT)

rgb()
GPIO.cleanup()

