"""Exception Handling: try, except, else, finally, and Custom Errors."""

class NegativeValueError(Exception):
    """Raised when an operation encounters an invalid negative value."""
    pass

def compute_square_root(n: float) -> float:
    if n < 0:
        raise NegativeValueError(f"Cannot compute real square root of negative number: {n}")
    return n ** 0.5

def safe_divide(a: float, b: float) -> float | None:
    try:
        result = a / b
    except ZeroDivisionError as err:
        print(f"Caught ZeroDivisionError: {err}")
        return None
    else:
        print(f"Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("Completed safe_divide invocation.")

if __name__ == "__main__":
    safe_divide(10, 2)
    safe_divide(10, 0)

    try:
        compute_square_root(-9)
    except NegativeValueError as err:
        print(f"Custom Error Caught: {err}")
