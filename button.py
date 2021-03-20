import RPi.GPIO as GPIO
import time
from adafruit_motorkit import MotorKit
from pygame import mixer
import os, random

mixer.init()
mixer.music.set_volume(0.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)

kit = MotorKit()

playing = False

sounds = os.listdir("/home/pi/sounds/")

try:
    while True:

        playing = mixer.music.get_busy()

        if not GPIO.input(5) and not playing:
            print("play")
            sound = random.choice(sounds)
            mixer.music.load("/home/pi/sounds/"+sound)
            mixer.music.play()
            time.sleep(0.5)

        if not GPIO.input(5) and playing:
            print("stop")
            mixer.music.stop()
            time.sleep(0.5)

        time.sleep(0.02)

        if playing:
            kit.motor1.throttle = 1
        else:
            kit.motor1.throttle = 0


finally:
    kit.motor2.throttle = 0
    kit.motor1.throttle = 0
    GPIO.cleanup()



