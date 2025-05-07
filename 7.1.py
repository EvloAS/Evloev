import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

leds = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7 ,1, 0, 5 ,12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)


def dec2bin(value):                                  #Функция перевода числа в двоичный вид
    return [int(e) for e in bin(value)[2:].zfill(8)]

def led_print(value):                                #Функция, измеряющая напряжение на выходе тройка-модуля
    GPIO.output(leds, dec2bin(value))

def adc():                              # Функция, измеряющая выход тройки-модуля
    i = [0, 0, 0, 0, 0, 0, 0, 0]

    for j in range(8):
        i[j] = 1
        GPIO.output(dac, i)
        time.sleep(0.003)
        if GPIO.input(comp) == 1:
            i[j] = 0

    res = 0
    for j in range(8):
        res = res + i[j]*2**(7-j)

    return res

def u_troyka(value):                     #Функция, переводящая двоичное число в напряжение
    return 3.3/256*value


try:
    dat = []
    time1 = time.time()
    GPIO.output(troyka, 1)

    while True:                         #Измерение зарядки конденсатора
        binu = adc() 
        dat.append(u_troyka(binu))
        if binu > 240:
            break
    
    while True:                        #Измерение разрядки конденсатора
        binu = adc() 
        GPIO.output(troyka, 0)
        dat.append(u_troyka(binu))
        if binu < 30:
            break

    time2 = time.time()                #Расчитываем общую продолжительность эксперимента, период одного измерения, среднюю частоту дискретизации проведённых измерений, шаг квантования АЦП
    dtime = time2 - time1
    per = dtime/len(dat)
    freq = 1/per
    step_acp = 3.3/256

    dat_str = [str(item) for item in dat]
    with open('data.txt', "w") as f:              #Печать даных в файл data.txt
        f.write("\n".join(dat_str))
    
    with open('setting.txt', "w") as f:                                             #Печать даных в файл setting.txt
        
        f.write(f'Среднюю частоту дискретизации проведённых измерений: {freq}\nШаг квантования АЦП: {step_acp}')   

    plt.plot(dat)
    plt.show()

    print('Общая продолжительность эксперимента:', dtime)                                    #Печать в терминал
    print('Период одного измерения:', per)
    print('Средняя частоту дискретизации проведённых измерений:', freq)
    print('Шаг квантования АЦП:', step_acp)

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
