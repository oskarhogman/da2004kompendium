\chapter{Tillämpningar: större program}

# Snake

Nu ska jag visa hur man kan tänka när man skriver ett lite större
program genom att implementera det klassiska spelet **Snake**. I
spelet styr man en orm som åker runt i ett fönster och äter mat i form
av fyrkanter. När ormen äter en bit mat växer den med en ruta. Om
ormen kör in i väggarna eller sig själv dör den och det är *game
over*.

Hur ska man tänka när man skriver ett större program som detta?

1. Vad är bra abstraktioner för programmet? Vilka attribut och metoder
   bör läggas ihop i en klass?

2. Vilken avancerad funktionalitet kommer jag behöva? Vilka bibliotek
   tillhandahåller detta för mig så att jag inte behöver skriva allt
   från grunden? (Googla: "writing games in python")

3. Hur ska själva huvuddelen av programmet fungera? Vilken typ av
   kontrollflöde kommer vi behöva?

För Snake har jag tänkt följande:

1. Ormen är en klass, `Snake`, med följande attribut:

   - Positionen för huvudet.
   - Positioner för kroppen.
   - Riktning den kör i (som kan vara 'UP', 'DOWN', 'RIGHT' och 'LEFT').

   Den har följande metoder:

   - `pos` och `body`: hämta de interna variablerna för positionen på
     huvudet och kroppen.
   - `setDir`: sätt riktningen på ormen.
   - `move`: flytta ormhuvudet ett steg framåt i riktningen den
     färdas.
   - `eat`: givet positionen på maten, avgör om ormen äter maten eller
     tappar en del av svansen.
   - `isGameOver`: har ormen krockat med väggarna eller sig själv?

   Jag har även en klass för spelet, `Game`, med följande attribut:

   - Storlek på fönstret (par med antal pixlar).
   - Storlek på rutorna i spelet (antal pixlar i bredd på de
     kvadratiska rutorna).
   - Poäng (antal ätna matbitar).
   - Positionen för maten.

   Den har följande metoder:

   - Funktioner för att hämta alla attribut.
   - Uppdatera positionen på maten (efter att ormen ätit en matbit).
   - Öka poängen med ett (efter att ormen ätit en matbit).

2. Funktionaliteten jag kommer behöva är: rita/animera, läs in
   knapptryckningar från användaren och reagera på dessa. Detta
   hanteras på smidigt av biblioteket `pygame`:
   https://www.pygame.org/ (installera i Anaconda eller genom `pip
   install pygame`).

3. Vi kommer först behöva initalisera och rita upp ett fönster med
   ormen. Ormen ska sedan flytta sig en ruta i taget och riktningen
   ska ändras om vi trycker på piltangenterna. Det som alltså händer i
   huvudloopen är något av:

   - Huvudet är på en matbit och vi äter maten och växer, matbiten
     dyker sedan upp på en ny slumpmässig position.
   - Vi har krockat med väggen eller oss själva och det är game over.
   - Ormen flyttar sig en ruta.


Jag har delat upp koden för Snake i flera sektioner där jag lägger in
mer och mer funktionalitet.

# `snakev0.py`: Initialisera ett fönster med ett ormhuvud

```python
import pygame
import time
import random

# Colors
red   = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

class Game():

    def __init__(self):
        self._delta = 10
        self._size = (400,400)

    def delta(self):
        return self._delta

    def size(self):
        return self._size

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")

    # Initialize the game
    game  = Game()
    delta = game.delta()

    # Make the window for the game
    win = pygame.display.set_mode(game.size())

    win.fill(black)

    # draw a green dot at position (100,50)
    pygame.draw.rect(win, green, pygame.Rect(100, 50, delta, delta))

    # update the display
    pygame.display.update()

    time.sleep(2)
    pygame.quit()
    exit()

main()
```



# `snakev1.py`: Skapa en klass för ormen och börja flytta ormhuvudet åt höger

```python
class Snake():

    def __init__(self):
        self._pos = (100,50)
        self._dir = "RIGHT"

    def pos(self):
        return self._pos

    def move(self, delta):
        d , (p1 , p2) = self._dir , self._pos

        if d == 'RIGHT':
            self._pos = (p1 + delta,p2)

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")

    # Initialize the game and snake
    game  = Game()
    snake = Snake()
    delta = game.delta()

    # Make the window for the game
    win = pygame.display.set_mode(game.size())

    # temporary counter
    i = 0

    while True:
        snake.move(delta)

        win.fill(black)

        sPos = snake.pos()
        pygame.draw.rect(win, green, pygame.Rect(sPos[0], sPos[1], delta, delta))

        pygame.display.update()
        time.sleep(.07)

        # run the game for 30 iterations
        if i == 30:
            pygame.quit()
            exit()
        i += 1
```



# `snakev2.py`: Gör så att ormhuvudet går att styra

**Obs**: man ska inte kunna vända riktning för då krockar man med sig själv!

```python
class Snake():

    def __init__(self):
        self._pos = (100,50)
        self._dir = "RIGHT"

    def pos(self):
        return self._pos

    def setDir(self, newDir):
        if self._dir == "RIGHT" and newDir != "LEFT":
            self._dir = newDir
        if self._dir == "LEFT" and newDir != "RIGHT":
            self._dir = newDir
        if self._dir == "UP" and newDir != "DOWN":
            self._dir = newDir
        if self._dir == "DOWN" and newDir != "UP":
            self._dir = newDir

    def move(self, delta):
        d , (p1 , p2) = self._dir , self._pos

        if d == 'RIGHT':
            self._pos = (p1 + delta,p2)
        if d == 'LEFT':
            self._pos = (p1 - delta,p2)
        if d == 'DOWN':
            self._pos = (p1,p2 + delta)
        if d == 'UP':
            self._pos = (p1,p2 - delta)

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")

    # Initialize the game and snake
    game  = Game()
    snake = Snake()
    delta = game.delta()

    # Make the window for the game
    win = pygame.display.set_mode(game.size())

    # temporary counter
    i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: snake.setDir('RIGHT')
                if event.key == pygame.K_LEFT: snake.setDir('LEFT')
                if event.key == pygame.K_UP: snake.setDir('UP')
                if event.key == pygame.K_DOWN: snake.setDir('DOWN')

        # Update snake position
        snake.move(delta)

        win.fill(black)

        sPos = snake.pos()
        pygame.draw.rect(win, green, pygame.Rect(sPos[0], sPos[1], delta, delta))

        pygame.display.update()
        time.sleep(.07)

        # run the game for 50 iterations
        if i == 50:
            pygame.quit()
            exit()
        i += 1
```



# `snakev3.py`: Ge ormen en kropp

```python
class Snake():

    def __init__(self):
        self._pos = (100,50)
        self._body = [(100, 50), (90, 50), (80, 50)]
        self._dir = "RIGHT"

    def move(self, delta):
        d , (p1 , p2) = self._dir , self._pos

        if d == 'RIGHT':
            self._pos = (p1 + delta,p2)
        if d == 'LEFT':
            self._pos = (p1 - delta,p2)
        if d == 'DOWN':
            self._pos = (p1,p2 + delta)
        if d == 'UP':
            self._pos = (p1,p2 - delta)

        self._body.insert(0, self._pos)

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")

    # Initialize the game and snake
    game  = Game()
    snake = Snake()
    delta = game.delta()

    # Make the window for the game
    win = pygame.display.set_mode(game.size())

    # temporary counter
    i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: snake.setDir('RIGHT')
                if event.key == pygame.K_LEFT: snake.setDir('LEFT')
                if event.key == pygame.K_UP: snake.setDir('UP')
                if event.key == pygame.K_DOWN: snake.setDir('DOWN')

        # Update snake position
        snake.move(delta)

        win.fill(black)

        for sPos in snake.body():
            pygame.draw.rect(win, green, pygame.Rect(sPos[0], sPos[1], delta, delta))

        pygame.display.update()
        time.sleep(.07)

        # run the game for 50 iterations
        if i == 50:
            pygame.quit()
            exit()
        i += 1
```



# `snakev4.py`: Lägg in mat och låt inte ormen växa om den inte äter

```python
class Snake():

    ...

    def eat(self,foodPos):
        if self._pos == foodPos:
            return True
        else:
            self._body.pop()

class Game():

    def __init__(self):
        self._size = (400,400)
        self._delta = 10
        self._foodPos = (300,50)

    def delta(self):
        return self._delta

    def size(self):
        return self._size

    def foodPos(self):
        return self._foodPos

    def newFoodPos(self):
        w , h = self.size()
        d     = self.delta()
        self._foodPos = (random.randrange(1, w // d) * d, random.randrange(1, h // d) * d)

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")

    # Initialize the game and snake
    game  = Game()
    snake = Snake()
    delta = game.delta()

    # Make the window for the game
    win = pygame.display.set_mode(game.size())

    # temporary counter
    i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: snake.setDir('RIGHT')
                if event.key == pygame.K_LEFT: snake.setDir('LEFT')
                if event.key == pygame.K_UP: snake.setDir('UP')
                if event.key == pygame.K_DOWN: snake.setDir('DOWN')

        # Update snake position
        snake.move(delta)

        # Check if snake eats the food
        foodPos = game.foodPos()
        if snake.eat(foodPos):
            game.newFoodPos()

        win.fill(black)

        # Draw the snake
        for sPos in snake.body():
            pygame.draw.rect(win, green, pygame.Rect(sPos[0], sPos[1], delta, delta))

        # Draw the food
        pygame.draw.rect(win, brown, pygame.Rect(foodPos[0], foodPos[1], delta, delta))

        pygame.display.update()
        time.sleep(.07)

        # run the game for 100 iterations
        if i == 100:
            pygame.quit()
            exit()
        i += 1
```



# `snakev5.py`: Lägg in gameOver testet

```python
class Snake():

    ...

    def isGameOver(self,size):
        snakePos , snakeBody , (width, height) = self._pos , self._body, size

        # Crashed with edges?
        if snakePos[0] >= width or snakePos[0] < 0:
            return True
        if snakePos[1] >= height or snakePos[1] < 0:
            return True

        # Self hit
        for block in snakeBody[1:]:
            if snakePos == block:
                return True

        return False

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")

    # Initialize the game and snake
    game  = Game()
    snake = Snake()
    delta = game.delta()

    # Make the window for the game
    win = pygame.display.set_mode(game.size())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: snake.setDir('RIGHT')
                if event.key == pygame.K_LEFT: snake.setDir('LEFT')
                if event.key == pygame.K_UP: snake.setDir('UP')
                if event.key == pygame.K_DOWN: snake.setDir('DOWN')

        # Update snake position
        snake.move(delta)

        # Check if snake eats the food
        foodPos = game.foodPos()
        if snake.eat(foodPos):
            game.newFoodPos()

        win.fill(black)

        # Draw the snake
        for sPos in snake.body():
            pygame.draw.rect(win, green, pygame.Rect(sPos[0], sPos[1], delta, delta))

        # Draw the food
        pygame.draw.rect(win, brown, pygame.Rect(foodPos[0], foodPos[1], delta, delta))

        if snake.isGameOver(game.size()):
            pygame.quit()
            exit()
        else:
            pygame.display.update()
            time.sleep(.07)
```



# `snakev6.py`: Lägg in poäng

```python
def drawText(win,s,color,pos):
    font = pygame.font.Font(None, 36)
    text = font.render(s, True, color)
    rect = text.get_rect()
    rect.midtop = pos
    win.blit(text, rect)

class Game():

    def __init__(self):
        self._size = (400,400)
        self._delta = 10
        self._score = 0
        self._foodPos = (300,50)

    ...

    def incScore(self):
        self._score += 1

    def score(self):
        return self._score

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")

    # Initialize the game and snake
    game  = Game()
    snake = Snake()
    delta = game.delta()

    # Make the window for the game
    win = pygame.display.set_mode(game.size())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: snake.setDir('RIGHT')
                if event.key == pygame.K_LEFT: snake.setDir('LEFT')
                if event.key == pygame.K_UP: snake.setDir('UP')
                if event.key == pygame.K_DOWN: snake.setDir('DOWN')

        # Update snake position
        snake.move(delta)

        # Check if snake eats the food
        foodPos = game.foodPos()
        if snake.eat(foodPos):
            game.newFoodPos()
            game.incScore()

        win.fill(black)

        # Draw score in upper left corner
        drawText(win,"Score: " + str(game.score()),white,(80,10))

        # Draw the snake
        for sPos in snake.body():
            pygame.draw.rect(win, green, pygame.Rect(sPos[0], sPos[1], delta, delta))

        # Draw the food
        pygame.draw.rect(win, brown, pygame.Rect(foodPos[0], foodPos[1], delta, delta))

        if snake.isGameOver(game.size()):
            pygame.quit()
            exit()
        else:
            pygame.display.update()
            time.sleep(.07)

main()
```

# `snake.py`: Komplett program där det skrivs "Game Over" när vi dött

```python
import pygame
import time
import random

# Colors
red   = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

def drawText(win,s,color,pos):
    font = pygame.font.Font(None, 36)
    text = font.render(s, True, color)
    rect = text.get_rect()
    rect.midtop = pos
    win.blit(text, rect)

# Class for the snake

class Snake():

    def __init__(self):
        self._pos = (100,50)
        self._body = [(100, 50), (90, 50), (80, 50)]
        self._dir = "RIGHT"

    def pos(self):
        return self._pos

    def body(self):
        return self._body

    def setDir(self, newDir):
        if self._dir == "RIGHT" and newDir != "LEFT":
            self._dir = newDir
        if self._dir == "LEFT" and newDir != "RIGHT":
            self._dir = newDir
        if self._dir == "UP" and newDir != "DOWN":
            self._dir = newDir
        if self._dir == "DOWN" and newDir != "UP":
            self._dir = newDir

    def move(self, delta):
        d , (p1 , p2) = self._dir , self._pos

        if d == 'RIGHT':
            self._pos = (p1 + delta,p2)
        if d == 'LEFT':
            self._pos = (p1 - delta,p2)
        if d == 'DOWN':
            self._pos = (p1,p2 + delta)
        if d == 'UP':
            self._pos = (p1,p2 - delta)

        self._body.insert(0, self._pos)

    def eat(self,foodPos):
        if self._pos == foodPos:
            return True
        else:
            self._body.pop()

    def isGameOver(self,size):
        snakePos , snakeBody , (width, height) = self._pos , self._body, size

        # Crashed with edges?
        if snakePos[0] >= width or snakePos[0] < 0:
            return True
        if snakePos[1] >= height or snakePos[1] < 0:
            return True

        # Self hit
        for block in snakeBody[1:]:
            if snakePos == block:
                return True

        return False

class Game():

    def __init__(self):
        self._size = (400,400)
        self._delta = 10
        self._score = 0
        self._foodPos = (300,50)

    def delta(self):
        return self._delta

    def size(self):
        return self._size

    def foodPos(self):
        return self._foodPos

    def newFoodPos(self):
        w , h = self.size()
        d     = self.delta()
        self._foodPos = (random.randrange(1, w // d) * d, random.randrange(1, h // d) * d)

    def incScore(self):
        self._score += 1

    def score(self):
        return self._score

def main():
    pygame.init()
    pygame.display.set_caption("Snake Game")

    # Initialize the game and snake
    game  = Game()
    snake = Snake()
    delta = game.delta()

    # Make the window for the game
    win = pygame.display.set_mode(game.size())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: snake.setDir('RIGHT')
                if event.key == pygame.K_LEFT: snake.setDir('LEFT')
                if event.key == pygame.K_UP: snake.setDir('UP')
                if event.key == pygame.K_DOWN: snake.setDir('DOWN')

        # Update snake position
        snake.move(delta)

        # Check if snake eats the food
        foodPos = game.foodPos()
        if snake.eat(foodPos):
            game.newFoodPos()
            game.incScore()

        win.fill(black)

        # Draw score in upper left corner
        drawText(win,"Score: " + str(game.score()),white,(80,10))

        # Draw the snake
        for sPos in snake.body():
            pygame.draw.rect(win, green, pygame.Rect(sPos[0], sPos[1], delta, delta))

        # Draw the food
        pygame.draw.rect(win, brown, pygame.Rect(foodPos[0], foodPos[1], delta, delta))

        if snake.isGameOver(game.size()):
            w , h = game.size()
            drawText(win, "Game Over", red, (w / 2, h / 2))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            exit()
        else:
            pygame.display.update()
            time.sleep(.07)

main()
```

# Vad har jag inte gjort?

Vi har nu implementerat ett fungerande Snake spel i Python! Vad har
jag inte gjort?

- Dokumentation (DocStrings och mer kommentarer)
- Testning och dokumentation genom testfall (mer i nästa föreläsning)
- Felhantering (vad händer om något går fel)

Reflektioner om koden:

- Används bra abstraktioner och funktioner?
- Kan man testa den på ett bra sätt?
- Är den väldokumeterad?
- Vad händer om något går fel?

# Läxa

* Skriv om koden så att huvudet på ormen har en annan färg.

* Gör så att maten inte kan hamna i kroppen på ormen.

* Gör så att det går snabbare och snabbare ju mer man har ätit.

