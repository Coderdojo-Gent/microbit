# Zoek de Schat

## Intro

Voor deze opdracht heb je 2 (of meer) micro:bits nodig.

Een micro:bit is *de schat*. Hij stuurt berichten uit die andere micro:bits kunnen ontvangen. De schat wordt ergens verstopt.

Een andere micro:bit is *de schattenzoeker*. Hij ontvangt de berichten van de schat. Door te kijken hoe sterk het signaal van het bericht is kan de zoeker laten zien hoe dicht de zoeker bij de schat is. Bijvoorbeeld door steeds meer leds de laten branden.

## Stap 1: Berichten sturen en ontvangen

Open de micro:bit Python editor (https://python.microbit.org/v/3) en zoek bij `API` naar `radio`. Daar staan alle functies die te maken hebben met berichten sturen en ontvangen.

Deze functies zullen we nodig hebben. Lees goed de hele uitleg (klik op *Show more*!).
- `radio.config()`
- `radio.on()`
- `radio.send()`
- `radio.receive_full()`

Het is belangrijk dat we de functie `radio.receive_full()` (en bvb. niet gewoon `radio.receive()`) zodat we ook de signaalsterkte kunnen uitlezen.

Probeer zelf volgende programmas te maken:
- Schat: stuurt de hele tijd een bericht (bvb `"hallo"`)
- Zoeker: ontvangt berichten en toont het ontvangen bericht op het scherm (display)

Tips:
- Om de `radio` functies te kunnen gebruiken moet je die module eerste importen met `import radio`.
- Zorg dat beide micro:bits dezelfde `group` gebruiken. Die kan je installen met `radio.config()`.
- Vergeet de "radio` ook niet aan te zetten!
- Het is belangrijk om tussen het sturen en ontvangen van berichten even te wachten (`sleep`). De lus van elk programma ziet er dan ongeveer zo uit:

```python
while True:
    # stuur bericht, of
    # ontvang bericht - als ontvangen toon op scherm
    sleep(200)
```
