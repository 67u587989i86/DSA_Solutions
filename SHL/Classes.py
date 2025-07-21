class Rectangle:
    def __init__(self, l, b):
        if l <= 0 or b <= 0:
            raise ValueError("Length and breadth must be positive")
        self.length = l
        self.breadth = b
        self.area = l * b   # calculation ho gaya object bante hi

r = Rectangle(4, 5)
print(r.area)  # Output: 20




class Student:
    def __init__(self, naam):
        self.naam = naam
        self.roll = self.generate_roll()

    def generate_roll(self):
        import random
        return random.randint(100, 999)

s = Student("Meena")
print(s.naam, s.roll)
