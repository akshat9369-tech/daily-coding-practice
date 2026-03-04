"""Stack: Evaluate Reverse Polish Notation."""

def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b),
    }

    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))

    return stack[0]

if __name__ == "__main__":
    expr = ["2", "1", "+", "3", "*"]
    print(f"RPN {expr} = {eval_rpn(expr)}")
    expr2 = ["4", "13", "5", "/", "+"]
    print(f"RPN {expr2} = {eval_rpn(expr2)}")
