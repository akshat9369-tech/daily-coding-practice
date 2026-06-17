"""Next Greater Element II (Circular Array)."""

def next_greater_elements_circular(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(2 * n):
        idx = i % n
        while stack and nums[stack[-1]] < nums[idx]:
            popped_idx = stack.pop()
            result[popped_idx] = nums[idx]
        if i < n:
            stack.append(idx)

    return result

if __name__ == "__main__":
    sample = [1, 2, 1]
    print("Array:", sample)
    print("Circular NGE:", next_greater_elements_circular(sample))
