import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

isPressed = False



try:
    while True:
        button = GPIO.input(31)
        if button == False:
            if isPressed == False
                GPIO.output(35, True)
                GPIO.output(37, False)
                print('Button Pressed...')
                isPressed = True
        else:
            if isPressed == True
                GPIO.output(37, True)
                GPIO.output(35, False)
                print('ready to roll')
                isPressed = False
except:
    GPIO.cleanup()