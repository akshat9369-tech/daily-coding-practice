"""Minimum Window Substring (Hard Sliding Window)."""

from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    target_counts = Counter(t)
    required = len(target_counts)
    window_counts = {}

    formed = 0
    left = 0
    ans = float("inf"), None, None

    for right, ch in enumerate(s):
        window_counts[ch] = window_counts.get(ch, 0) + 1
        if ch in target_counts and window_counts[ch] == target_counts[ch]:
            formed += 1

        while left <= right and formed == required:
            char_left = s[left]
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            window_counts[char_left] -= 1
            if char_left in target_counts and window_counts[char_left] < target_counts[char_left]:
                formed -= 1
            left += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

if __name__ == "__main__":
    s, t = "ADOBECODEBANC", "ABC"
    print(f"Min window in {s} containing {t}: {min_window(s, t)!r}")
