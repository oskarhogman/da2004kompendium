class ProgMon():
    def __init__(self):
        self._attack = 0.0
        self._defense = 0.0
        self._caffeinated = False
        self._unit_testing = False

    def __str__(self):
        return "<ProgMon object>"

    def get_attack(self):
        if self._caffeinated:
            return 2 * self._attack
        else:
            return self._attack

    def get_defense(self):
        if self._unit_testing:
            return 2 * self._defense
        else:
            return self._defense

    def fight(self, other_progmon):
        '''
        Attack is the best form of defense!
        Returns (True, False) if self wins, (False, True) if other_progmon
        wins and (False, False) otherwise.
        '''
        if self.get_attack() > other_progmon.get_defense():
            return (True, False)
        elif other_progmon.get_attack() > self.get_defense():
            return (False, True)
        else:
            return (False, False)


class Hacker(ProgMon):
    def __init__(self):
        super().__init__()  # Call the superclass constructor!
        self._attack = 0.5
        self._defense = 0.25

    def __str__(self):
        return "<Hacker A=" + str(self._attack) + ">"

    
class Newbie(ProgMon):
    def __init__(self):
        super().__init__()
        self._attack = 0.15
        self._defense = 0.1

    def __str__(self):
        return "<Newbie>"

    
class Guru(ProgMon):
    def __init__(self):
        super().__init__()
        self._attack = 1.0
        self._defense = 1.0

    # method overloading
    def fight(self, other_progmon):
        '''
        Don't win, don't lose.
        '''
        # same type of return value as in the super class
        return (False, False)
    
        
h = Hacker()
n = Newbie()
g = Guru()
print(n.fight(h))
print(g.fight(h))
print(h.fight(n))


class HackerDojo():
    def __init__(self):
        self._members = []

    def add_member(self, m):
        self._members.append(m)

    def challenge(self, pm):
        for monster in self._members:
            win, loose = pm.fight(monster)
            if loose:
                # Lost against one member, challenge failed.
                return False
        # Won against all members of the dojo
        return True

print('Hacker dojo')
dojo = HackerDojo()
dojo.add_member(h)
dojo.add_member(n)
print('Dojo vs guru:', dojo.challenge(g))
print('Dojo vs newbie:', dojo.challenge(n))
