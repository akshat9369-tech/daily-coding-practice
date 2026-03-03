"""Stack: Valid Parentheses Validator."""

def is_valid_parentheses(s: str) -> bool:
    matching = {")": "(", "}": "{", "]": "["}
    stack = []

    for ch in s:
        if ch in matching.values():
            stack.append(ch)
        elif ch in matching:
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == "__main__":
    tests = ["()[]{}", "([{}])", "(]", "([)]", "{[]}"]
    for t in tests:
        print(f"Expression {t:7s} -> Valid: {is_valid_parentheses(t)}")
