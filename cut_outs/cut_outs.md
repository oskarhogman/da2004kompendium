# Mer om funktioner #

Vi gillar funktioner därför att de...

- samlar kod i lätthanterliga och återanvändbara delar
- är bra för att undvika upprepning av kod
- inför *abstraktioner* => förenklar avancerade program ( Exempel: funktion som itererar över "sekvens", sekvens abstraktion av lista, tupel, mängd, etc)
- gör programmet mer lättläst:
    * Tydliggör beroenden i koden: "indata" som argument, resultat efter 'return'
    * Bra kodenhet för dokumentation
    * Bra kodenhet för _testning_



## Dokumentation ##

Två sätt att dokumentera i Python:

* Dokumentationssträngar

    – Primära dokumentationsmetoden
    – Används för att dokumentera funktioner. Prova skriv help(print) i Python-tolken
* Kommentarer

    – Används för att förklara beräkningssteg, typiskt enskilda rader eller små block med

Dokumentationssträngar är beskrivna i PEP-257: 

> The docstring [...] should summarize its behavior and document its arguments,
> return value(s), side effects, exceptions raised, and restrictions on when it can be called (all
> if applicable). Optional arguments should be indicated. It should be documented whether keyword
> arguments are part of the interface.


Allmän princip: förklara det som inte framgår av identifierare (dvs variabelnamn, funktionsnamn, klassnamn, metodnamn).

* Om en variabel heter `partial_sum` så behövs ingen kommentar som säger samma sak. Möjligen kan det
  vara bra att nämna varför variabeln behövs.
* Om en funktion heter `compute_integral` så behöver inte dokumentationssträngen säga samma
  sak. Däremot kan det vara bra att skriva om vilken algoritm som används, vilka antaganden man har
  på parametrar, och vad som gäller för returvärdet.


```python
def square(x):
    """Description of square function
    Parameters:
    x (int): input number
    Returns:
    int: Square of x
    """
    return x*x
```

```python
help(square)
```

```python
def main(x):
    y = square(x + 2) # Takes the square of x + 2
    do more stuff...
```


## Funktionens anatomi ##

Peka ut definition ("kropp") och huvud ("signatur") på funktionen.

* Huvudet har en parameterlista.
* Det vi skickar in till funktionen kallas argument
* Ordet parameter har två betydelser.
  - Variabler i huvudet kallas _formella parameterar_.
  - De värden man ger vid ett anrop till en funktion kallas _anropsparametrar_.
* Kroppen har en dokumentationssträng följt av satser, och är indragen.
* Indragningen är viktig!

Kroppen avslutas ofta med `return` av ett värde. Om `return` saknas så returneras
värdet `None`. Märk: man kan stoppa in `return` lite var som helst i en funktion.

Parameterlistan kan vara tom. Ex:
```python
def print_menu():
   print("1. Do this")
   print("2. Do that")
```


## Multipla returvärden ##

Vi har returnerat värden från funktioner med `return`, men hur gör man om man vill returnera flera
värden? Det finns flera dåliga sätt att lösa detta, men ett bra: multipla returvärden.

```python
def integer_div(nominator, denominator):
    q = nominator // denominator
    r = nominator % denominator
    return q, r
```
Denna lilla funktion kan man sedan anropa så här:
```python
quotient, remainder = integer_div(17, 10)
```

Till exempel är print en fördefinerad funktion som tar flera värden och har standardvärden.
```python
>>> print('hej','du')
hej du
>>> print('hej','du',sep='\n')
hej
du
```

Ett till exempel: Antag att man vill extrahera konsonanter och vokaler ur en sträng:
```python
def characters(s):
    s_vowels = dict()
    s_consonants = dict()
    vowels = 'aeiouyåäö'
    consonants = 'bcdfghjklmnpqrstvxz'
    for ch in s:
        if ch in vowels:
            s_vowels[ch] = None
        elif ch in consonants:
            s_consonants[ch] = None
    return s_vowels.keys(), s_consonants.keys()   
```

## Skönsvärden ##

Det är vanligt att man skriver funktioner med parametrar som nästan alltid sätts till samma värde.
Python låter dig ange explicit sådana vanliga värden: "skönsvärden" (eng: _default values_).

Låt oss skriva en funktion som tar en sträng och bryter upp den i smådelar där man hittar en blank som separator.
```python
def split(s):
    res = []
    term = ''
    for ch in s:
        if ch == ' ':
            if term:
                res.append(term)
                term = ''
	else:
            term += ch
    if term:
        res.append(term)
    return res
```
Hur använder man denna funktion?

Säg att vi vill generalisera detta till många olika möjliga separatorer:
```python
def split(s, sep):
    res = []
    term = ''
    for ch in s:
        if ch in sep:
            if term:
                res.append(term)
                term = ''
	else:
            term += ch
    if term:
        res.append(term)
    return res
```
Nu måste man alltid ange två argument, trots att det vanligaste användningsfallet är med mellanslag som separator.
Det är här skönsvärden kommer in:
```python
def split(s, sep=' '):
    res = []
    term = ''
    for ch in s:
        if ch == ' ':
            if term:
                res.append(term)
                term = ''
	else:
            term += ch
    if term:
        res.append(term)
    return res
```
Vi kan nu anropa funktionen med ett _eller_ två argument.

* OBS: notera att det finns en variant på `split` inbyggd i Python.


## Nyckelordsparametrar ##

Python låter dig namnge parametrar även i anropen. 
__Exempel__: `integer_div(denominator=10, nominator=17)` ger samma effekt som
anropet `integer_div(17, 10)`. 

* `print` har flera nyckelordsparametrar:
    - `sep=' '` — dvs ett mellanslag som separator
    - `end='\n'` — backslash-n betyder radbrytning.
    - `file=sys.stdout` — Låt utdata gå till terminalen




# Labb 5: Game of Life

Conway's Game of Life är en "cellular automaton" uppfunnen 1970 av
matematikern John Conway
(<https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life>). Det är ett
spel med 0 spelare där man interagerar med spelet genom att sätta upp
ett starttillstånd och sedan observera hur spelet utvecklas.

Spelet spelas på ett bräde av celler som antingen lever eller är
döda. Vi kommer representera celler som rutor på ett bräde (världen)
där de som är vid liv är svarta medans de som är döda är vita. Nästa
tillstånd i spelet beräknas genom att applicera följande 3 regler:

1. Alla levande celler med två eller tre grannar överlever.
2. Alla döda celler med tre levande grannar återupplivas.
3. Alla andra levande celler dör och redan döda celler fortsätter vara döda.

Med grannar menas de 8 celler som angränsar till cellen, så cellen med
koordinater `(2,3)` har grannar
`[(1,2),(2,2),(3,2),(1,3),(3,3),(2,4),(3,4),(4,4)]`.

Så om världen (här skriven som en lista) har en rad med 3 celler
[(1,1), (2,1), (3,1)] så kommer nästa tillstånd vara:

[(2,0), (2,1), (2,2)]

Nästa tillstånd efter det kommer vara:

[(1,1), (2,1), (3,1)]

Så en rad med tre element hoppar mellan dessa två tillstånd. Det finns
många andra starttillstånd som leder till mer komplexa mönster:
<https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns.>

Labben går alltså ut på att implementera Game of Life samt testa några
olika starttillstånd. Vi kommer representera celler och världen på
följande sätt:

- En klass `Cell` med två tal `_x` och `_y` vilka representerar
cellens koordinater (så en cell innehåller samma data som en tupel)
med följande metoder:
  * `__init__`: Konstruktor för celler.
  * `coordinates`: Returnerar koordinaterna som en tupel.
  * `neighbors`: Returnera en lista av alla grannar till cellen.
  * `__eq__`: Likhetstest för celler (jämför bara deras koordinater).
  * `__hash__`: Hashfunktion för celler (nödvänding för att celler ska
    kunna användas som nycklar i en uppslagstabell).
- En uppslagstabell från `Cell` till `bool` som representerar världen.
  * En cell som är vid liv mappas till `True`.
  * En cell som är död är inte med i uppslagstabellen.

Labben har följande uppgifter:

- 1a: implementera `coordinates`
- 1b: implementera `neighbors`
- 2: skriv en funktion som genererar en slumpmässig värld.
- 3: implementera en funktion som tar in en värld och returnerar en
     värld där reglerna har applicerats (dvs, spelets nästa
     tillstånd).

Större delen av koden för labben finns redan skriven i filen
`gameoflife.py`. Er uppgift är att fylla i alla `pass`. Vi kommer
använda ett litet grafikbibliotek för att animera världen och för att
"gameoflife.py" ska ladda i Python måste ni hämta hem:

<https://mcsp.wartburg.edu/zelle/python/graphics.py>

Om ni sedan sparar detta i samma mapp som `gameoflife.py` så ska allt
fungera. Får ni problem kom på ett labbpass så kan handledarna hjälpa
er.



# Från kap 11, men urklippt/borttaget från 10
#  Lite mer exempel av arv: geometriska figurer

\anders{Inklippt från kapitel 11. Vi behöver nog inte göra allt jag gjorde här.}

Låt oss säga att vi håller på att skriva ett ritprogram och vill
representera geometriska figurer, typ cirklar, rektanglar,
kvadrater... Dessa ska alla ha färg och en `bool` som säger om de är
ifyllda eller inte. Vi kan då skapa en superklass `Shape` som
innehåller denna specifika information som gäller för alla figurer och
de olika geometriska figurerna kan sedan ärva dessa egenskaper från
`Shape` klassen:

```python
class Shape:

    def __init__(self, color='black', filled=False):
        self._color = color
        self._filled = filled

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_filled(self):
        return self._filled

    def set_filled(self, filled):
        self._filled = filled
```

Vi kan nu definiera en rektangel som en `Shape` som även har en längd
och höjd, samt metoder för att beärkna dessa area och omkrets:

```python
class Rectangle(Shape):

    def __init__(self, length, height):
        super().__init__()
        self._length = length
        self._height = height

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def get_area(self):
        return self._length * self._height

    def get_perimeter(self):
        return 2 * (self._length + self._height)
```

En cirkel är även den en `Shape`, men med radie istället för höjd och
bredd:

```python
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def get_area(self):
        return 3.14 * self._radius ** 2

    def get_perimeter(self):
        return 2 * 3.14 * self._radius
```

Vi kan sedan instansiera dessa klasser och manipulera dem var för sig:

```python
rect = Rectangle(10, 3)

print("Area of rect:", rect.get_area())
print("Perimeter of rect:", rect.get_perimeter())
print("Color of rect:", rect.get_color())
print("Is rect filled?", rect.get_filled())
rect.set_filled(True)
print("Is rect filled? ", rect.get_filled())
rect.set_color("orange")
print("Color of rect:", rect.get_color())

circ = Circle(2)

print("\nArea of circ:", format(circ.get_area(), "0.2f"))
print("Perimeter circ:", format(circ.get_perimeter(), "0.2f"))
print("Color circ:", circ.get_color())
print("Is circ filled?", circ.get_filled())
circ.set_filled(True)
print("Is circ filled? ", circ.get_filled())
circ.set_color("blue")
print("Color of circ:", circ.get_color())
```

## `graphics.py`

Biblioteket `graphics.py` som används i labb 5 innehåller en massa
geometriska figurer, samt funktioner för att rita upp dom. För en
tutorial se:
<http://anh.cs.luc.edu/handsonPythonTutorial/graphics.html>

Här är ett litet exempel på hur man kan rita:

```python
from graphics import *

win = GraphWin("Cool window", 600, 600)
win.setBackground("white")

head = Circle(Point(300,300), 100) # set center and radius
head.setFill("yellow")
head.draw(win)

eye1 = Circle(Point(260,275), 10)
eye1.setFill('blue')
eye1.draw(win)

eye2 = Circle(Point(340,275), 10)
eye2.setFill('blue')
eye2.draw(win)

nose = Circle(Point(300,312), 5)
nose.setFill('red')
nose.draw(win)

mouth = Oval(Point(260, 350), Point(340, 350))
mouth.setWidth(10)
mouth.draw(win)

win.getMouse()
win.close()
```

Vi kan även göra animationer:

```python
import time

win = GraphWin('Back and Forth', 300, 300)

cir1 = Circle(Point(40,100), 25)
cir1.setFill("yellow")
cir1.draw(win)

while (cir1.getCenter().getX() + cir1.getRadius() < 300):
    cir1.move(5, 0)
    time.sleep(.05)

while (cir1.getCenter().getX() - cir1.getRadius() > 0):
    cir1.move(-5, 0)
    time.sleep(.05)

win.close()
```

## Turtle graphics

Ett annat roligt sätt att rita är "turtle graphics", se:

<https://docs.python.org/3.3/library/turtle.html?highlight=turtle>

<https://github.com/thomasmarsh/python-turtle/blob/master/turtle.md>


