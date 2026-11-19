from modular import *

import random

rng = random.Random(42)

def test_mod_class():
    a = Mod(3, 7)
    assert a + Mod(5, 7) == Mod(1, 7)
    assert a - 5 == Mod(5, 7)
    assert -a == 4
    assert a * 5 == 1
    assert 1 + a == Mod(4, 7)
    assert a.inverse() == 5
    assert Mod(2, 7) / Mod(3, 7) == Mod(3, 7)
    assert a ** 6 == 1 and a ** -1 == 5
    assert repr(a) == "Mod(3, 7)"
    for _ in range(1000):
        n = rng.randint(1, 10**30)
        x, y = rng.randint(-10**40, 10**40), rng.randint(-10**40, 10**40)
        assert Mod(x, n) * Mod(y, n) == Mod(x * y, n)
        assert Mod(x, n) + Mod(y, n) == Mod(x + y, n)

def random_number(max_bits=256):
    bits = rng.randint(0, max_bits)
    return rng.getrandbits(bits)

def test_naive_exp_random():
    for _ in range(2000):
        a = random_number(200)
        e = random_number(200)
        n = random_number(200)
        while n == 0:
            n = random_number(200)
        assert pow_naive(a, e, n) == pow(a, e, n)


def test_fast_exp_random():
    for _ in range(2000):
        a = random_number(200)
        e = random_number(200)
        n = random_number(200)
        while n == 0:
            n = random_number(200)
        assert pow_mod(a, e, n) == pow(a, e, n)

if __name__ == "__main__":
    test_mod_class()
    assert crt_pair(2, 3, 3, 5) == 8
    assert crt([2, 3, 2], [3, 5, 7]) == 23
    test_fast_exp_random()
    assert pow_naive(3, 13, 7) == 3