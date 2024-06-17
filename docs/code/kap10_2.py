class Polygon:
    def __init__(self, n_sides, n_unique_sides=None):
        self.n_sides = n_sides
        if n_unique_sides:
            self.n_unique_sides = n_unique_sides
        else:
            self.n_unique_sides = n_sides
        if self.n_sides % self.n_unique_sides:
            raise ValueError(
                "The total number of sides must be an integer"
                " multiple of the number of unique sides")
        self.sides = None
        self.__name__ = 'Polygon'

    def _check_sides(self):
        if not all(map(lambda x: x > 0, self.sides)):
            print("Invalid side lengths.")
            return False
        else:
            return True

    def _get_side(self, side_no):
        s = float(input("Enter side " + str(side_no + 1) + " : "))
        return s

    def input_sides(self):
        print("Please enter the " + str(self.n_unique_sides) + " unique"
              " side lengths for a " + self.__name__)
        unique_sides = [self._get_side(i) for i in range(self.n_unique_sides)]
        self.sides = unique_sides * (self.n_sides // self.n_unique_sides)
        if not self._check_sides():
            print("Please provide positive side lenghts.")
            self.input_sides()

    def display_sides(self):
        if self._check_sides:
            for i in range(self.n_sides):
                print("Length of side", i + 1, ":", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
        self.__name__ = 'Triangle'

    # method specific to triangles
    def get_area(self):
        a, b, c = sorted(self.sides)
        if c > (a + b):
            print("Non-valid side lengths for a triangle.")
            return
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c))**0.5


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4, n_unique_sides=2)
        self.__name__ = 'Rectangle'

    def get_area(self):
        return self.sides[0] * self.sides[1]

    # method specific for rectangles
    def get_diagonal(self):
        return (self.sides[0]**2 + self.sides[1]**2)**0.5


class Square(Rectangle):
    def __init__(self):
        super(Rectangle, self).__init__(4, n_unique_sides=1)
        self.__name__ = 'Square'

    def get_corner_coordinates(self):
        s = self.sides[0]/2
        return ((-s, -s), (-s, s), (s, s), (s, -s))


t = Triangle()
t.input_sides()
print('The area of the triangle is:', t.get_area())
t.display_sides()

r = Rectangle()
r.input_sides()
print('The area of the rectangle is:', r.get_area())
print('The diagonal of the rectangle is:', r.get_diagonal())

s = Square()
s.input_sides()
print('The area of the square is:', s.get_area())
print('The diagonal of the square is:', s.get_diagonal())
print('The coordinates of the square corners are:\n',
      s.get_corner_coordinates())
