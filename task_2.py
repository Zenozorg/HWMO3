class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denom = other.real**2 + other.imag**2
            real_part = (self.real * other.real + self.imag * other.imag) / denom
            imag_part = (self.imag * other.real - self.real * other.imag) / denom
            return Complex(real_part, imag_part)
        return NotImplemented

    def __repr__(self):
        return f"Complex(real={self.real}, imag={self.imag})"

    def __str__(self):
        return f"({self.real} + {self.imag}i)"

c1 = Complex(2, 3)
c2 = Complex(4, 5)

print(c1 + c2)
print(c1 - c2) 
print(c1 * c2) 
print(c1 / c2)
