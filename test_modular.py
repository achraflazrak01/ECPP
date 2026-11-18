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

if __name__ == "__main__":
    test_mod_class()
    assert crt_pair(2, 3, 3, 5) == 8
    assert crt([2, 3, 2], [3, 5, 7]) == 23