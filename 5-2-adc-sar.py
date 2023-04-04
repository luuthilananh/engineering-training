import time
import RPi.GPIO as GPIO

# Define GPIO pins
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)

# Function to convert decimal number to binary list
def dec2binlist(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

# Function to convert binary list to decimal number
def binlist2dec(binlist):
    return int(''.join(map(str, binlist)), 2)

# Function to implement successive approximation ADC
def adc():
    value = 0
    for i in range(8):
        bit_value = 2 ** (7 - i)
        dac_value = dec2binlist(value | bit_value)
        GPIO.output(dac, dac_value)
        time.sleep(0.001)
        comp_value = GPIO.input(comp)
        if comp_value == 1:
            value |= bit_value
    return value

# Main program
try:
    while True:
        value = adc()
        voltage = round(value / 255 * 3.3, 2)
        print(f'Digital value: {value}, Voltage: {voltage}V')
        time.sleep(1)
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()