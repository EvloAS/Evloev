import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

p = GPIO.PWM(24, 1000)
p.start(0)

try:
    while True:
        p.start(int(input()))

                
finally:
    p.start(0)
    GPIO.cleanup()
