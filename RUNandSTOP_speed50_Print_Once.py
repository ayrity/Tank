#!/usr/bin/python
import RPi.GPIO as GPIO
import time

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

# set the speed to start, from 0 (off) to 255 (max speed)
mh.getMotor(3).setSpeed(50)
mh.getMotor(4).setSpeed(50)
# turn on motor


sensor = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
current = GPIO.input(sensor)
previous = current
def printState(current):
    print 'GPIO pin %s is %s' % (sensor, 'HIGH' if current else 'LOW')

if (0 == GPIO.input(sensor)):
    print "Forward"
if (0 != GPIO.input(sensor)):
    print "Detected Barrier!"

while True:
    if (0 == GPIO.input(sensor)):
        mh.getMotor(3).run(Adafruit_MotorHAT.FORWARD)
        mh.getMotor(4).run(Adafruit_MotorHAT.FORWARD)
    if (0 != GPIO.input(sensor)):
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    time.sleep(1.0)
GPIO.cleanup()
