"""Word Break I and II (DP and Backtracking with Memo)."""

def word_break(s: str, word_dict: list[str]) -> bool:
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]

if __name__ == "__main__":
    s = "leetcode"
    dict_words = ["leet", "code"]
    print(f"Can segment {s!r}:", word_break(s, dict_words))
