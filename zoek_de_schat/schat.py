from microbit import sleep, set_volume
import radio
import music


def map(waarde, in_min, in_max, uit_min, uit_max):
    waarde = min(max(waarde, in_min), in_max)
    in_verschil = in_max - in_min
    uit_verschil = uit_max - uit_min
    waarde_geschaald = (waarde - in_min) / in_verschil
    return uit_min + (waarde_geschaald * uit_verschil)


radio.config(group=1, power=5)
radio.on()
set_volume(0)

while True:
    radio.send("hallo")
    message = radio.receive_full()
    if message:
        signaal_sterkte = message[1]
        volume = map(signaal_sterkte, -255, 0, 0, 30)
        set_volume(round(volume))
        music.play(["e"])
    sleep(200)
