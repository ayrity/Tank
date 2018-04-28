import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

redLED = 37
greenLED = 35
button = 31

while True:
    if button == False:
        GPIO.output(35, True)
        GPIO.output(37, False)
        print('button pressed')
        time.sleep(0.2)
    else:
        GPIO.output(35, False)
        GPIO.output(37, True)
        print('ready to start')
        time.sleep(0.2)
GPIO.cleanup()