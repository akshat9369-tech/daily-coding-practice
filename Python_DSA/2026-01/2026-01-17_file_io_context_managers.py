"""File I/O and Context Managers (with statement)."""

import tempfile
import os

def demonstrate_file_io():
    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as tmp:
        tmp_name = tmp.name
        tmp.write("Day 17: Python File I/O\n")
        tmp.write("Line 2: Context managers ensure automatic resource cleanup.\n")
        tmp.write("Line 3: Final check line.\n")

    try:
        with open(tmp_name, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(f"Read {len(lines)} lines from temporary file:")
            for idx, line in enumerate(lines, 1):
                print(f"  [{idx}] {line.strip()}")
    finally:
        if os.path.exists(tmp_name):
            os.remove(tmp_name)

if __name__ == "__main__":
    demonstrate_file_io()
