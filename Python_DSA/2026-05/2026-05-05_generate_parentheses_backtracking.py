"""Backtracking: Generate Valid Parentheses."""

def generate_parentheses(n: int) -> list[str]:
    result = []

    def backtrack(curr_str: str, open_count: int, close_count: int):
        if len(curr_str) == 2 * n:
            result.append(curr_str)
            return
        if open_count < n:
            backtrack(curr_str + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(curr_str + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result

if __name__ == "__main__":
    n = 3
    print(f"Valid parentheses of length {2*n}:", generate_parentheses(n))
