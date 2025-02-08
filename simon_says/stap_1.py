from microbit import *

while True:
    if button_a.is_pressed():
        display.set_pixel(0, 2, 9)
    elif button_b.is_pressed():
        display.set_pixel(4, 2, 9)
    elif pin_logo.is_touched():
        display.set_pixel(2, 0, 9)

    sleep(150)
    display.clear()
