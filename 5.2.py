import RPi.GPIO as GPIO
import time


def dec2bin(value):
    return [int(e) for e in bin(value)[2:].zfill(8)]

def bin2dec(n):
    res = 0
    for i in range(8):
        res = res + n[i]*2**(7-i)
    return res




def adc():

    i = [1, 0, 0, 0, 0, 0, 0, 0]
    GPIO.output(dac, i)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        i[0] = 0

    i[1] = 1
    GPIO.output(dac, i)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        i[1] = 0

    i[2] = 1
    GPIO.output(dac, i)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        i[2] = 0

    i[3] = 1
    GPIO.output(dac, i)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        i[3] = 0

    i[4] = 1
    GPIO.output(dac, i)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        i[4] = 0

    i[5] = 1
    GPIO.output(dac, i)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        i[5] = 0

    i[6] = 1
    GPIO.output(dac, i)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        i[6] = 0

    i[7] = 1
    GPIO.output(dac, i)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        i[7] = 0

    res = 0
    for j in range(8):
        res = res + i[j]*2**(7-j)
    return res
    
    


GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7 ,1, 0, 5 ,12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        time1 = time.time()
        n = adc()
        U = 3.3/256*n
        time2 = time.time()
        print("Время выполнения кода:", time2-time1)
        print("Цифровое значение:", n, ". Напряжение:", U)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()