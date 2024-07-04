class Airplane:
    def __init__(self, airplane_type, max_passengers, current_passengers):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.airplane_type == other.airplane_type
        return False

    def __add__(self, value):
        if isinstance(value, int):
            return Airplane(self.airplane_type, self.max_passengers, self.current_passengers + value)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, int):
            return Airplane(self.airplane_type, self.max_passengers, self.current_passengers - value)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, int):
            self.current_passengers += value
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, int):
            self.current_passengers -= value
            return self
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented

    def __repr__(self):
        return (f"Airplane(type={self.airplane_type}, max_passengers={self.max_passengers}, "
                f"current_passengers={self.current_passengers})")

a1 = Airplane("Boeing 737", 200, 150)
a2 = Airplane("Airbus A320", 180, 120)
a3 = Airplane("Boeing 737", 250, 200)

print(a1 == a2) 
print(a1 == a3) 

a4 = a1 + 30
print(a4) 
a1 += 20
print(a1)
a1 -= 50
print(a1) 

print(a1 > a2)  
print(a1 < a3)   
print(a2 <= a3)  
print(a1 >= a2)
