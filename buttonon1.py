import RPi.GPIO as GPIO
import time
import Robot
import atexit

GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

isPressed = False

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
            if isPressed == False:
                while True:
                    if (0 == GPIO.input(sensorRIGHT and sensorLEFT)):
                        robot.forward(200, )
                    if (0 != GPIO.input(sensorRIGHT)):
                        robot.backward(150, 0.5)
                        robot.left(150, 0.8)
                    if (0 != GPIO.input(sensorLEFT)):
                        robot.backward(150, 0.5)
                        robot.right(150, 0.6)
                    if (0 != GPIO.input(sensorLEFT) and 0 != GPIO.input(sensorRIGHT)):
                        robot.backward(150, 1.5)
                        robot.left(150, 1.4)
                    time.sleep(1.0)
                GPIO.output(35, True)
                GPIO.output(37, False)
                print('Button Pressed...')
                isPressed = True
        else:
            if isPressed == True:
                GPIO.output(37, True)
                GPIO.output(35, False)
                print('ready to roll')
                isPressed = False
except:
    GPIO.cleanup()