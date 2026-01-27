"""Mathematical Algorithms: Euclidean GCD and Fast Exponentiation."""

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Returns (gcd, x, y) such that a*x + b*y = gcd(a, b)."""
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def modular_exponentiation(base: int, exp: int, mod: int) -> int:
    res = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

if __name__ == "__main__":
    print("GCD(48, 18):", gcd(48, 18))
    g, x, y = extended_gcd(35, 15)
    print(f"Extended GCD: 35*({x}) + 15*({y}) = {g}")
    print("Modular Exponentiation (3^13 % 7):", modular_exponentiation(3, 13, 7))
