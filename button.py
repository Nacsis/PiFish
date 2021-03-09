import RPi.GPIO as GPIO
import time
from adafruit_motorkit import MotorKit
from pygame import mixer
import os, random

mixer.init()

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)

try:
    while True:
        if not GPIO.input(5)
            print("play")
            random.choice(os.listdir("~/sounds/"))
        
        
finally:
    kit.motor2.throttle = 0
    GPIO.cleanup()



