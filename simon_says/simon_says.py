from microbit import *
import music
import random

te_raden = []
alle_knoppen = []


def game_over():
    display.show(Image.SKULL)
    music.play(["F3:4", "D3:4", "B2:10"])
    reset()


def knop_a():
    display.set_pixel(0, 2, 9)
    music.play("C")
    sleep(50)
    display.clear()


def knop_b():
    display.set_pixel(4, 2, 9)
    music.play("E")
    sleep(50)
    display.clear()


def knop_l():
    display.set_pixel(2, 0, 9)
    music.play("G")
    sleep(50)
    display.clear()


while True:
    if not te_raden:
        alle_knoppen.append(random.choice(["A", "B", "L"]))
        te_raden = alle_knoppen.copy()
        for knop in te_raden:
            if knop == "A":
                knop_a()
            elif knop == "B":
                knop_b()
            elif knop == "L":
                knop_l()

    if button_a.is_pressed():
        knop_a()
        if te_raden.pop(0) != "A":
            game_over()
    elif button_b.is_pressed():
        knop_b()
        if te_raden.pop(0) != "B":
            game_over()
    elif pin_logo.is_touched():
        knop_l()
        if te_raden.pop(0) != "L":
            game_over()

    sleep(150)
    display.clear()
