#!/usr/bin/env python3


# import RPi.GPIO as GPIO
from periphery import GPIO
import subprocess

powerPin = GPIO(107, "high")
powerPin.direction = 'in'
powerPin.edge = "falling"
powerPin.read()
powerPin.poll()

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.wait_for_edge(3, GPIO.FALLING)

subprocess.call(['shutdown', '-h', 'now'], shell=False)
