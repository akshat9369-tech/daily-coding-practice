"""Lambda Functions with Map, Filter, and Reduce."""

from functools import reduce

def functional_pipeline():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Filter odd numbers
    odds = list(filter(lambda x: x % 2 != 0, nums))
    print("Odd numbers:", odds)

    # Map to their cubes
    cubes = list(map(lambda x: x ** 3, odds))
    print("Cubes of odds:", cubes)

    # Reduce to compute cumulative sum
    total_sum = reduce(lambda acc, curr: acc + curr, cubes)
    print("Sum of cubes:", total_sum)

    # Max element via reduce
    max_val = reduce(lambda a, b: a if a > b else b, nums)
    print("Max element:", max_val)

if __name__ == "__main__":
    functional_pipeline()
