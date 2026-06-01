"""Two Sum (Hash Map and Two Pointer Variants)."""

def two_sum_hash_map(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def two_sum_all_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
    seen = set()
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)

if __name__ == "__main__":
    nums = [2, 7, 11, 15, 3, 6]
    target = 9
    print("Indices for target 9:", two_sum_hash_map(nums, target))
    print("All unique value pairs:", two_sum_all_pairs(nums, target))
