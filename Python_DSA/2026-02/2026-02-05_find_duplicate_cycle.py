"""Find Duplicate Number Using Floyd's Cycle Detection."""

def find_duplicate(nums: list[int]) -> int:
    slow = nums[0]
    fast = nums[0]

    # Find meeting point in cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Find entrance to cycle
    ptr1 = nums[0]
    ptr2 = slow
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

if __name__ == "__main__":
    arr = [1, 3, 4, 2, 2]
    print("Duplicate number is:", find_duplicate(arr))
