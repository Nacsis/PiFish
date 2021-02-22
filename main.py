#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

pin1=5
pin2=6

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

i=0

try:
    while True:
        if GPIO.input(pin1):
            print "Pin1 ON"
        if GPIO.input(pin2):
            print "Pin2 ON"

	if not GPIO.input(pin1) and not GPIO.input(pin2):
		print(i)

	time.sleep(0.5)

finally:
    GPIO.cleanup()

