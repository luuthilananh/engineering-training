import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [1, 0, 0, 0, 0, 0, 0, 0]  # двоичное представление числа 2

# Настройка режима обращения к GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

# Подача на выход GPIO-пинов значений из списка number
GPIO.output(dac, number)

# Пауза для измерения напряжения
time.sleep(10)

# Подача на выход GPIO-пинов значения 0
GPIO.output(dac, [0] * len(dac))

# Сброс настроек GPIO
GPIO.cleanup()



# import RPi.GPIO as GPIO
# import time

# dac = [26, 19, 13, 6, 5, 11, 9, 10]
# number = [0, 1, 0, 1, 1, 1, 0, 0]

# # Настройка режима обращения к GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(dac, GPIO.OUT)

# # Подача на выход GPIO-пинов значений из списка number
# GPIO.output(dac, number)

# # Пауза для измерения напряжения
# time.sleep(15)

# # Подача на выход GPIO-пинов значения 0
# GPIO.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])

# # Сброс настроек GPIO
# GPIO.cleanup()
