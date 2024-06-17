import warnings  # included in Python's standard library

class Course:

    def __init__(self, code, name, year=2020):       # Constructor
        self.participants = []
        self.code = code
        self.name = name
        self.year = year

    def _check_duplicate(self, p):
        for other in self.participants:
            if p.name() == other.name(): # check if identical name
                # raise warning and print message if identical name:
                warnings.warn(f'Name already exists under entry:' + str(p))

    def number_participants(self):
        return len(self.participants)

    def new_participant(self, p):
        self._check_duplicate(p)
        self.participants.append(p)


class Participant:

    def __init__(self, fname, lname, email): 
        self._fname = fname 
        self._lname = lname 
        self._email = email

    def name(self):
        return self._fname + ' ' + self._lname

    def email(self):
        return self._email
        

c = Course('DA2004', 'ProgTek')
p1 = Participant('Lasse', 'Arve', 'a@b')
p2 = Participant('Anna', 'Ukas', 'a@b')
p3 = Participant('Lasse', 'Arve', 'c@b')
c.new_participant(p1)
c.new_participant(p2)
c.new_participant(p3)
