"""Recursion: Permutations of Distinct Elements."""

def permute(nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(curr: list[int], remaining: list[int]):
        if not remaining:
            result.append(curr)
            return
        for i in range(len(remaining)):
            backtrack(curr + [remaining[i]], remaining[:i] + remaining[i+1:])

    backtrack([], nums)
    return result

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(f"Permutations of {nums}:", permute(nums))
