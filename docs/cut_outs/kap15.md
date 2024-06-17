\chapter{Sammanfattning}

# Labb 6 uppgift 2d

Många har mailat mig och frågat om uppgift 2d:

*Skriv `create_all_pairs_rec(xs,ys)` med bara funktionen `map` och
 rekursion (så funktionen ska anropa sig själv och ej använda varken
 for, while eller listomfattningar).*

Här är koden för en enklare funktion som bara parar ihop elementen i xs och ys:

```python
def create_pairs(xs,ys):
    if xs == [] or ys == []:
        return []
    else:
        x, y = xs[0], ys[0]
        return [(x,y)] + create_pairs(xs[1:],ys[1:])

print(create_pairs([1,2], [3,4]))
print(create_pairs([1,2,10], [-2,3]))
print(create_pairs([], [1,2,3]))
print(create_pairs([2,3,1], []))
print(create_pairs(['a'], [1,2,3]))
```

För uppgift 2d kan vi istället para ihop `xs[0]` med alla element i
`ys` med hjälp av `map(lambda y: (xs[0],y),ys)`.

# Projektet

Projektet (3hp) ligger nu uppe: implementera Kalaha. Genomgång av
Kalaha och projektbeskrivningen på tavlan.

Två uppgifter:
- Simulera Kalaha
- Spela Kalaha

För betyg E-C behöver man lösa en av uppgifterna. För E-A behöver man
lösa båda uppgifterna. För att få högre betyg än E måste man uppfylla
ett eller flera av de 4 kriterierna beskrivna i "Generella
instruktioner":

* Kriterie 1: väl valda identifierare och informativa kommentarer
* Kriterie 2: god struktur på koden
* Kriterie 3: god felhantering
* Kriterie 4: dokumenterad utprovning av programmet

Inlämning på PeerGrade senast onsdag 8/1 kl 20:00.

Granskningen ska vara klar senast söndag 12/1 kl 20:00.

# Kurssammanfattning

Kursmål: komma igång med grundläggande programmering i Python genom
att

- Skriva egna, relativt små, program.
- Läsa andras kod.
- Kunna realisera en algoritmbeskrivning i kod.

Vi har gått igenom följande i kursen:

* Input/output (`print` och `input`)
* Aritmetiska operationer (`+`, `-`, `*`... för olika typer)
* Boolska uttryck (`and`, `or`, `not`)
* Villkorssatser (`if`, `elif`, `else`)
* Funktioner (`def`, `return`)
* Globala och lokala variabler
* Listor (muterbara, `range`, slicing, listomfattningar)
* Iteration med `for` och `while`
* Rekursion
* Filhantering (`with`)
* Högre ordningens funktioner (`lambda`)
* Generatorer (`yield`)
* Moduler (`import`, `from`, `as`)
* Felhantering (exceptions, `try`, `except`, `raise`)
* Datastrukturer och typer:
  - Uppslagstabeller (eng. *dictionaries*)
  - Mängder
  - Sekvenser (listor, tupler, strängar)
* Objektorientering (`class`, instanser, metoder, arv, interface/gränssnitt)
* Assertions och defensiv programmering (`assert`)
* Testning (manuell/automatisk testning, enhetstester (unittest))

# Exempel på utvalda delar

## Input/output (`print` och `input`)

För att skriva ut något använda `print`:

```python
print(42)
print('hej')
```

**Obs**: glöm inte att konvertera till `str` om du vill göra något med
  strängar innan utskrift:

```python
print('hej' + str(42))
```

För att läsa in något från användaren använd `input`:

```python
namn = input("Vad heter du? ")
print('Hej ' + namn)
```

**Obs**: glöm inte att konvertera från `str` om du vill göra något med
  det som använder skrivit.

```python
age = input("Hur gammal är du? ")
print(namn + " är född " + str(2019 - int(age)))
```

## Aritmetiska operationer (`+`, `-`, `*`... för olika typer)

Python stödjer de normala räknesätten:

* addition (`+`)
* subtraktion (`-`)
* multiplikation (`*`)
* division (`/`)
* heltalsdivision (`//`)
* exponentiering (`**`)
* modulus/rest (`%`)

Vi kan utföra aritmetiska operationer på olika typer:

```python
print(3 * 42)
print(3 * 'hej')
```

## Boolska uttryck (`and`, `or`, `not`)

`x and y` är `True` omm både `x` och `y` är.

`x or y` är `True` omm någon av `x` och `y` är.

`not x` är `True` om `x` är `False` och `False` annars.

  x         y          x `and` y          x `or` y           (`not` x `or` `not` y) `and` (x `or` y)
------   ------     --------------     --------------     ---------------------------------------------
`True`   `True`     `True`             `True`             ?
`True`   `False`    `False`            `True`             ?
`False`  `True`     `False`            `True`             ?
`False`  `False`    `False`            `False`            ?

## Villkorssatser (`if`, `elif`, `else`)

Här är ett exempel på en `if`-`elif`-`else` sats:

```python
temp = int(input('Hur kallt är det? '))
if temp < -30:
    print('Mycket kallt')
elif temp < 0:
    print('Kallt')
elif temp == 0:
    print('Noll')
elif temp < 30:
    print('Varmt')
else:
    print('Mycket varmt')
```

## Funktioner (`def`, `return`)

Funktioner definieras med `def` och returnerar något med `return`.

```python
def integer_div(nominator, denominator):
    q = nominator // denominator
    r = nominator % denominator
    return q, r
```

Denna  funktion kan man sedan anropa så här:

```python
quotient, remainder = integer_div(17, 10)
```

**Obs:** om det står "skriv funktionen f som **returnerar** ..." på
  tentan så ska `return` användas i f (så ni ska inte använda
  `print`).

## Globala och lokala variabler

Globala variabler är tillgängliga överallt i programmet.

Lokala variabler är endast tillgängliga "lokalt", exempelvis i kroppen
för en funktion.

Om `x` är global och vi sedan skriver över den lokalt i funktionen så
är dess värde oförändrat utanför funktionen:

```python
x = 5

def foo():
    x = 10
    print("local x:", x)

foo()
print("global x:", x)
```

Samma sak händer med funktionsargument:

```python
x = 5

def foo(x):
    print("local x:", x)

foo(12)
print("global x:", x)
```

Det är viktigt att förstå var olika variabler är synliga!

## Listor (muterbara, `range`, slicing, listomfattningar)

Listor i Python är muterbara:

```python
xs = [1,2,3,4]

def foo(xs):
    x = xs.pop()
    print(x)

foo(xs)  # 4
foo(xs)  # 3

print(xs)  # [1, 2]
```

Man kan hämta ut alla element med index `i < j` genom `xs[i:j]`. Detta
kallas för *slicing*. Skriver vi `xs[:j]` får vi allt från början till
index `j-1`. Skriver vi `xs[i:]` så får vi allt från index `i` till
slutet av listan. Skriver vi `xs[:-1]` får vi allt utom sista
elementen (kom ihåg att genom att indexera med negativa tal indexerar
vi från slutet av listan).

```python
>>> xs = [0,1,2,3]
>>> xs[:2]
[0, 1]
>>> xs[2:]
[2, 3]
>>> xs[:-1]
[0, 1, 2]
>>> xs[:-2]
[0, 1]
>>> xs[-1:]
[3]
```

Listomfattningar låter oss skapa listor på ett enkelt sätt:

```python
>>> [x for x in range(20) if x % 2 == 1]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

## Iteration med `for` och `while`

Då vi har sett så många exempel med `for` och `while` kommer jag
istället fokusera på rekursion.

**Obs:** kan iterera över bokstäver i strängar med `for`.

```python
for c in 'hej':
    print(c)
```

## Rekursion

Låt oss skriva en rekursion funktion som kostar bort `n` element ur en
lista `xs`.

```python
def drop(n,xs):
    if n == 0 or xs == []:
        return xs
    else:
        return drop(n-1,xs[1:])

print(drop(2,[1,2,3,4]))
```

## Filhantering (`with`)

```python
with open('ut.txt', 'w') as out:
     out.write("hej hopp")
```

## Högre ordningens funktioner (`lambda`)

HOF = funktioner som tar in funktioner och/eller returnerar
funktioner.

```python
f = lambda x, y: 2 * x + y

print(f(3,4))
```

map:

```python
print(list(map(lambda x: x**2, [1,2,3,4])))
print(list(map(lambda t: t[0], [[1,1], [0,2,1], [3,1,53,2]])))
print(list(map(len, ["hej","hopp"])))
```

filter:

```python
print(list(filter(lambda x: x % 2, range(10))))
```

Listomfattning vs. HOF:

```python
print([ x ** 2 for x in range(10) if x % 2 != 0 ])
print(list(map(lambda x: x ** 2,filter(lambda x: x % 2 != 0,range(10)))))
```

## Moduler (`import`, `from`, `as`)

Man kan importera moduler på ett antal olika sätt:

- `import m`: Tillåter att funktioner/variabler används med
punktnotation (dvs allt från modulen är importerat "qualified").

```python
import math
math.ceil(3.5)  # Avrunda uppåt
ceil(4.4)  # Fel!
```

- `from m import f1, f2, ...`: Tillåter användning av f1 och f2 i ditt
program.

```python
from math import ceil
ceil(3.5)
```

- `from m import *`: Gör allt från `m` tillgängligt.

**Varning:** detta anses orsaka dålig läsbarhet (och det är svårt att
veta vilka delar av en modul en annan modul beror på).

*Obs:* namn som börjar med `_` importeras inte.

- `import m as X`: Lättare hantera långa modulnamn.  Ex:

```python
import math as M
M.ceil(3.4)     # Praktiskt för långa modulnamn
```

- `from m import X as Y`: För att undvika namnkrockar. Ex:

```python
from math import gcd as libgcd

def gcd(a,b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

for a in range(2,10):
    for b in range(2,a):
        print(gcd(a,b) == libgcd(a,b))
```

## Felhantering (exceptions, `try`, `except`, `raise`)

try-except:

```python
while True:
    try:
        svar = input("Write a number (write 0 to quit): ")
        x = int(svar)
        if x == 0:
            print("Bye bye!")
            break
        else:
            print("The square of the number is: " + str(x ** 2))
    except:
        print("You must write a number!")
```

raise:

```python
def head(xs):
   if xs == []:
      raise Exception("head: input list is empty")
   else:
      return xs[0]
```

Finns många särfall definierade:

* `Exception`
* `ArithmeticError`
* `IOError`
* `IndexError`
* `MemoryError`
* `ZeroDivisionError`
* mmfl.

## Datastrukturer och typer:

- Uppslagstabeller (eng. *dictionaries*):

  Avbildning från icke-muterbara typer (strängar, siffror, tupler, men
  ej listor) till godtyckliga typer. Skrivs med måsvingar:

  ```python
  test = {'hopp': 4127, 'foo': 4098, 'hej': 4139, 12: 'hej'}
  ```

  Jättesnabbt att leta upp värdet givet en nyckel.

  ```python
  print(test['foo'])
  test['hej'] = 341
  ```

  Kan iterera över alla nycklar med `for`:

  ```python
  for k in test:
    print(k)
  ```

- Mängder: samling objekt, listor utan duplikationer.

- Sekvenser (listor, tupler, strängar)

  listor muterbara

  tupler och strängar omuterbara

## Objektorientering (`class`, instanser, metoder, arv, interface/gränssnitt)

En klass:

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

En klass som ärver från `Shape`:

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

Speciella metoder:

`__init__` - konstruktor

`__str__` - konvertera till sträng

# Läxa

* Plugga inför tentan! Programmera mycket för hand på papper. Ni kan
  sedan testa att mata in en era lösningar på datorn och se om de
  fungerar som de ska.

* Jobba på projektet.
