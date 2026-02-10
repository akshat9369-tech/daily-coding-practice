"""Two Pointers: 3Sum Problem (Unique Triplets)."""

def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    triplets = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return triplets

if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    print("3Sum unique triplets:", three_sum(arr))
