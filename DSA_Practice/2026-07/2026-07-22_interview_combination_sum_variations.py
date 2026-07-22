"""Combination Sum III and IV."""

def combination_sum3(k: int, n: int) -> list[list[int]]:
    res = []
    def backtrack(start: int, combo: list[int], remain: int):
        if len(combo) == k:
            if remain == 0:
                res.append(list(combo))
            return
        for i in range(start, 10):
            if i > remain:
                break
            combo.append(i)
            backtrack(i + 1, combo, remain - i)
            combo.pop()

    backtrack(1, [], n)
    return res

if __name__ == "__main__":
    print("Combination Sum 3 (k=3, n=9):", combination_sum3(3, 9))
