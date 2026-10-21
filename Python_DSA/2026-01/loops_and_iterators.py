"""Loops and Iterators (for, while, range, enumerate, zip)."""

def demonstrate_iterations():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    scores = [88, 92, 79, 95]

    print("Enumeration:")
    for idx, name in enumerate(names, start=1):
        print(f"  Rank {idx}: {name}")

    print("\nZipped iteration:")
    for name, score in zip(names, scores):
        print(f"  {name:7s} -> {score} pts")

    print("\nWhile loop accumulator:")
    total, step = 0, 1
    while step <= 10:
        total += step
        step += 1
    print(f"  Sum 1..10 = {total}")

if __name__ == "__main__":
    demonstrate_iterations()
