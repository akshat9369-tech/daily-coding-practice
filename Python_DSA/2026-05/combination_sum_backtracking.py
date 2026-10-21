"""Backtracking: Combination Sum I and II."""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result = []

    def backtrack(remain: int, combo: list[int], start: int):
        if remain == 0:
            result.append(list(combo))
            return
        elif remain < 0:
            return

        for i in range(start, len(candidates)):
            combo.append(candidates[i])
            backtrack(remain - candidates[i], combo, i)  # can reuse same candidate
            combo.pop()

    backtrack(target, [], 0)
    return result

if __name__ == "__main__":
    cands = [2, 3, 6, 7]
    tgt = 7
    print(f"Combinations for sum {tgt}:", combination_sum(cands, tgt))
