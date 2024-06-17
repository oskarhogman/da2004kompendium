\chapter{Tillämpningar: algoritmer}

# Iteration och rekursion för sortering

Under veckan har vi sett tre sätt att repetera en kodsnutt flera
gånger i Python:

- `for` loopar
- `while` loopar
- rekursion

Loopar är generellt snabbare, men rekursion kan leda till kortare och
mer lättläst kod. I labb 3 ska ni använda dessa tekniker för att
implementera två olika sorteringsalgoritmer.

**TODO**: lägg till "kontrollflöde med `pass`, `continue`, `break`,
`return`"

## Summan av listelement

Låt oss säga att vi vill beräkna summan av elementen i en lista. Detta
kan göras på många olika sätt med både `for`, `while` och rekursion.

Vi kan använda en `for` loop över alla index i listan på följande
sätt:

```python
def sum_for(xs):
    s = 0
    for i in range(len(xs)):
        s += xs[i]
    return s

print(sum_for([1,2,3,4]))
```

Med Pythons `for` kan vi även direkt iterera över alla element i
listan:

```python
def sum_for(xs):
    s = 0
    for x in xs:
        s += x
    return s

print(sum_for([1,2,3,4]))
```

Detta sätt är mer "pythonskt" än att iterera över index.

Detta program kan skrivas med en `while` loop över index också:

```python
def sum_while(xs):
    s = 0
    i = 0
    while i < len(xs):
        s += xs[i]
        i += 1
    return s

print(sum_while([1,2,3,4]))
```

Men ännu en gång är detta inte så pythonskt och vi kan direkt iterera
över listan istället:

```python
def sum_while(xs):
    s = 0
    while xs:  # kom ihåg att tomma listan motsvarar False!
        s += xs.pop()
    return s

print(sum_while([1,2,3,4]))
```

Låt oss slutligen skriva detta program med rekursion:

```python
def sum_rec(xs):
    if xs == []:
        return 0
    else:
        x = xs.pop()
        return (x + sum_rec(xs))

print(sum_rec([1,2,3,4]))
```

Vi måste dock vara lite försiktiga om vi använder de två sista
versionerna av summeringsfunktionen då de tömmer indata listan!

```python
xs = [1,2,3,4]

print(sum_rec(xs))

print(xs) # xs har tömts!
```

För att detta inte ska hända måste vi först kopiera listan:

```python
xs = [1,2,3,4]

print(sum_rec(xs.copy()))

print(xs) # xs har inte tömts!
```

Listor i Python är muterbara (eng. *mutable*), dvs
förändringsbara. Funktioner kan alltså ändra en lista som är
definierad utanför funktionen. På grund av detta är det lite farligt
att skicka in listor till funktioner i Python och man måste ibland
använda copy() som ovan.

En annan lösning är att inte använda funktioner som ändrar
listan. Många grejer kan göras direkt med indexering och slicing:

```python
def sum_rec(xs):
    if xs == []:
        return 0
    else:
        return (xs[0] + sum_rec(xs[1:]))

xs = [1,2,3,4]

print(sum_rec(xs))

print(xs) # xs har inte tömts!
```

Slicen `xs[1:]` betyder `xs[1:len(xs)]`.

För labb 3 kan det vara väldigt bra att inte använda .pop, .remove,
etc.

## Repetition: quicksort

I förra föreläsningen såg vi en implementation av quicksort. Detta är
en snabb och relativt lättimplementerad sorteringsalgoritm uppfanns av
Tony Hoare 1959
(<https://en.wikipedia.org/wiki/Quicksort#History>). Den fungerar på
följande sätt:

1. Välj ett element i listan ("pivotelementet").

2. Dela upp listan i två dellistor: en med alla element som är mindre
   än pivotelementet och en med alla element som är större än
   pivotelementet.

3. Sortera dellistorna genom rekursion. Basfallet är tomma listan
   vilken redan är sorterad.

4. Sätt ihop listorna med pivotelementet i mitten.

Detta implementeras enkelt i Python:

```python
def quick_sort(xs):
    if xs == []:
        return xs
    else:
        p = xs[0]
        tail = xs[1:]
        s = quick_sort([ x for x in tail if x <= p ])
        g = quick_sort([ x for x in tail if x > p ])
        return (s + [p] + g)

print(quick_sort([6,3,2,1,5]))
```

## Selection sort

En annan sorteringsalgoritm är selection sort
(<https://en.wikipedia.org/wiki/Selection_sort>). Den fungerar på
följande sätt:

1. Dela upp listan i två dellistor med sorterade och osorterade
   element --- i början är ju alla element osorterade, så den
   sorterade listan är tom.

2. Så länge som den osorterade listan är tom ta ut det minsta (eller
   största) elementet och sätt in det först (eller sist) i den
   sorterade listan.

Så här kan vi implementera det i Python:

```python
def selection_sort(xs):
    sorted = []
    while xs:
        x = min(xs)
        xs.remove(x)
        sorted.append(x)
    return sorted

print(selection_sort([6,3,2,1,5]))
```

I labb 3 ska ni implementera de två sorteringsalgoritmerna permutation
sort och insertion sort.





