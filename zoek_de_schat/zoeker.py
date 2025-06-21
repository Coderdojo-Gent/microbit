from microbit import display, sleep
import radio


def map(waarde, in_min, in_max, uit_min, uit_max):
    waarde = min(max(waarde, in_min), in_max)
    in_verschil = in_max - in_min
    uit_verschil = uit_max - uit_min
    waarde_geschaald = (waarde - in_min) / in_verschil
    return uit_min + (waarde_geschaald * uit_verschil)


def toon_leds(aantal):
    rij = 0
    kolom = 0
    for _ in range(aantal):
        display.set_pixel(rij, kolom, 9)
        rij += 1
        if rij > 4:
            rij = 0
            kolom += 1


radio.config(group=1, power=5)
radio.on()

for aantal in range(26):
    toon_leds(aantal)
    sleep(25)
sleep(1000)
display.clear()

while True:
    display.clear()
    radio.send("hallo")
    message = radio.receive_full()
    if message:
        signaal_sterkte = message[1]
        aantal_leds = map(signaal_sterkte, -120, -20, 0, 25)
        toon_leds(aantal_leds)
    sleep(200)
