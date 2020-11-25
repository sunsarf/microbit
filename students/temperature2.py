# Temperature Measurement Program 2
#
# s.case 10/18/20
#
# The microbit has an internal thermistor on the actual microprocesor chip.
# If we use the microbit libraries we can access the thermistor and the display
#
# The microbit has internal libraries of code stored in memory. We don't have
# write any special code to perform internal fucntions. Later, we will discover
# how to find out about all the libraries present in the microbit.

from microbit import *
while True:
    if button_a.was_pressed():
        degF = (9 / 5 * temperature()) + 32
        display.scroll(degF)