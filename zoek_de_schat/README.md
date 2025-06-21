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

Het is belangrijk dat we de functie `radio.receive_full()` gebruiken (en bvb. niet gewoon `radio.receive()`) zodat we ook de signaalsterkte kunnen uitlezen.

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

## Stap 2: Signaalsterkte van de schat

Om te weten hoe dicht de zoeker bij de schat is moet de zoeker de signaalsterkte van de berichten van de schat onderzoeken.

Als we een bericht ontvangen met `bericht = radio.receive_full()` krijgen we eigenlijk een lijst met 3 dingen in:
1. `bericht[0]` bevat de teks in het bericht. Die hebben we nu eigenlijk niet nodig.
2. `bericht[1]` bevat de signaalsterkte! Dit is een getal tussen -255 en 0. Hoe groter hoe beter het signaal. In werkelijkheid zal je signaalsterkes krijgen tussen ongeveer -120 en -20.
3. `bericht[2]` bevat het tijdstip dat het bericht ontvangen werd. Hebben we ook niet nodig.

Zorg er voor dat het programma van de zoeker de signaalsterkte telks op het display laat zien. We kunnen nu al eens testen wat er gebeurt als de zoeker dichter of verder van de schat is.

## Stap 3: Signaalsterke omzetten

We willen eigenlijk de leds van de zoeker aanzetten in functie van de signaalsterkte. Hoe beter het signaal, hoe meer leds er moeten aan staan. We hebben 25 leds. We moeten tussen een manier vinden om de signaalsterkte (bvb tussen -120 en -20) om te zetten naar een getal tussen 0 en 25. -120 wordt dan 0 en -20 wordt 25.

Hiervoor hebben we een paar wiskundige berekeningen nodig. Je kan deze functie gebruiken:

```python
def omzetten(waarde, in_min, in_max, uit_min, uit_max):
    waarde = min(max(waarde, in_min), in_max)
    in_verschil = in_max - in_min
    uit_verschil = uit_max - uit_min
    waarde_geschaald = (waarde - in_min) / in_verschil
    return uit_min + (waarde_geschaald * uit_verschil)
```

De `waarde` is een getal tussen `in_min` en `in_max` en wordt omgezet in een getal tussen `uit_min` en `uit_max`.

Gebruik de functie om een signaalsterkte om te zetten naar een getal tussen 0 en 25, en toon dit getal op het display.

## Stap 4: Een functie om een aantal leds aan te zetten
