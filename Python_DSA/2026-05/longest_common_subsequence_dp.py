"""DP: Longest Common Subsequence (LCS) Length and String."""

def lcs(text1: str, text2: str) -> tuple[int, str]:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if text1[i] == text2[j]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # Reconstruct string
    i, j = m, n
    lcs_chars = []
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs_chars.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], "".join(reversed(lcs_chars))

if __name__ == "__main__":
    s1, s2 = "abcde", "ace"
    length, substr = lcs(s1, s2)
    print(f"LCS between {s1!r} and {s2!r}: length={length}, string={substr!r}")
