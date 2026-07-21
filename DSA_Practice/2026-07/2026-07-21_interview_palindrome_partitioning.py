"""Palindrome Partitioning (Backtracking with DP Matrix)."""

def partition_palindrome(s: str) -> list[list[str]]:
    res = []
    part = []

    def is_pal(sub: str) -> bool:
        return sub == sub[::-1]

    def dfs(i: int):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            sub = s[i:j + 1]
            if is_pal(sub):
                part.append(sub)
                dfs(j + 1)
                part.pop()

    dfs(0)
    return res

if __name__ == "__main__":
    print("Partitions of 'aab':", partition_palindrome("aab"))
