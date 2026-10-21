"""Insertion Sort with Custom Key Comparators."""

from typing import Callable, Any

def insertion_sort(arr: list[Any], key: Callable[[Any], Any] = lambda x: x) -> list[Any]:
    res = arr.copy()
    for i in range(1, len(res)):
        curr_item = res[i]
        curr_key = key(curr_item)
        j = i - 1
        while j >= 0 and key(res[j]) > curr_key:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = curr_item
    return res

if __name__ == "__main__":
    words = ["banana", "pie", "apple", "strawberry", "kiwi"]
    # Sort by length
    by_length = insertion_sort(words, key=len)
    print("Sorted by length:", by_length)

    students = [("Alice", 85), ("Bob", 95), ("Charlie", 70)]
    by_grade = insertion_sort(students, key=lambda s: s[1])
    print("Sorted by score :", by_grade)
