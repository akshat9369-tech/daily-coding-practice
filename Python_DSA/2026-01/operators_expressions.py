"""Arithmetic, Relational, and Logical Operators in Python."""

def evaluate_expressions(a: int, b: int):
    print(f"a = {a}, b = {b}")
    print(f"Addition        (a + b)  = {a + b}")
    print(f"Floor Division  (a // b) = {a // b}")
    print(f"Float Division  (a / b)  = {a / b:.4f}")
    print(f"Modulo          (a % b)  = {a % b}")
    print(f"Exponentiation  (a ** b) = {a ** b}")

    # Logical operations
    print(f"(a > 10 and b < 10)      = {a > 10 and b < 10}")
    print(f"(a == 20 or b == 3)      = {a == 20 or b == 3}")
    print(f"not (a < b)              = {not (a < b)}")

if __name__ == "__main__":
    evaluate_expressions(17, 5)
