import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Define GPIO pins
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 17
troyka = 4
leds = [21, 20, 16, 12, 7, 8, 25, 24]

# Set GPIO pins as outputs
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)

# Set GPIO pin as input
GPIO.setup(comp, GPIO.IN)

def dec2bin_list(value):
    """Convert decimal value to binary list"""
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def bin_list2dec(bin_list):
    """Convert binary list to decimal value"""
    return int("".join(str(bit) for bit in bin_list), 2)

def adc():
    """Perform analog to digital conversion"""
    value = 0
    for i in range(8):
        bin_value = dec2bin_list(value)
        bin_value[7 - i] = 1
        value = bin_list2dec(bin_value)

        # Set DAC output
        GPIO.output(dac, dec2bin_list(value))

        # Allow some settling time for the circuit to stabilize
        time.sleep(0.001)

        # Read comparator output and update value accordingly
        if GPIO.input(comp) == 0:
            value -= 2 ** (7 - i)

    return value

try:
    while True:
        value = adc()
        voltage = value / 255 * 3.3
        leds_to_light = int(value / 32) + 1
        GPIO.output(leds[:leds_to_light], GPIO.HIGH)
        GPIO.output(leds[leds_to_light:], GPIO.LOW)
        print("ADC value: {}, Voltage: {}V".format(value, voltage))
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup()