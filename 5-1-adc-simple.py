import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the DAC, COMP and TROYKA MODULE
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

# Configure GPIO pins for output (DAC) and input (COMP and TROYKA MODULE)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)

def dec2bin_list(value):
    """Convert a decimal number to a list of 8 bits"""
    bin_list = list(bin(value)[2:].zfill(8))
    return [int(bit) for bit in bin_list]

def adc():
    """Returns a decimal number proportional to the voltage at TROYKA MODULE S terminal"""
    for value in range(256):
        # Set the DAC to the current value and wait for voltage to stabilize
        bin_list = dec2bin_list(value)
        GPIO.output(dac, bin_list)
        time.sleep(0.0001)

        # Read the voltage at the COMP pin and convert it to a decimal value
        voltage = GPIO.input(comp) * 3.3
        decimal_value = int((voltage / 3.3) * 255)

        # If the decimal value is equal to the current DAC value, return it
        if decimal_value == value:
            return decimal_value

try:
    while True:
        # Call the adc() function and convert the decimal value to a voltage
        decimal_value = adc()
        voltage = decimal_value * (3.3 / 255)

        # Print the decimal value and corresponding voltage to the console
        print(f"Decimal value: {decimal_value}, Voltage: {voltage:.2f}V")
except KeyboardInterrupt:
    pass
finally:
    # Set all used GPIO pins to 0 and clean up GPIO settings
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()