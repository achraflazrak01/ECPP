
from number_theory import inverse_mod, gcd, is_prime_trial


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

def fermat_liars(n):
    """Bases 1 <= a < n with gcd(a, n) = 1 and a**(n-1) = 1 mod n."""
    return [a for a in range(1, n) if gcd(a, n) == 1 and pow(a, n - 1, n) == 1]

def crt_pair(a, n, b, m):
    """The x in [0, n*m) with x = a mod n and x = b mod m, for gcd(n, m) = 1."""
    m_inv = inverse_mod(m, n)           # m * m_inv = 1 mod n
    n_inv = inverse_mod(n, m)           # n * n_inv = 1 mod m
    return (a * m * m_inv + b * n * n_inv) % (n * m)

def crt(residues, moduli):
    """Solve x = residues[i] mod moduli[i] for pairwise coprime moduli."""
    x, N = 0, 1
    for a, n in zip(residues, moduli):
        x = crt_pair(x, N, a, n)
        N *= n
    return x