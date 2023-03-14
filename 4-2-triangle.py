import RPi.GPIO as GPIO
import time

# GPIO settings
GPIO.setmode(GPIO.BOARD)

# List of DAC pins
dac = [26, 24, 22, 21, 19, 23, 18, 16]

# Setup DAC pins as outputs
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)

# Function for converting a number to binary code
def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    # Set the period of the triangle wave
    period = float(input("Enter the period of the triangle wave (in seconds): "))

    # Infinite loop for generating the triangle wave
    while True:
        for value in range(256):
            voltage = value / 255 * 3.3
            GPIO.output(dac, dec2bin(value))
            time.sleep(period / 512)

        for value in range(255, -1, -1):
            voltage = value / 255 * 3.3
            GPIO.output(dac, dec2bin(value))
            time.sleep(period / 512)

except KeyboardInterrupt:
    print("\nProgram terminated by keyboard interrupt")

finally:
    # Reset GPIO settings
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()


# in russian languge

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Список пинов ЦАП
dac = [26, 24, 22, 21, 19, 23, 18, 16]

# Настройка пинов ЦАП как выходов
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)

# Функция преобразования числа в двоичный код
def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    # Задаем период сигнала
    period = float(input("Введите период треугольного сигнала (в секундах): "))

    # Формируем бесконечный цикл формирования треугольного сигнала
    while True:
        for value in range(256):
            voltage = value / 255 * 3.3
            GPIO.output(dac, dec2bin(value))
            time.sleep(period / 512)

        for value in range(255, -1, -1):
            voltage = value / 255 * 3.3
            GPIO.output(dac, dec2bin(value))
            time.sleep(period / 512)

except KeyboardInterrupt:
    print("\nProgram terminated by keyboard interrupt")

finally:
    # Сброс настроек GPIO
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
#3 the GPIO pins are numbered according to(dc danh so theo) their location on the board, starting from pin 1
#26 Dòng /512trong time.sleep(period / 512)được sử dụng để chia khoảng thời gian thành 512 bước. 
# Vì DAC là một thiết bị 8 bit nên nó có thể xuất ra 256 mức điện áp tương tự. Để tạo sóng tam giác, mã lặp qua các mức này theo thứ tự tăng dần từ 0 đến 255 và sau đó theo thứ tự giảm dần từ 255 đến 0.
#  Bằng cách chia khoảng thời gian thành 512 bước (2 x 256), mã sẽ dành một khoảng thời gian bằng nhau ở mỗi mức trước khi chuyển sang mức tiếp theo, dẫn đến sóng tam giác mịn.