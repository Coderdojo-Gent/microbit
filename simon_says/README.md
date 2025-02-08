# Simon Says

## Intro

Je kent vast wel [het spel "Simon"](https://nl.wikipedia.org/wiki/Simon_(spel)) (of "Simon Says").

> Het spel laat een bepaalde toon horen, waarbij de overeenkomstige drukknop oplicht. De speler dient binnen een bepaalde tijd die knop in te drukken. Indien correct, hoort de speler deze toon opnieuw, gevolgd door een tweede toon. De speler dient dan de 2 overeenkomstige knoppen terug in te drukken. Vervolgens laat het spel 3 tonen horen, ... Dit blijft zo verdergaan tot de speler een fout maakt of te lang wacht.

![](https://nl.wikipedia.org/wiki/Simon_(spel)#/media/Bestand:Simon_game.jpg)

Onze micro:bit versie zal maar drie knoppen hebben: de twee drukknoppen A/B links en rechts, en de 'touch' knop met het logo bovenaan.

De knoppen van onze micro:bit kunnen natuurlijk ook niet oplichten. In de plaats kunnen we het ledje (lichtje) net naast de knop aan laten gaan.

## Stap 1: Led aan als knop ingedrukt

Om te beginnen willen we dat bij het indrukken van elke van de drie knoppen de juiste led event gaat branden.

Start met deze code:

```python
from microbit import *

while True:
    # Hier komt jou code
```

We gebruiken altijd een oneindige while lus zodat ons programma blijft draaien en telkens kijkt of er een knop is ingedrukt.

We moeten dus code schrijven die het volgende doet:
- ALS knop a is ingedrukt DAN zet de led op positie x=0 en y=2 aan
- ALS knop b is ingedrukt DAN zet de led op positie x=4 en y=2 aan
- ALS logo is ingedrukt DAN zet de led op positie x=2 en y=0 aan

Gebruik de _reference_ in de micro:bit editor om meer te leren over de functies die je nodig hebt.

Tips:
- De functie `button_a.is_pressed()` checkt of knop A ingedrukt is.
- De functie `display.set_pixel` kan je gebruiken om 1 enkele led (pixel) aan te zetten

Als je dit gelukt is zie je waarschijnlijk een klein probleempje: de juiste led gaat wel aan, maar hij gaat niet meer uit! Met de functie `display.clear()` kunnen we alle leds terug uitzetten.

Maar nu is er een nieuw probleem! De ledjes gaan maar heel even aan. Om ze iets langer te doen branden kan je de functie `sleep()` gebruiken. Tussen de haakje zet je een getal om te bepalen hoe lang het programma hier moet wachten (slapen). Het getal is in miliseconden. 1000 miliseconden is 1 seconde. Probeer verschillende waardes uit en kies wat voor jou het beste is.

## Stap 2: Geluid toevoegen

De juiste led gaat nu branden als we een knop indrukken. Maar daat hoort ook geluid bij!

Met de functie `music.play()` kan je een of meer noten door de micro:bit laten spelen. Hiervoor moeten we wel eerste de model `music` importeren. Dat doe je door bovenaan je programma `import music` te zetten.

Zoek de functie op om er meer over te leren. Om een enkele noot af te spelen zet je de letter van de noot tussen de haakjes. Bvb. `music.play("D")` speelt de noot "D" (= een Re).

Kies zelf welke noten het je leukst vindt. Gebruik wel een verschillende noot voor elke knop!

Als je nu een knop indrukt moet de juiste led gaan branden _en_ een geluid afspelen.


## Stap 3: Een vaste reeks knoppen raden

Om te beginnen werken we met een vaste lijst van knoppen die moeten ingedrukt worden. Later laten we het programma zelf telkens een extra random knop toevoegen aan de lijst. Om aan te duiden welke knop we willen kunnen we bvb. een letter gebruiken: `"A"` en `"B"` voor de A en B knoppen en `"L"` voor het logo.

```python
te_raden = ["A", "B", "L"]
```

Nu moeten we, *voor* de `while` lus, de knoppen uit de lijst aanduiden (met de juiste led en geluid).

```python
for knop in te_raden:
    if knop == "A":
      # Werk zelf verder af
```

Tip: Je hebt dezelfde functies nodig die je in de vorige stappen al gebruikte.

Als dat gelukt is willen we nu de code *in* de `while` lus aanpassen:

ALS de eerste knop in de `te_raden` juist is ingedrukt DAN gaan we naar de volgende in de lijst. ANDERS is de speler verloren.

We kunnen de functie `te_raden.pop(0)` gebruiken om te weten wat het eerste element in de lijst is en tegelijk dat element uit de lijst te verwijderen.

Bvb:

```python
te_raden = ["A", "B", "L"]

test = te_raden.pop(0)
# Nu is test = "A"
# en te_raden = ["B", "L"]
```

Pas de code in de lus zo aan dat bij het indrukken van een knop wordt getest of dit de knop is de als eerste in de `te_raden` staat. Als dat fout is kunnen we de functie `reset()` gebruiken om het programma opnieuw de laten beginnen. Game Over!

Het is ook leuk als je tegelijk een apparte melodie afspeekt zodat de speler weet dat hij verloren is. Misschien kan je ook een bijpassende emoji op de display laten zien. Dit is een voorbeeldje maar je kan zelf iets verzinnen!

```python
display.show(Image.SKULL)
music.play(["F3:4", "D3:4", "B2:10"])
reset()
```

## Stap 4: Automatisch random knoppen

Ons programma is bijna af! In de vorige stap hebben we een vaste lijst, `te_raden`, met de knoppen. Dat is natuurlijk niet de bedoeling. Wat we willen is starten met 1 random knop. Als die juist wordt ingedrukt voegen we een tweede random knop toe. Nu moet de speler die twee knoppen, in de juiste volgorde, indrukken. Zo blijven knoppen toevoegen tot de speler een fout maakt.

We gaan nu *twee* lijsten nodig hebben. Een eerste lijst, `alle_knoppen`, met - je raadt het al - alle knoppen die tot nu toe toegevoegd zijn. Die lijst wordt dus steeds langer. Nadat we een knop toevoegen wordt de `te_raden` lijst een kopie van `alle_knoppen`. Telkens als de speler nu juist is wordt `te_raden` kleiner. Als `te_raden` leeg is heeft de speler alle knoppen juist geraden. Nu voegen we een nieuwe knop toe aan `alle_knoppen` en de speler kunnen opnieuwe raden.

Onze code zal er ongeveer zo uitzien:

```python
# In het begin zijn beide lijsten leeg
te_raden = []
alle_knoppen = []

while True:
    # ALS te_raden leeg is
    if not te_raden:
          # 1. Voeg een random knop toe aan alle_knoppen
          # 2. Maak een kopie van alle_knoppen in te_raden
          # 3. Toon alle te_raden knoppen aan de speler,
          #    dit is de code van stap 4, die komt dus nu IN de while lus

    # Deze code heb je al uit de vorige stappen!
    if button_a.is_pressed():
        # Eerste knop in te_raden = "A" ?
        # Indien fout, game over!
    elif button_b.is_pressed():
        # Eerste knop in te_raden = "B" ?
        # Indien fout, game over!
    elif pin_logo.is_touched():
        # Eerste knop in te_raden = "L" ?
        # Indien fout, game over!

    sleep(150)
    display.clear()
```

Tips:
- Om een random (willekeurige) letter A of B of L te krijgen kan je `random.choice(["A", "B", "L"])` gebruiken. Je moet dan wel `import random` toevoegen.
- Om een kopie van `alle_knoppen` te krijgen gebruik je `alle_knoppen.copy()`

Ons programma is af!

## Stap 5: Bonus - de code verbeteren

Als je naar het programma kijkt zul je zien dat er heel wat dingen verschillende keren herhaald worden. Bijvoorbeeld wat er gebeurd als een knop wordt ingedrukt, of wanner het game over it. Programmeurs zijn lui en herhalen niet krijg verschillende keren hetzelfde! We kunnen onze code verbeteren met eigen functies. We hebben al heel veel functies gebruikt maar we kunnen er ook zelf maken. Alles wat we in de functie zetten wordt dan uitgevoerd zelkens we die functie gebruiken!

Maak de volgende functies:

```python
def game_over():
    # De code wanneer het spel verloren is

def knop_a():
    # De code wanneer A ingedrukt wordt

def knop_b():
    # De code wanneer B ingedrukt wordt

def knop_l():
    # De code wanneer L ingedrukt wordt
```

Nu wordt de `while` lus veel korter en duidelijker:

```python
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
```
