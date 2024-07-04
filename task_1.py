class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() < other.circumference()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.circumference() <= other.circumference()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() > other.circumference()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.circumference() >= other.circumference()
        return NotImplemented
    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius - value)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            self.radius -= value
            return self
        return NotImplemented

    def __repr__(self):
        return f"Circle(radius={self.radius})"
c1 = Circle(5)
c2 = Circle(10)

print(c1 == c2)
print(c1 < c2)
print(c1 > c2) 
print(c1 <= c2)
print(c1 >= c2)

c3 = c1 + 3
print(c3)

c4 = c2 - 5
print(c4)

c1 += 2
print(c1)

c2 -= 3
print(c2)
