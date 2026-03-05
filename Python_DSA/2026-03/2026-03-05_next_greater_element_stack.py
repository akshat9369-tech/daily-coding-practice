"""Stack: Next Greater Element using Monotonic Decreasing Stack."""

def next_greater_elements(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [-1] * n
    stack = []  # stores indices

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            res[idx] = nums[i]
        stack.append(i)

    return res

if __name__ == "__main__":
    nums = [4, 5, 2, 25, 7, 18]
    print("Array:", nums)
    print("NGE  :", next_greater_elements(nums))
