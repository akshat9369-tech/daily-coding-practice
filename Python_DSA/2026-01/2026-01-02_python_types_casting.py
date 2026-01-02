"""Python Variables, Dynamic Typing, and Type Casting."""

def demonstrate_types():
    num_int = 42
    num_float = 3.14159
    text = "100"
    is_valid = True

    # Type conversions
    parsed_int = int(text)
    float_to_int = int(num_float)
    int_to_str = str(num_int)

    print(f"Original text: {text!r} -> int: {parsed_int} (type: {type(parsed_int).__name__})")
    print(f"Float {num_float} truncated to int: {float_to_int}")
    print(f"Int to string: {int_to_str!r} (type: {type(int_to_str).__name__})")
    print(f"Boolean value: {is_valid} (int value: {int(is_valid)})")

if __name__ == "__main__":
    demonstrate_types()
