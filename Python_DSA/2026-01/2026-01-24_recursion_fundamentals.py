"""Recursion Fundamentals: Factorial and Fibonacci with Memoization."""

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci_memo(n: int, memo: dict[int, int] | None = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    print(f"Factorial(6) = {factorial(6)}")
    print("Fibonacci first 12 terms:")
    for i in range(12):
        print(f"  F({i}) = {fibonacci_memo(i)}")
