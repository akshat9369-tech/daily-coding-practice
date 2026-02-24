"""Binary Search: Find First and Last Position of Element."""

def search_range(nums: list[int], target: int) -> list[int]:
    def find_bound(is_first: bool) -> int:
        low, high = 0, len(nums) - 1
        bound = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return bound

    return [find_bound(True), find_bound(False)]

if __name__ == "__main__":
    arr = [5, 7, 7, 8, 8, 10]
    print("Range for 8:", search_range(arr, 8))
    print("Range for 6:", search_range(arr, 6))
