#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
from adafruit_motorkit import MotorKit


kit = MotorKit()

pin1=5
pin2=6

pin1_old = False
pin2_old = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

i=0

try:
    while True:

	# Pin 1
        if GPIO.input(pin1) and not pin1_old:
		print("ON")
		kit.motor1.throttle = 1
		pin1_old = True
		time.sleep(0.1)

	if not GPIO.input(pin1) and pin1_old:
		print("OFF")
		kit.motor1.throttle = -1
		pin1_old = False
		time.sleep(0.1)

	kit.motor1.throttle = 0


	time.sleep(0.5)
finally:
    GPIO.cleanup()

