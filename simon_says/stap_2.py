from microbit import *
import music

while True:
    if button_a.is_pressed():
        display.set_pixel(0, 2, 9)
        music.play("C")
    elif button_b.is_pressed():
        display.set_pixel(4, 2, 9)
        music.play("E")
    elif pin_logo.is_touched():
        display.set_pixel(2, 0, 9)
        music.play("G")

    sleep(150)
    display.clear()
