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

print([order_mod(a, 11) for a in range(1, 11)])