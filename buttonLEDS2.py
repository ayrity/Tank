import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

redLED = 37

try:
    while True:
         button = GPIO.input(31)
         if button == False:
             GPIO.output(35, True)
             print('Button Pressed...')
             time.sleep(0.2)
         else:
             GPIO.output(35, False)
except:
    GPIO.cleanup()