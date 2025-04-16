import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(e) for e in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7 ,1, 0, 5 ,12, 6]

GPIO.setup(dac, GPIO.OUT)

try:
    n = int(input())
    n = n / 510
    while True:
        for i in range(256):
            num = dec2bin(i)
            GPIO.output(dac, num)
            time.sleep(n*256/510)
        for i in range(255):
            num = dec2bin(255-i)
            GPIO.output(dac, num)
            time.sleep(n*254/510)

                
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
