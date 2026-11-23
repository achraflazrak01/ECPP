from primality import may_be_prime
from number_theory import is_prime_trial


def test_filter():
    for n in range(20000):
        assert may_be_prime(n) == is_prime_trial(n)
    for n in [561, 1105, 1729, 341]:
        assert not may_be_prime(n)

def test_filter_is_not_a_proof():
    assert may_be_prime(721801) and 721801 == 601 * 1201
    n = 211 * 421 * 631
    assert may_be_prime(n) and not is_prime_trial(n)

if __name__ == "__main__":
    test_filter()
    test_filter_is_not_a_proof()
    first = next(n for n in range(2, 10**6) if may_be_prime(n) and not is_prime_trial(n))
    print(first)