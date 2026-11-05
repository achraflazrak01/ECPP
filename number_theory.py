def gcd(a: int, b: int) -> int:
    """Greatest common divisor of a >= 0 and b >= 0 (Theorem 1.6)."""
    # Invariant: gcd(a, b) never changes   (Lemma 1.6.2)
    # Variant:   b gets strictly smaller   (Lemma 1.6.1)
    while b != 0:
        a, b = b, a % b         # Lemma 1.5
    return a                    # Lemma 1.6.3

def xgcd(a: int, b: int) -> tuple[int, int, int]:
    """Return (d, x, y) with d = gcd(a, b) and a*x + b*y == d, for a, b >= 0."""
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    # Invariant: r0 == s0*a + t0*b  and  r1 == s1*a + t1*b   (Lemma 1.7.4)
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return r0, s0, t0

def inverse_or_none(a: int, n: int) -> int | None:
    """Inverse of a modulo n (n >= 2), or None if gcd(a, n) > 1."""
    d, x, _ = xgcd(a % n, n)
    if d != 1:
        return None
    return x % n

def inverse_brute(a: int, n: int) -> int | None:
    a %= n
    for x in range(n):
        if (a * x) % n == 1:
            return x
    return None

class NotInvertible(Exception):
    """a has no inverse modulo n. The attribute g = gcd(a, n) is a factor of n."""
    def __init__(self, a, n, g):
        super().__init__(f"{a} has no inverse modulo {n} (gcd = {g})") # the factor we want to keep
        self.g = g

def inverse_mod(a: int, n: int) -> int:
    """Inverse of a modulo n (n >= 2), or NotInvertible Exception if gcd(a, n) > 1."""
    d, x, _ = xgcd(a % n, n)
    if d != 1:
        raise NotInvertible(a, n, d)
    return x % n

def find_factor(n: int, candidates: list[int])-> int | None:
    for a in candidates:
        try:
            inverse_mod(a, n)
        except NotInvertible as e:
            return e.g
    return None

