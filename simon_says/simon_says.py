from microbit import *
import music
import random

random_seq = []
to_guess = []

while True:
    if not to_guess:
        random_seq.append(random.randrange(3))
        to_guess = random_seq.copy()
        for i in to_guess:
            if i == 0:
                display.set_pixel(0, 2, 9)
                music.play("A4:2")
                sleep(50)
                display.clear()
            elif i == 1:
                display.set_pixel(4, 2, 9)
                music.play("B4:2")
                sleep(50)
                display.clear()
            elif i == 2:
                display.set_pixel(2, 0, 9)
                music.play("C4:2")
                sleep(50)
                display.clear()
            sleep(50)

    if button_a.is_pressed():
        display.set_pixel(0, 2, 9)
        music.play("A4:2")
        if to_guess.pop(0) != 0:
            music.play("G4:10")
            reset()
    elif button_b.is_pressed():
        display.set_pixel(4, 2, 9)
        music.play("B4:2")
        if to_guess.pop(0) != 1:
            music.play("G4:10")
            reset()
    elif pin_logo.is_touched():
        display.set_pixel(2, 0, 9)
        music.play("C4:2")
        if to_guess.pop(0) != 2:
            music.play("G4:10")
            reset()

    sleep(150)
    display.clear()
