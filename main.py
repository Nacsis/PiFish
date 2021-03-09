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
# GPIO.setup(5, GPIO.IN)
#6 Sound sensor
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)


i=0

try:
	while True:
		# HEAD
		if GPIO.input(23):
			#print(".")
			kit.motor1.throttle = 1
		else:
			#print(".")
			kit.motor1.throttle = 0

		# Tail
		if GPIO.input(25):
			#print(".")
			kit.motor2.throttle = 1
		else:
			#print(".")
			kit.motor2.throttle = 0

		# Mouth
		if not GPIO.input(6):
			kit.motor3.throttle = 1
			time.sleep(0.10)
		else:
			kit.motor3.throttle = -1
			time.sleep(0.00)

		time.sleep(0.001)

finally:

	 kit.motor1.throttle = 0
	 kit.motor2.throttle = 0
	 kit.motor3.throttle = 0

	 GPIO.cleanup()
