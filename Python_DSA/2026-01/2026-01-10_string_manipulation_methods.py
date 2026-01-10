"""String Manipulation, Slicing, and Formatting Methods."""

def string_operations():
    raw_text = "  Structured Python & Algorithm Practice 2026!  "
    cleaned = raw_text.strip()

    print(f"Cleaned   : {cleaned!r}")
    print(f"Uppercase : {cleaned.upper()}")
    print(f"Titlecase : {cleaned.title()}")
    print(f"Words     : {cleaned.split()}")

    # Slicing
    reversed_str = cleaned[::-1]
    print(f"Reversed  : {reversed_str[:25]}...")

    # Join operation
    slug = "-".join(word.lower() for word in cleaned.split() if word.isalnum())
    print(f"Generated slug: {slug}")

if __name__ == "__main__":
    string_operations()
