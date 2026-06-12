"""Longest Substring Without Repeating Characters."""

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_length = 0

    for right, ch in enumerate(s):
        if ch in char_index_map and char_index_map[ch] >= left:
            left = char_index_map[ch] + 1
        char_index_map[ch] = right
        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    samples = ["abcabcbb", "bbbbb", "pwwkew", ""]
    for s in samples:
        print(f"String {s!r:12s} -> Longest Unique: {length_of_longest_substring(s)}")
