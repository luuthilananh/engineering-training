import RPi.GPIO as GPIO
import time

leds = [18, 23, 24, 25, 8, 7, 12, 16]  # GPIO-пины в области LEDS

GPIO.setmode(GPIO.BCM)  # Настраиваем режим нумерации GPIO
GPIO.setup(leds, GPIO.OUT)  # Настраиваем GPIO на выход

# Включаем светодиоды поочередно на 0.2 секунды
for i in range(7, -1, -1):
    GPIO.output(leds[i], GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(leds[i], GPIO.LOW)

# Делаем три круга
for j in range(3):
    for i in range(8):
        GPIO.output(leds[i], GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(leds[i], GPIO.LOW)

# Отключаем все GPIO-выходы
GPIO.output(leds, GPIO.LOW)

# Сбрасываем настройки GPIO
GPIO.cleanup()