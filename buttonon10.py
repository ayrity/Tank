import RPi.GPIO as GPIO
import time
import Robot
import atexit

GPIO.setmode(GPIO.BOARD)

sensorRIGHT = 40
sensorLEFT = 38

GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(sensorLEFT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensorRIGHT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

LEFT_TRIM   = 0
RIGHT_TRIM  = -7

robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

try:
    while True:
        button = GPIO.input(31)
        if button == False:
            if (0 != GPIO.input(sensorRIGHT)):
                robot.backward(175, 0.5)
                robot.left(175, 1)
            elif (0 != GPIO.input(sensorLEFT)):
                robot.backward(175, 0.5)
                robot.right(175, 1)
            elif (0 != GPIO.input(sensorLEFT) and 0 != GPIO.input(sensorRIGHT)):
                robot.backward(175, 1.5)
                robot.left(175, 1.75)
            else:
                robot.forward(175, )
            GPIO.output(35, True)
            GPIO.output(37, False)
            print('Button Pressed...')
        else:
            GPIO.output(37, True)
            GPIO.output(35, False)
            print('ready to roll')
            robot.forward(0, 0)
except:
    GPIO.cleanup()