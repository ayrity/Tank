import time
import Robot
import RPi.GPIO as GPIO
import atexit

LEFT_TRIM   = 0
RIGHT_TRIM  = 0

robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

sensor = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if (0 == GPIO.input(sensor)):
        robot.forward(150, 0)
    if (0 != GPIO.input(sensor)):
        robot.left(200, 1.5)
    time.sleep(1.0)
GPIO.cleanup()
