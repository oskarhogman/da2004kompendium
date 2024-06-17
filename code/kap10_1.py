"""Code to create class UML diagrams for kap10.md

This uses pylint. Run with
>>> pyreverse -o pdf kap10.py
"""


class A:
    """This is a base class
    """
    class_integer = 10

    def __init__(self):
        self.vals = [5]

    def power_sum(self):
        return sum([i**2 for i in self.vals]) + A.class_integer

class B(A):
    """This is a sub class
    """
    def __init__(self, x, y):
        self.vals = [x, y]

    def print_result(self):
        print(self.power_sum())

a = A()
print(a.power_sum())   # method defined in A

b = B(10, 20)
print(b.power_sum())   # calling method in B inherited from A
b.print_result()       # uses method specific to B

class C(A):
    def __init__(self, y):
        super().__init__()
        self.vals.append(y)
        
class D(B):
    def __init__(self, y):
        super().__init__(5, 10)
        self.vals.append(y)

c = C(10)
d = D(10)
print(c.power_sum())
d.print_result()
c.print_result()       # raises an Error

