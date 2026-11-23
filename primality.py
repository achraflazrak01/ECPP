import random
from number_theory import gcd, is_prime_trial, factor_trial
from modular import pow_mod, units, phi

def order_mod(a, n):
    """Multiplicative order of a modulo n (a must be a unit)."""
    if gcd(a, n) != 1:
        raise ValueError("a is not a unit modulo n")
    k, x = 1, a % n
    while x != 1 % n:
        x = (x * a) % n
        k = k + 1
    return k

FILTER_PRIMES = [p for p in range(2, 100) if all(p % q for q in range(2, p))]
FILTER_BASES = [2, 3, 5, 7]

def may_be_prime(n: int)-> bool:
    """A compositeness filter. False: n is certainly composite. True: n passed, NOT a proof."""
    if n < 2:
        return False
    for p in FILTER_PRIMES:
        if n % p == 0:
            return n == p
    for a in FILTER_BASES:
        if pow_mod(a, n - 1, n) != 1:
            return False
    return True

