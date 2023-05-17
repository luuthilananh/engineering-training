import RPi.GPIO as GPIO
import time
import numpy as np
#-----------------реализация последовательного АЦП
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
bits = len(dac) #bits là số bit của ADC được sử dụng.
levels = 2**bits  #levels là số mức giá trị đầu ra của ADC.
maxVoltage = 3.3
troykaModule = 17  #cổng GPIO được sử dụng để kết nối với module ADC.
ystanovka = 17
comparator = 4  #cổng GPIO được sử dụng để đọc giá trị đầu ra của ADC

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troykaModule, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

measured_data = np.array([]) #---------------------------------------

#chuyển đổi số thập phân sang dãy nhị phân gồm 8 bits
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
#chuyển đổi ngược lại
def binary2decimal(mass):
    res = 0
    for i in range(8):
        res = res + mass[i]*2**(7-i)
    return res

def adc():
    #for i in range(8): GPIO.output(leds[7-i], 0);
    podbor = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (8):
        podbor[i] = 1
    GPIO.output(dac, podbor)
    time.sleep(0.0007)
    comparatorValue = GPIO.input(comparator)# считываем значение 0/1 с компаратора
    if comparatorValue == 0:
        podbor[i] = 0
    else:
        podbor[i] = 1
    #print(podbor)
    return podbor
try:
    GPIO.output(ystanovka, 1) # кондёр будет заряжаться
    t1 = time.time() # фиксируем время начала эксперимента

    while(1):
        podb = adc()
        value = binary2decimal(podb) # сохраним отчёт АЦП в переменную
        voltage = value / levels * maxVoltage
        print("Digital = {:^3}, input voltage = {:.2f}".format(value, voltage))

        x = int(voltage/3.3*8 + 0.5) # подача value на leds
        for i in range(x): GPIO.output(leds[7-i], 1)
        #time.sleep(0.01)
        for i in range(x, 8): GPIO.output(leds[7-i], 0)

        measured_data = np.append(measured_data, value)
        if (value == 251):
            break

    GPIO.output(ystanovka, 0) # кондёр будет разряжаться

    while(1):
        podb = adc()
        value = binary2decimal(podb) # сохраним отчёт АЦП в переменную
        voltage = value / levels * maxVoltage
        print("Digital = {:^3}, input voltage = {:.2f}".format(value, voltage))

        x = int(voltage/3.3*8 + 0.5) # подача value на leds
        for i in range(x): GPIO.output(leds[7-i], 1)
        #time.sleep(0.01)
        for i in range(x, 8): 
            GPIO.output(leds[7-i], 0)

            measured_data = np.append(measured_data, value)
        if (value == 0):
            break

    t2 = time.time()
    measure_time = t2-t1
    print(measured_data)
    measured_data_str = [str(item) for item in measured_data]
    print(measured_data_str)
    with open("data.txt", 'w') as file:
        file.write("\n".join(measured_data_str))

    with open("settings.txt", 'w') as file:
        file.write(str(measure_time)) # длительность эксперимента
        file.write('\n')
        file.write(str(3.3/255)) # значение одного разряда в вольтах

except KeyboardInterrupt:
    print("Нажатие ctrl+c - выход")
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    quit()
finally:
    print("Работает блок finally")
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()