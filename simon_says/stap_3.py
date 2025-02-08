from microbit import *
import music

te_raden = ["A", "B", "L"]

for knop in te_raden:
    if knop == "A":
        display.set_pixel(0, 2, 9)
        music.play("C")
        sleep(50)
        display.clear()
    elif knop == "B":
        display.set_pixel(4, 2, 9)
        music.play("E")
        sleep(50)
        display.clear()
    elif knop == "L":
        display.set_pixel(2, 0, 9)
        music.play("G")
        sleep(50)
        display.clear()
    sleep(50)

while True:
    if button_a.is_pressed():
        display.set_pixel(0, 2, 9)
        music.play("C")
        if te_raden.pop(0) != "A":
            display.show(Image.SKULL)
            music.play(["F3:4", "D3:4", "B2:10"])
            reset()
    elif button_b.is_pressed():
        display.set_pixel(4, 2, 9)
        music.play("E")
        if te_raden.pop(0) != "B":
            display.show(Image.SKULL)
            music.play(["F3:4", "D3:4", "B2:10"])
            reset()
    elif pin_logo.is_touched():
        display.set_pixel(2, 0, 9)
        music.play("G")
        if te_raden.pop(0) != "L":
            display.show(Image.SKULL)
            music.play(["F3:4", "D3:4", "B2:10"])
            reset()

    sleep(150)
    display.clear()
