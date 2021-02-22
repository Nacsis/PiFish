#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
from adafruit_motorkit import MotorKit


kit = MotorKit()


GPIO.setmode(GPIO.BCM)
#22 LED Active
#23 Input Active
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#24 LED Recording
#25 Input Recording
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#5 Button Even (pulled up)
#6 Sound sensor
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


i=0

try:
	while True:
		# HEAD
		if GPIO.input(23):
			kit.motor1.throttle = 1
		else:
			kit.motor1.throttle = 0

		# Tail
		if GPIO.input(25):
			kit.motor2.throttle = 1
		else:
			kit.motor2.throttle = 0

		# Mouth
		if GPIO.input(6):
			kit.motor3.throttle = 1
		else:
			kit.motor3.throttle = -1

		time.sleep(0.001)

finally:

	 kit.motor1.throttle = 0
	 kit.motor2.throttle = 0
	 kit.motor3.throttle = 0

	 GPIO.cleanup()
