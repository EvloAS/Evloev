import RPi.GPIO as GPIO
import time


def dec2bin(value):
    return [int(e) for e in bin(value)[2:].zfill(8)]


def adc():
    for i in range(256):
        GPIO.output(dac, dec2bin(i))
        time.sleep(0.005)
        v_comp = GPIO.input(comp)
        if v_comp == 1:
            return i


GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7 ,1, 0, 5 ,12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        n = adc()
        U = 3.3/256*n
        print("Цифровое значение:", n, ". Напряжение:", U)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
