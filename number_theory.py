def gcd(a: int, b: int) -> int:
    """Greatest common divisor of a >= 0 and b >= 0 (Theorem 1.6)."""
    # Invariant: gcd(a, b) never changes   (Lemma 1.6.2)
    # Variant:   b gets strictly smaller   (Lemma 1.6.1)
    while b != 0:
        a, b = b, a % b         # Lemma 1.5
    return a                    # Lemma 1.6.3
