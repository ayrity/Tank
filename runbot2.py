import time
import Robot

LEFT_TRIM   = 0
RIGHT_TRIM  = 0

robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

sensorRIGHT = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorRIGHT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

sensorLEFT = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorLEFT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if (0 == GPIO.input(sensorRIGHT) and 0 == GPIO.input(sensorLEFT)):
        robot.forward(125, 0)
    if (0 != GPIO.input(sensorRIGHT)):
        robot.left(150, 0.6)
    if (0 != GPIO.input(sensorLEFT)):
        robot.right(150, 0.6)
    time.sleep(1.0)
GPIO.cleanup()