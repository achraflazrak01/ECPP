import math

from number_theory import gcd, xgcd
import random

rng = random.Random(42)

def test_gcd_examples():
    assert gcd(1071, 462) == 21
    assert gcd(252, 198) == 18
    assert gcd(462, 1071) == 21  # a < b
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0
    assert gcd(17, 5) == 1  # coprime

def random_number(max_bits=256):
    bits = rng.randint(0, max_bits)
    return rng.getrandbits(bits)

def test_gcd_random():
    for _ in range(5000):
        a = random_number()
        b = random_number()
        d = gcd(a, b)
        if d != 0:
            assert gcd(a // d, b // d) == 1
            assert gcd (a, b) == math.gcd(a, b)

def test_xgcd():
    assert xgcd(240, 46) == (2, -9, 47)
    assert xgcd(1071, 462) == (21, -3, 7)
    for _ in range(5000):
        a = random_number()
        b = random_number()
        d, x, y = xgcd(a, b)
        assert a * x + b * y == d
        assert d == gcd(a, b)


if __name__ == "__main__":
    test_gcd_examples()
    print("All tests passed.")
    print(random_number())
    test_gcd_random()
    print("All tests passed.")
    test_xgcd()
    print("All tests passed.")