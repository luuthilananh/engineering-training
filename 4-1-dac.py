import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
# the GPIO pins are numbered according to the Broadcom SOC channel numbers
# sets up the GPIO pins specified in the 'dac' list as output pins using the 'GPIO.OUT' 
# initial=GPIO.LOW all the pins will be set to a low voltage (0V) initially when the script starts running.

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(bits)]
# bin(dec) converts dec (dang thap phan) to a binary string.
#[2:] remove "0b" because of the way bin() formats its output.(bo di ddang có 2b cua so nhi phan)
#.zfill(bits) pads(đệm) the resulting string with leading zeros to ensure that it has a length of bits(them 0 de dảm bảo dạng bit)
#int(bit) converts(chuyển) each character in the resulting string to an integer.
try:
    while True:
        in_str = input("Enter a number between 0 and 255 ('q' to quit): ") 
        if in_str.isdigit():
            val = int(in_str)
            if val >= 0 and val <= 255:
                volt = val / 255 * 3.3
                print("Expected voltage on DAC: {:.2f} V".format(volt))
                GPIO.output(dac, dec2bin(val))
            else:
                print("Number must be between 0 and 255")
        elif in_str == 'q':
            break
        else:
            print("Invalid input. Enter a number between 0 and 255 or 'q' to quit.")
except KeyboardInterrupt:
    print("\nProgram terminated by keyboard interrupt")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()

#19 in_str=input_str/ khi xhien q thì quit dung lai
#20 checks the in_str entered contains only digits (using the isdigit() method). If right, it is converted to an integer(so nguyen) and assigned(gan) to value.
#23 calculates the voltage corresponding(tg ung) to that number and prints it to the console
#25 dec2bin convert the decimal number to binary, and binary values are output to the DAC pins using GPIO.output.
#32 except KeyboardInterrupt block is executed(đc ket thúc) when the user presses(ấn) Ctrl+C to terminate(cham dứt)the program.


