import RPi.GPIO as GPIO
import time

# Номер GPIO-пина, подключенного к RC-цепи
PIN = 12

# Настройка GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

# Создание объекта управления ШИМ на выбранном GPIO-пине с частотой 50 Гц
pwm = GPIO.PWM(PIN, 50)

try:
    # Запуск ШИМ с коэффициентом заполнения (duty cycle) 0
    pwm.start(0)

    while True:
        # Запрос у пользователя значения коэффициента заполнения в процентах
        duty_cycle = float(input("Введите коэффициент заполнения (0-100%): "))

        # Ограничение введённого значения коэффициента заполнения от 0 до 100%
        duty_cycle = min(max(duty_cycle, 0), 100)

        # Установка заданного коэффициента заполнения ШИМ-сигнала
        pwm.ChangeDutyCycle(duty_cycle)

        # Расчёт и вывод в терминал предполагаемого значения напряжения на выходе RC-цепи
        voltage = 3.3 * duty_cycle / 100
        print("Предполагаемое напряжение на выходе RC-цепи: {:.2f} В".format(voltage))

        # Задержка для стабилизации значений RC-цепи
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    # Остановка ШИМ и очистка настроек GPIO
    pwm.stop()
    GPIO.cleanup()

# in english

import RPi.GPIO as GPIO

# Set the GPIO mode and the PWM pin
GPIO.setmode(GPIO.BCM)
PWM_PIN = 18

# Set the PWM frequency and start with 0 duty cycle
PWM_FREQ = 50  # in Hz
PWM_DUTY_CYCLE = 0  # in percentage (0-100)

GPIO.setup(PWM_PIN, GPIO.OUT)
pwm = GPIO.PWM(PWM_PIN, PWM_FREQ)
pwm.start(PWM_DUTY_CYCLE)

try:
    while True:
        # Get the PWM duty cycle from user input
        duty_cycle = float(input("Enter PWM duty cycle (0-100): "))

        # Set the duty cycle and print the expected voltage
        pwm.ChangeDutyCycle(duty_cycle)
        expected_voltage = duty_cycle / 100.0 * 3.3  # assuming 3.3V power supply
        print("Expected voltage: {:.2f} V".format(expected_voltage))

except KeyboardInterrupt:
    # Clean up the GPIO pins
    print("\nCleaning up GPIO...")
finally:
    pwm.stop()
    GPIO.cleanup()    