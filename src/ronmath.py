from __future__ import annotations

class Rational:
    def __init__(self,
                 n: int,
                 d: int
                 ):
        self.n = n
        self.d = d
        return
    
    def __repr__(self) -> str:
        return f'{self.n}/{self.d}'
    
    def __add__(self, other) -> Rational:
        n = self.n*other.d + self.d*other.n
        d = self.d*other.d
        return Rational(n, d)
    
    def __sub__(self, other) -> Rational:
        n = self.n*other.d - self.d*other.n
        d = self.d*other.d
        return Rational(n ,d)

    def __mul__(self, other) -> Rational:
        n = self.n*other.n
        d = self.d*other.d
        return Rational(n, d)

    def __truediv__(self, other) -> Rational:
        n = self.n * other.d
        d = self.d * other.n
        return Rational(n, d)
    
    def __float__(self):
        # Do the division. Do this as last as possible.
        return self.n/self.d
    
    def __lt__(self, other) -> bool:
        return float(self) < float(other)
    
    def __eq__(self, other) -> bool:
        x = self.reduce()
        y = other.reduce()
        return (x.n == y.n) and (self.d == other.d)

    def gcd(x:int, y:int):
        if y==0:
            return x
        else:
            return Rational.gcd(y, x%y)
    
    def reduce(self):
        g = Rational.gcd(self.n, self.d)
        self.n = self.n//g
        self.d = self.d//g
        return self
    
class Complex:
    def __init__(self,
                 real: Rational,
                 imag: Rational
                 ):
        self.real = real
        self.imag = imag
        return
    
    def __repr__(self) -> str:
        return f'{self.real} + {self.imag}i'
    
    def __add__(self, other) -> Complex:
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)