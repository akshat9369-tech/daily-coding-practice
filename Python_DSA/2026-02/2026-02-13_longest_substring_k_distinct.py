"""Sliding Window: Longest Substring with At Most K Distinct Characters."""

def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    if not s or k == 0:
        return 0

    char_freq = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        char_freq[s[right]] = char_freq.get(s[right], 0) + 1

        while len(char_freq) > k:
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                del char_freq[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

if __name__ == "__main__":
    text = "eceba"
    k = 2
    print(f"Longest substring with at most {k} distinct characters:",
          length_of_longest_substring_k_distinct(text, k))
