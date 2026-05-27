"""Hashing: Longest Consecutive Sequence in O(N)."""

def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Check if it's the start of a streak
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print("Longest consecutive sequence length:", longest_consecutive(nums))
