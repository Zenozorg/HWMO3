class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area
        return False

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.area != other.area
        return False

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price
        return NotImplemented

    def __repr__(self):
        return f"Flat(area={self.area}, price={self.price})"

flat1 = Flat(60, 100000)
flat2 = Flat(80, 150000)
flat3 = Flat(60, 120000)

print(flat1 == flat2)
print(flat1 != flat2)
print(flat1 == flat3)
print(flat1 != flat3)

print(flat1 < flat2) 
print(flat1 > flat2)
print(flat1 <= flat3)
print(flat1 >= flat3)
