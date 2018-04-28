import RPi.GPIO as GPIO
import time
import Robot
import atexit

GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

LEFT_TRIM   = 0
RIGHT_TRIM  = -7

robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

sensorRIGHT = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorRIGHT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

sensorLEFT = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorLEFT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        button = GPIO.input(31)
        if button == False:
            if (0 == GPIO.input(sensorRIGHT and sensorLEFT)):
                robot.forward(125, )
            if (0 != GPIO.input(sensorRIGHT)):
                robot.backward(125, 1.5)
                robot.left(125, 1.25)
            if (0 != GPIO.input(sensorLEFT)):
                robot.backward(125, 1.5)
                robot.right(125, 1.5)
            if (0 != GPIO.input(sensorLEFT) and 0 != GPIO.input(sensorRIGHT)):
                robot.backward(125, 3)
                robot.left(125, 2)
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
