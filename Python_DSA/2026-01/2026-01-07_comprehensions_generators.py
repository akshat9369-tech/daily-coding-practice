"""List Comprehensions and Generator Expressions."""

def demonstrate_comprehensions():
    numbers = list(range(1, 16))

    # List comprehension: squares of even numbers
    even_squares = [x * x for x in numbers if x % 2 == 0]
    print(f"Even squares: {even_squares}")

    # Dict comprehension: number to parity label
    parity_map = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 6)}
    print(f"Parity mapping: {parity_map}")

    # Generator expression (memory efficient sum of cubes)
    sum_cubes = sum(x ** 3 for x in range(1, 101))
    print(f"Sum of first 100 cubes (via generator): {sum_cubes}")

if __name__ == "__main__":
    demonstrate_comprehensions()
