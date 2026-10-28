def euclid_gcd(a: int, b: int)->int:
    while b != 0:
        a, b = b, a % b
    return a

def euclid_gcd_rec(a: int, b: int)->int:
    if b == 0:
        return a
    return euclid_gcd(b, a % b)

print(euclid_gcd(18, 24))
print(euclid_gcd_rec(18, 24))