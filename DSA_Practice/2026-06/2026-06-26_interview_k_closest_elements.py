"""Find K Closest Elements to Target."""

def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    low = 0
    high = len(arr) - k

    while low < high:
        mid = (low + high) // 2
        if x - arr[mid] > arr[mid + k] - x:
            low = mid + 1
        else:
            high = mid

    return arr[low:low + k]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("4 closest to 3:", find_closest_elements(arr, 4, 3))
    print("4 closest to -1:", find_closest_elements(arr, 4, -1))
