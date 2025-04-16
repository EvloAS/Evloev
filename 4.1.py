import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(e) for e in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7 ,1, 0, 5 ,12, 6]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        n = input("Введите число (0-255):")
        if n == "q":
            exit()
        try:
            n = int(n)
            if n < 0:
                print("Число не должно быть отрицательным")
                continue
            if n > 255:
                print("Чило не должно быть больше 255")
                continue2
        except ValueError:
            try:
                n = float(n)
                print("Число должно быть целым")
                continue
            except ValueError:
                print("Это должно быть число")
                continue

        U = 3.3/256*n
        print("Напряжение:", U)
        num = decimal2binary(n)
        GPIO.output(dac, num)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
