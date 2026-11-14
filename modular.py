
from number_theory import inverse_mod


class Mod:
    def __init__(self, value, n):
        if n < 1:
            raise ValueError("Modulus must be positive")
        self.n = n
        self.value = value % n

    def _check(self, other):
        if isinstance(other, int):
            return Mod(other, self.n)

        if isinstance(other, Mod):
            if self.n != other.n:
                raise ValueError("Different moduli")
            return other

        return NotImplemented

    def __repr__(self):
        return f"Mod({self.value}, {self.n})"

    def __add__(self, other):
        other = self._check(other)
        if other is NotImplemented:
            return NotImplemented
        return Mod(self.value + other.value, self.n)

    __radd__ = __add__

    def __neg__(self):
        return Mod(-self.value, self.n)

    def __sub__(self, other):
        other = self._check(other)
        if other is NotImplemented:
            return NotImplemented
        return Mod(self.value - other.value, self.n)

    def __rsub__(self, other):
        other = self._check(other)
        if other is NotImplemented:
            return NotImplemented
        return other - self

    def __mul__(self, other):
        other = self._check(other)
        if other is NotImplemented:
            return NotImplemented
        return Mod(self.value * other.value, self.n)

    __rmul__ = __mul__

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other % self.n

        if isinstance(other, Mod):
            return self.n == other.n and self.value == other.value

        return NotImplemented

    def inverse(self):
        if self.n < 2:
            raise ValueError("Modulus must be at least 2")
        return Mod(inverse_mod(self.value, self.n), self.n)

    def __truediv__(self, other):
        other = self._check(other)
        if other is NotImplemented:
            return NotImplemented
        return self * other.inverse()

    def __pow__(self, e):
        if not isinstance(e, int):
            return NotImplemented

        if e < 0:
            return self.inverse() ** (-e)

        return Mod(pow(self.value, e, self.n), self.n)
