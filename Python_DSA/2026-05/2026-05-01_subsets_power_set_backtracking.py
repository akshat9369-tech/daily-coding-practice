"""Recursion: Subsets / Power Set Generation."""

def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    subset = []

    def backtrack(i: int):
        if i >= len(nums):
            result.append(subset.copy())
            return
        # Include nums[i]
        subset.append(nums[i])
        backtrack(i + 1)
        # Exclude nums[i]
        subset.pop()
        backtrack(i + 1)

    backtrack(0)
    return result

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(f"Subsets of {nums}:", subsets(nums))
