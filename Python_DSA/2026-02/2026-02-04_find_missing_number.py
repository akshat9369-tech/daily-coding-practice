"""Find the Missing Number in Range [0, n]."""

def find_missing_number_sum(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)

def find_missing_number_xor(nums: list[int]) -> int:
    xor_all = len(nums)
    for i, num in enumerate(nums):
        xor_all ^= i ^ num
    return xor_all

if __name__ == "__main__":
    arr = [3, 0, 1]
    print("Missing (sum method):", find_missing_number_sum(arr))
    print("Missing (xor method):", find_missing_number_xor(arr))
