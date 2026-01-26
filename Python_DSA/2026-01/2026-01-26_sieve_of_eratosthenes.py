"""Mathematical Algorithms: Sieve of Eratosthenes for Primes."""

def sieve_of_eratosthenes(limit: int) -> list[int]:
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1

    return [i for i, prime in enumerate(is_prime) if prime]

if __name__ == "__main__":
    n = 100
    primes = sieve_of_eratosthenes(n)
    print(f"Prime numbers up to {n} (count: {len(primes)}):")
    print(primes)
