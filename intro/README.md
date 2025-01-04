# Beginnen met Micro:bit

## De Micro:bit Python editor

Een editor is een applicatie waarin je code voor je programmas schrijft. Om 'gewone' Python code te schrijven hebben we bijvoorbeeld VSCode gebruikt. Om Python code voor de Micro:bit te schrijven zullen we micro:bit Python editor gebruiken. Hiervoor hoe je niets te installeren want als werkt gewoon via een website.

Dit is de makkelijkste manier om Python code voor de micro:bit te schrijven en je programma naar de micro:bit te sturen. Jammer genoeg is de editor nog niet in het nederlands vertaald dus je zult je beste engels moeten bovenhalen!

De website is https://python.microbit.org/v/3.

Belangrijk: de website werkt met de meeste browsers maar programmas naar de micro:bit sturen werkt enkel met Chrome of Edge. Zorg dus dat je met een van deze twee browsers werkt!

## Je eerste Micro:bit programma

Als je voor de eerste keer naar de website gaat krijg je normaal gezien de volgende code te zien:

```python
# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.HEART)
    sleep(1000)
    display.scroll('Hello')
```

Wat gebeurt er in dit programma?
1. `from microbit import *` importeert alles uit het `microbit` pakket. Hiervan gebruikt het programma enkel `display`, `sleep` en `Image`.
2. De `display.show()` functie 'toont' (show) iets op het scherm (display) van de Microbit. Wat? Een `Image.HEART`, ofwel een tekening van een hart.
3. Met `sleep(1000)` wacht het programma 1 seconde (1000 miliseconde).
4. De `display.scroll()` functie laat de tekst `Hello` over het scherm 'rollen' (scroll).
5. De vorige 3 stappen worden oneindig herhaald door de `while True` lus.

Goed voor een eerste test!
1. Sluit je micro:bit aan op een USB poort van de computer.
2. Click onderaan op de knop _Send to micro:bit_ en dan twee maal op _Next_.
3. Je ziet nu een venster met de verbonden micro:bit (bvb. _BBC micro:bit CMSIS-DAP - paired_). Klik op de micro:bit en dan op _Connect_.
4. Als alles goed ging voert de micro:bit nu het programma uit!

In the Python editor kan je ook altijd op voorhand het programma testen door op de play knop te klikken in de afgebeelde micro:bit, rechts bovenaan.

## De Reference gebruiken

Helemaal links in de editor zie je drie knoppen: _Reference_, _Ideas_ en _API_. Klik op _Reference_. Hier kan je informatie vinden over alle Python functies die je kan gebruiken om met de micro:bit te werken.

Klik op _Display_ om meer informatie te krijgen over wat we met het display (scherm) kunnen doen. Je kan telkens om _More_ klikken om extra informatie te krijgen over een bepaalde functie.

Om te beginnen zien we bijvoorbeeld de `Image.HEART` die in ons eerste programma gebruikt is. Maar er zijn nog veel meer afbeeldingen. Kies er een uit (bvb. `Image.SILLY`) en pas het programma aan door `Image.HEART` te vervangen. Test je aanpassing uit door het programma opnieuw naar de micro:bit te sturen of door rechtstreeks in de editor te testen.

Klik nu terug op _Reference_ en dan op _Buttons_. Hier kunnen we leren hoe we de knoppen op de micro:bit kunnen gebruiken. In het eerste voorbeeld zien we deze code:

```python
while True:
    if button_a.was_pressed():
        display.scroll('A')
```

`button_a` stelt de knop A voor (de knop links van het display) en die `button_a` heeft een functie `was_pressed()` die `True` (waar) zal geven als de knop ingedrukt is, of `False` (vals) indien niet. Als (`if`) de knop ingedrukt is toont het programma de letter `A` op het display.

Past het programma aan zodat deze nieuwe code gebruikt wordt. Let op: in je programma staat al een `while: True` lus! Je kan ook alles vervangen in het programma zodat enkel `A` wordt getoond.

Probeer nu zelf het programma uit te breiden zodat de letter `B` wordt getoond als de knop B (rechts van het display) in wordt gedrukt.

Om af te sluiten bekijken we een laatse functie. Klik terug op _Reference_ en dan op _Temperature_. Op de micro:bit zit ook een thermometer. De functie `temperature()` geeft de huidige temperatuur. Het resultaat van die functie tonen we op het scherm met de functie `display.scroll()`. Probeer de code uit in je programma. Klopt de temperatuur?
