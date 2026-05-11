"""DP: House Robber I and II (Linear and Circular)."""

def rob_linear(nums: list[int]) -> int:
    rob1, rob2 = 0, 0
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

def rob_circular(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    # Either omit first house or omit last house
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

if __name__ == "__main__":
    houses = [2, 7, 9, 3, 1]
    print("Linear robber max loot  :", rob_linear(houses))
    print("Circular robber max loot:", rob_circular(houses))
